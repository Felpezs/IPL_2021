numbers = [5, 6, 7, 12, 29]
prod = 1
out = None

if(len(numbers) != 0):
    for n in numbers:
        prod *= n
        print(prod)
    out = prod**(1/len(numbers))
    print(out)