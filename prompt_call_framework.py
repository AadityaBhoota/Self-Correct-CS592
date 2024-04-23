from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio
import re
from anthropic import AsyncAnthropic
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
load_dotenv()

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

main_system_prompt = "You are a Python expert, who is tasked with a few problems. You carefully plan out everything. You make sure the plan makes sense before you start coding. You only code each step at a time, and you check to see if it follows your plan."
main_promblem_prompt = "[[problem]]"
main_planning_prompt = "Let me plan it out step-by-step first:"
main_plan_eval_prompt = "Are you sure this plan makes sense to do?"
main_plan_redo_prompt = "Okay. Re-plan it."
main_code_gen_prompt = "Good. Now implement step [[step]]."
main_code_eval_prompt = "Are you sure this implements step [[step]] correctly?"
main_code_redo_prompt = "Okay. Re-implement step [[step]]."
main_final_prompt = "Good. Now return correct code. Only return code."

problem = """from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    \"\"\"
"""


async def prompt_openai(system_prompt, messages, logprobs=None, top_logprobs=None, max_tokens=None, num_responses=1):
    all_messages = []
    all_messages.append({"role": "system", "content": system_prompt})
    for message in messages:
        all_messages.append(message)
    completion = await openai_client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=all_messages,
        logprobs=logprobs,
        top_logprobs=top_logprobs,
        max_tokens=max_tokens,
        n=num_responses
    )
    print(completion)
    return completion


async def prompt_anthropic(system_prompt, messages, max_tokens=4096, temperature=1.0):
    message = await anthropic_client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=max_tokens,
        temperature=temperature,
        system=system_prompt,
        messages=messages
    )

    print(message)
    return message


async def planning_stage(model, messages, system_prompt, planning_prompt):
    messages.append({"role": "assistant", "content": planning_prompt})
    if model == "openai":
        response = await prompt_openai(system_prompt, messages)
        plan = response.choices[0].message.content
    elif model == "anthropic":
        response = await prompt_anthropic(system_prompt, messages)
        plan = response.content[0].text

    return plan


async def full_code_generation(model, plan, problem, full_code_generation_prompts):
    prompt = full_code_generation_prompts[1].replace("[[problem]]", problem).replace("[[plan]]", plan)
    if model == "openai":
        response = await prompt_openai(full_code_generation_prompts[0], prompt)
        plan = response.choices[0].message.content
    elif model == "anthropic":
        response = await prompt_anthropic(full_code_generation_prompts[0], prompt)
        plan = response.content

    return plan


async def planning_update(model, messages, system_prompt, plan_eval_prompt, plan_redo_prompt, max_iterations=3):
    final_plan = messages[-1]["content"]
    num_iterations = 0
    while num_iterations < max_iterations:
        # Code checking step
        messages.append({"role": "user", "content": plan_eval_prompt})
        if model == "openai":
            response = await prompt_openai(system_prompt, messages)
            plan_eval_result = response.choices[0].message.content
        elif model == "anthropic":
            response = await prompt_anthropic(system_prompt, messages)
            plan_eval_result = response.content[0].text
        messages.append({"role": "assistant", "content": plan_eval_result})

        if is_positive(plan_eval_result):
            break
        else:
            messages.append({"role": "user", "content": plan_redo_prompt})
            if model == "openai":
                response = await prompt_openai(system_prompt, messages)
                plan_redo = response.choices[0].message.content
            elif model == "anthropic":
                response = await prompt_anthropic(system_prompt, messages)
                plan_redo = response.content[0].text
            messages.append({"role": "assistant", "content": plan_redo})
            final_plan = messages[-1]["content"]
        num_iterations += 1

    return messages, final_plan


# Assumes planning response is in the form of a numbered list with "\n" as the delimiter
def parse_planning_response(planning_response):
    pattern = r'^(\d+\.\s.+)$'
    steps = re.findall(pattern, planning_response, re.MULTILINE)

    return steps


def is_positive(string):
    scores = sia.polarity_scores(string)
    if scores['pos'] > scores['neg'] or scores['neu'] > scores['neg']:
        return True
    else:
        return False


