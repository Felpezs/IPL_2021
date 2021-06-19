size = "medium"
toppings = ["calabresa","tomate","queijo","bacon"]

cost = 16 

for index, item in enumerate(toppings):
    cost += (12 + index + len(item))/100 * cost

if("anchovas" in toppings):
    cost += cost * 10/100

if("bacon" in toppings):
    cost += cost * 10/100

out = cost
