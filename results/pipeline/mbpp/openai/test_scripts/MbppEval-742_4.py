import math

def area_tetrahedron(side):
    height = math.sqrt(2/3) * side
    face_area = (side ** 2) * math.sqrt(3) / 4
    total_area = 3 * face_area
    return total_area

def check(candidate):
    assert area_tetrahedron(3)==15.588457268119894
    assert area_tetrahedron(20)==692.8203230275509
    assert area_tetrahedron(10)==173.20508075688772

check(area_tetrahedron)