# code = await refining_stage(model, messages, planning_steps, code_gen_prompt, code_eval_prompt, code_redo_prompt, max_iterations)
async def refining_stage(model, messages, system_prompt, planning_steps, code_gen_prompt, code_eval_prompt, code_redo_prompt, final_prompt, max_iterations=3):
    for index, planning_step in enumerate(planning_steps):
        # Code generation step
        code_generation_prompt = code_gen_prompt.replace("[[step]]", str(index))
        messages.append({"role": "user", "content": code_generation_prompt})
        if model == "openai":
            response = await prompt_openai(system_prompt, messages)
            new_code = response.choices[0].message.content
        elif model == "anthropic":
            response = await prompt_anthropic(system_prompt, messages)
            new_code = response.content[0].text
        messages.append({"role": "assistant", "content": new_code})

        num_iterations = 0
        while num_iterations < max_iterations:
            # Code checking step
            code_checking_prompt = code_eval_prompt.replace("[[step]]", str(index))
            messages.append({"role": "user", "content": code_checking_prompt})
            if model == "openai":
                response = await prompt_openai(system_prompt, messages)
                code_check_result = response.choices[0].message.content
            elif model == "anthropic":
                response = await prompt_anthropic(system_prompt, messages)
                code_check_result = response.content[0].text
            messages.append({"role": "assistant", "content": code_check_result})

            if is_positive(code_check_result):
                break
            else:
                code_redo_prompt = code_redo_prompt.replace("[[step]]", str(index))
                messages.append({"role": "user", "content": code_redo_prompt})
                if model == "openai":
                    response = await prompt_openai(system_prompt, messages)
                    code_redo = response.choices[0].message.content
                elif model == "anthropic":
                    response = await prompt_anthropic(system_prompt, messages)
                    code_redo = response.content[0].text
                messages.append({"role": "assistant", "content": code_redo})
            num_iterations += 1

    messages.append({"role": "user", "content": final_prompt})
    if model == "openai":
        response = await prompt_openai(system_prompt, messages)
        final_code = response.choices[0].message.content
    elif model == "anthropic":
        response = await prompt_anthropic(system_prompt, messages)
        final_code = response.content[0].text
    messages.append({"role": "assistant", "content": final_code})

    return messages


# async def code_refine_stage(model, problem, code, code_evaluation_prompts, code_regeneration_prompts, max_iterations=3):
#     # Decide how to split code, for now doing it based on lines
#     code_sections = code.split("\n")
#     prev_sections = []
#     for code_section in code_sections:
#         num_iterations = 0
#         curr_code = code_section
#         while num_iterations < max_iterations:
#             # Code evaluation section
#             code_evaluation_prompt = code_evaluation_prompts[1].replace("[[curr_code]]", curr_code).replace("[[problem]]", problem).replace("[[prev_code]]", "\n".join(prev_sections))
#             if model == "openai":
#                 response = await prompt_openai(code_evaluation_prompts[1], code_evaluation_prompt)
#                 code_evaluation_result = response.choices[0].message.content
#             elif model == "anthropic":
#                 response = await prompt_anthropic(code_evaluation_prompts[1], code_evaluation_prompt)
#                 code_evaluation_result = response.contect
#
#             if is_positive(code_evaluation_result):
#                 break
#
#             code_regeneration_prompt = code_regeneration_prompts[1].replace("[[prev_code]]", "\n".join(prev_sections)).replace("[[problem]]", "\n".join(problem))
#             if model == "openai":
#                 response = await prompt_openai(code_regeneration_prompts[1], code_regeneration_prompt)
#                 new_code = response.choices[0].message.content
#             elif model == "anthropic":
#                 response = await prompt_anthropic(code_regeneration_prompts[1], code_regeneration_prompt)
#                 new_code = response.contect
#
#             curr_code = new_code
#             num_iterations += 1
#         prev_sections.append(curr_code)
#
#     return "\n".join(prev_sections)


async def self_refine(model, problem, system_prompt, planning_prompt, plan_eval_prompt, plan_redo_prompt, code_gen_prompt, code_eval_prompt, code_redo_prompt, final_prompt, max_iterations=3):
    messages = [{"role": "user", "content": problem}]
    # Implement plan checking prompt
    plan = await planning_stage(model, messages, system_prompt, planning_prompt)
    messages[-1] = {"role": "assistant", "content": messages[-1]["content"] + "\n" + plan}
    print(plan)
    print(messages)
    messages, final_plan = await planning_update(model, messages, system_prompt, plan_eval_prompt, plan_redo_prompt)
    planning_steps = parse_planning_response(final_plan)
    all_messages = await refining_stage(model, messages, system_prompt, planning_steps, code_gen_prompt, code_eval_prompt, code_redo_prompt, final_prompt, max_iterations)
    print(all_messages)
    # Either save or evaluate code from here


# async def ablation_self_refine(model, problem, planning_prompts, full_code_generation_prompts, code_evaluation_prompts, code_regeneration_prompts, max_iterations=3):
#     plan = await planning_stage(model, planning_prompts, problem)
#     initial_code = await full_code_generation(model, plan, problem, full_code_generation_prompts)
#     code = await code_refine_stage(model, problem, initial_code, code_evaluation_prompts, code_regeneration_prompts, max_iterations)


if __name__ == "__main__":
    model = "openai"
    asyncio.run(self_refine(model, problem, main_system_prompt, main_planning_prompt, main_plan_eval_prompt, main_plan_redo_prompt, main_code_gen_prompt, main_code_eval_prompt, main_code_redo_prompt, main_final_prompt))