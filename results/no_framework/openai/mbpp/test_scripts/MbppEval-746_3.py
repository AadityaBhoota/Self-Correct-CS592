def sector_area(r, a):
    if a > 360:
        return None
    else:
        return (math.pi * r**2 * a) / 360

def check(candidate):
    assert sector_area(4,45)==6.283185307179586
    assert sector_area(9,45)==31.808625617596654
    assert sector_area(9,361)==None

check(sector_area)