def find_solution(a, b, n):
    for x in range(n // a + 1):
        y = (n - a * x) / b
        if y.is_integer() and y >= 0:
            return ('x = ', x, ', y = ', int(y))
    return "No solution"

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)