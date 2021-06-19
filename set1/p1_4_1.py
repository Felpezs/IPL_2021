#f(x) = 4x^3 + 3x^2 + 2x + 27

poly = [27,2,3,4]
derivative = []

for index, number in enumerate(poly):
    derivative.append(number * index)

derivative.remove(0)
out = derivative