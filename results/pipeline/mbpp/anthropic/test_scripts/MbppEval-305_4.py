import re

def start_withp(words):
    word_list = words.split()
    p_words = [word for word in word_list if re.match(r'^p', word, re.IGNORECASE)]
    return tuple(p_words[:2])

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)