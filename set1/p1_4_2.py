#f(x) = 4x^3 + 3x^2 + 2.5x + 27

poly = [27,2.5,3,4]
const = 3

#integral = x^4 + x^3 + 1.25x^2 + 27x + 3
integral = [const]

for index, number in enumerate(poly):
    integral_value = number/(index+1)
    integral.append(integral_value)

out = integral