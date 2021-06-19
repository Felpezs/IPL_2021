class Vector():
    """Classe que representa os vetores"""

    def __init__(self, array_list):
        self.array = array_list
    
    def __str__(self):
        return f'{self.array}'

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.array) == len(other.array):
                new_vector_list = [v1 + v2 for v1, v2 in zip(self.array, other.array)]

                return Vector(new_vector_list)

    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.array) == len(other.array):
                new_vector_list = [v1 - v2 for v1, v2 in zip(self.array, other.array)]

                return Vector(new_vector_list)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.array) == len(other.array):
                new_vector_list = [v1 * v2 for v1, v2 in zip(self.array, other.array)]

                return sum(new_vector_list)
        
        elif isinstance(other, float) or isinstance(other, int):
            new_vector_list = [other * number for number in self.array]
            return Vector(new_vector_list)

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_vector_list = [number/other for number in self.array]
            return Vector(new_vector_list)

    def as_list(self):
        """Retorna uma lista contendo os elementos do vetor"""

        return self.array

    def size(self):
        """Retorna um inteiro contendo os números de elementos do vetor"""
        return len(self.array)

    def magnitude(self):
        """Retorna a magnitude do vetor"""

        vet_mag = 0

        for numbers in self.array:
            vet_mag += numbers**2

        return vet_mag**0.5

    def euclidean_distance(self, other):
        """Retorna a distância euclidiana entre dois vetores"""
        euc_dist = 0

        for v1, v2 in zip(self.array, other.array):
            euc_dist += ((v1 - v2))**2

        return euc_dist**0.5

    def normalized(self):
        """Retorna o vetor unitário"""
        
        vet_mag = self.magnitude()
        unit_vet = []

        for numbers in self.array:
            unit_vet.append(numbers/vet_mag)

        return Vector(unit_vet)

    def cosine_similarity(self, other):
        """Retorna o ângulo entre os vetores"""
        
        cosine = (self * other)/(self.magnitude() * other.magnitude())

        return cosine