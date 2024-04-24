import re

def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

# Test cases




def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)