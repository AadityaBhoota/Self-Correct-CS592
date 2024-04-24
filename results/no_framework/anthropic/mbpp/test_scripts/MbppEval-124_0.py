import cmath

def angle_complex(a, b):
    """
    Write a function to get the angle of a complex number.

    Examples:
    angle_complex(0, 1j) == 1.5707963267948966
    angle_complex(2, 1j) == 0.4636476090008061
    angle_complex(0, 2j) == 1.5707963267948966
    """
    z = complex(a, b)
    return cmath.phase(z)

def check(candidate):
    assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
    assert math.isclose(angle_complex(2,1j), 0.4636476090008061, rel_tol=0.001)
    assert math.isclose(angle_complex(0,2j), 1.5707963267948966, rel_tol=0.001)

check(angle_complex)