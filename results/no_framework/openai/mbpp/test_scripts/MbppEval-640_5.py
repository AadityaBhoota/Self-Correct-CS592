import re

def remove_parenthesis(items):
    result = []
    for item in items:
        result.append(re.sub(r'\([^)]*\)', '', item).strip())
    return tuple(result)

# Test cases




def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)