def approx_derivative(f, x: int, delta =  1e-6):
    return (f(x + delta) - f(x - delta))/(2 * delta)

def approx_derivative_2(f, delta =  1e-6):
    def new_func(x):
        return (f(x + delta) - f(x - delta))/(2 * delta)
    return new_func

def approx_integral(f, lo, hi, num_regions):
    area = 0
    h = (hi - lo)/num_regions
    x = lo + h
    for i in range(num_regions - 1):
        area += f(x)
        x += h

    total_area = h * ((f(hi) + f(lo))/2 + area) 

    return total_area