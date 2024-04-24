def parabola_directrix(a, b, c): 
    directrix = c - (b**2) / (4*a)
    return int(directrix)


# Test cases




def check(candidate):
    assert parabola_directrix(5,3,2)==-198
    assert parabola_directrix(9,8,4)==-2336
    assert parabola_directrix(2,4,6)==-130

check(parabola_directrix)