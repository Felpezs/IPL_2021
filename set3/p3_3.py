def dictmap(d, f):
    for keys in d:
        d[keys] = f(d[keys])