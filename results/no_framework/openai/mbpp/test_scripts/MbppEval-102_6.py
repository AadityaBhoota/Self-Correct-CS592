def snake_to_camel(word):
    return ''.join([w.capitalize() for w in word.split('_')])

# Test cases




def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)