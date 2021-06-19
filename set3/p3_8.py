def composite_result(f, g, x):
    return f(g(x))

def composite(f, g):
    def composite_func(x):
        return f(g(x))
    return composite_func