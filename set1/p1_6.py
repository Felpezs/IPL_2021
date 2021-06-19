#células de grid em cada eixo
p_d = 131

#quantidade total de quadrados (index iniciando em 0)
num_squares = int(p_d/2)

#quantidade de quadrados dentro do círculo
true_squares = []
#lista com coordenadas de x
x = []

#lista com coordenadas de y
y = []

#lista com coordenadas de x e y
coords = []

for i in range(-num_squares, num_squares + 1):
    x.append(i)
    y.append(i)

for i in x:
    for j in y:
        coords_aux = [x[i],y[j]]
        coords.append(coords_aux)

#para cada coordenada, foi feita a verificação se ela está dentro ou não do círculo (centro dos quadrados)
for item in coords:
    calc_aux = (item[0]**2 + item[1]**2)**(1/2)

    if(calc_aux <= p_d/2):
        true_squares.append(item)
    
out = (len(true_squares)/len(coords))*4
