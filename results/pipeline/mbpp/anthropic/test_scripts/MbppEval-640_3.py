import re

def remove_parenthesis(items):
    output = []
    for item in items:
        modified = re.sub(r'\(.*?\)', '', item)
        output.append(modified)
    return output

def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")

check(remove_parenthesis)