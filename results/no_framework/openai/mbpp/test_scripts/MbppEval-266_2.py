def lateralsurface_cube(l):
    return 4 * l * l

# Testing the function




def check(candidate):
    assert lateralsurface_cube(5)==100
    assert lateralsurface_cube(9)==324
    assert lateralsurface_cube(10)==400

check(lateralsurface_cube)