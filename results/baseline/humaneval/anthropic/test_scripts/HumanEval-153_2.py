def Strongest_Extension(class_name, extensions):
    """
    Returns the strongest extension for the given class name.

    Args:
        class_name (str): The name of the class.
        extensions (list): A list of extensions to be used to load additional classes.

    Returns:
        str: The class name and the strongest extension in the format "ClassName.StrongestExtensionName".
    """
    strongest_extension = None
    strongest_strength = float('-inf')

    for ext in extensions:
        uppercase_count = sum(1 for char in ext if char.isupper())
        lowercase_count = sum(1 for char in ext if char.islower())
        strength = uppercase_count - lowercase_count
        if strength > strongest_strength:
            strongest_extension = ext
            strongest_strength = strength
        elif strength == strongest_strength and ext < strongest_extension:
            strongest_extension = ext
            strongest_strength = strength

    return f"{class_name}.{strongest_extension}"

def check(candidate):

    # Check some simple cases
    assert candidate('Watashi', ['tEN', 'niNE', 'eIGHt8OKe']) == 'Watashi.eIGHt8OKe'
    assert candidate('Boku123', ['nani', 'NazeDa', 'YEs.WeCaNe', '32145tggg']) == 'Boku123.YEs.WeCaNe'
    assert candidate('__YESIMHERE', ['t', 'eMptY', 'nothing', 'zeR00', 'NuLl__', '123NoooneB321']) == '__YESIMHERE.NuLl__'
    assert candidate('K', ['Ta', 'TAR', 't234An', 'cosSo']) == 'K.TAR'
    assert candidate('__HAHA', ['Tab', '123', '781345', '-_-']) == '__HAHA.123'
    assert candidate('YameRore', ['HhAas', 'okIWILL123', 'WorkOut', 'Fails', '-_-']) == 'YameRore.okIWILL123'
    assert candidate('finNNalLLly', ['Die', 'NowW', 'Wow', 'WoW']) == 'finNNalLLly.WoW'

    # Check some edge cases that are easy to work out by hand.
    assert candidate('_', ['Bb', '91245']) == '_.Bb'
    assert candidate('Sp', ['671235', 'Bb']) == 'Sp.671235'
    

check(Strongest_Extension)