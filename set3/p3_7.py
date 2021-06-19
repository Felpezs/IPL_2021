"""
Solução iterativa
def hailstone_sequence(a_0: int):
    out = [a_0]
    while(1 not in out):
        if(out[-1] % 2 == 0):
            value = out[-1]/2
            out.append(value)
        else:
            value = 3 * out[-1] + 1
            out.append(value)
    
    return out
"""

def hailstone_sequence(a_0: int):
    out = [a_0]

    if(a_0 == 1):
        return [1]
    else:
        if(a_0 % 2 == 0):
            return out + hailstone_sequence(a_0/2)
        else:
            return out + hailstone_sequence(3 * a_0 + 1)

print(hailstone_sequence(800))