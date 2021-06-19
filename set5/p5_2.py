class Matrix():
    """Classe para representar matrizes"""

    def __init__(self, array_list):
        self.matrix_list = array_list
    
    def __add__(self, other):
        if isinstance(other, Matrix):
            if other.size() == self.size():
                new_matrix = []
                for lst_self, lst_other in zip(self.matrix_list, other.matrix_list):
                    #Para cada elemento de cada lista, efetua-se a soma dos elementos. O resultado é uma lista adicionada em na lista new_matrix
                    new_matrix.append([element_self + element_other for element_self, element_other in zip(lst_self,lst_other)])
                return Matrix(new_matrix)

        elif isinstance(other, int) or isinstance(other, float):
            aux_matrix = []
            for lst_self in self.matrix_list:
                aux_matrix.append([number + other for number in lst_self])
            
            return Matrix(aux_matrix)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if other.size() == self.size():
                new_matrix = []
                for lst_self, lst_other in zip(self.matrix_list, other.matrix_list):
                    #Para cada elemento de cada lista, efetua-se a subtração dos elementos. O resultado é uma lista adicionada em na lista new_matrix
                    new_matrix.append([element_self - element_other for element_self, element_other in zip(lst_self,lst_other)])
                return Matrix(new_matrix)

        elif isinstance(other, int) or isinstance(other, float):
            aux_matrix = []
            for lst_self in self.matrix_list:
                aux_matrix.append([number - other for number in lst_self])
            
            return Matrix(aux_matrix)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            #Se colunas de self forem iguais as linhas de other
            if self.size()[1] == other.size()[0]:
                self_rows = self.size()[0]
                other_cols = other.size()[1]

                new_matrix = []

                for row in range(self_rows):
                    new_matrix.append([])
                    aux_list = []
                    for col in range(other_cols):
                        aux_list = (i * j for i, j in zip(self.row(row), other.col(col)))

                        new_matrix[row].append(sum(aux_list))

                return Matrix(new_matrix)

        elif isinstance(other, int) or isinstance(other, float):
            aux_matrix = []
            for lst_self in self.matrix_list:
                aux_matrix.append([number * other for number in lst_self])
            
            return Matrix(aux_matrix)

    def __str__(self):
        return f'{self.matrix_list}'

    def size(self):
        """Retorna o número de linhas e o número de colunas"""
        return (len(self.matrix_list), len(self.matrix_list[0]))

    def get(self, r, c):
        """Retorna o número da linha(r) e coluna(c)"""

        return self.matrix_list[r][c]
    
    def set(self, r, c, val):
        """Define um novo valor(val) na linha(r) e coluna(c) desejada"""

        self.matrix_list[r][c] = val
    
    def row(self, n):
        """Retorna os elementos da linha(n)"""

        return self.matrix_list[n]
    
    def col(self, c):
        """Retorna os elementos da coluna(c)"""
        
        return [lst[c] for lst in self.matrix_list]
    
    def transpose(self):
        """Retorna a matriz transposta"""

        mat_transpose = []
        rows, cols = self.size()
        for j in range(cols):
            mat_transpose.append([self.get(i, j) for i in range(rows)])

        return Matrix(mat_transpose)