def decode_cyclic(s: str):
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
  
    # reverse cyclic shift for each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:2]) if len(group) == 3 else group for group in groups]
  
    return "".join(groups)



METADATA = {}


def check(candidate):
    from random import randint, choice
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_cyclic(str)
        assert candidate(encoded_str) == str


check(decode_cyclic)