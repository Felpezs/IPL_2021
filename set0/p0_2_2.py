a=1
b=2
c=3

if(a != 0):
    x1 = (-b + (b**2 -4*a*c)**0.5)/ 2*a
    x2 = (-b - (b**2 -4*a*c)**0.5)/ 2*a

    out = x1,x2

else:
    out = -c/b
