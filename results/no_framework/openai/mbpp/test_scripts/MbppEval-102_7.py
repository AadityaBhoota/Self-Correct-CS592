def snake_to_camel(word):
    words = word.split('_')
    camel_case = words[0].capitalize() + ''.join(w.capitalize() for w in words[1:])
    return camel_case

# Test cases




def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)