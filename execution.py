import contextlib
import os
import time
from uuid import uuid4


def execute_code(code_program: str, outfile=None) -> bool:
    """Unsafely(!!!) executes code and returns if successfully ran (asserts are considered fails)
    """
    if outfile:
        with open(outfile, "w") as f:
            with contextlib.redirect_stdout(f):
                try:
                    glob = {}
                    exec(code_program, glob)
                    return True
                except Exception as e:
                    print("Error running code:", e)
                    return False
    else:
        try:
            glob = {}
            exec(code_program, glob)
            return True
        except Exception as e:
            print("Error running code:", e)
            return False
    
def main():
    start_time = time.time()

    # he_dataset = load_humaneval_dataset("./data/HumanEval.jsonl")
    # for entry in he_dataset:
    #     code_solution = entry["prompt"] + entry["canonical_solution"] + entry["test"] + "\n" + f"check({entry['entry_point']})"
    #     execute_code(code_solution)
    
    # mbpp_dataset = load_humaneval_dataset("./data/mbpp.jsonl")
    # for entry in mbpp_dataset:
    #     code_solution =  entry["code"] + "\n" + entry["test_setup_code"] + "\n" + "\n".join(entry["test_list"])
    #     execute_code(code_solution)

    execute_code("assert(False)")

    # it runs pretty quick
    print("Total secs:", time.time() - start_time)

if __name__ == "__main__":
    main()
