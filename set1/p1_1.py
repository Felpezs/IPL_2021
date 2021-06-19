#float de 0 a 1 (taxa de juros)
interest_rate = 0.14
t = 1
m = 1

while(m < 2):
    t+=1
    m = ( 1+interest_rate )**t

#anos para dobrar o dinheiro
out = t