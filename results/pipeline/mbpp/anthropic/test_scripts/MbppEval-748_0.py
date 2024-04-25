import re

def capital_words_spaces(str1):
    capital_words = re.findall(r'[A-Z][a-z]*', str1)
    return ' '.join(capital_words)

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)