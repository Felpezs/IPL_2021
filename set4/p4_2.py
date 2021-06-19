import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)

class Triangle:

    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
    
    def side_lengths(self):
        """Calcula o comprimento dos lados de um triângulo"""

        ab = self.point_a.euclidean_distance(self.point_b)
        bc = self.point_b.euclidean_distance(self.point_c)
        ca = self.point_c.euclidean_distance(self.point_a)

        return (ab, bc, ca)
    
    def angles(self):
        """Calcula os ângulos de um triângulo"""
        a, b, c = self.side_lengths()

        angle_ab = math.acos((a ** 2 + b ** 2 - c ** 2)/(2 * a * b))
        angle_bc = math.acos((b ** 2 + c ** 2 - a ** 2)/(2 * b * c))
        angle_ca = math.acos((c ** 2 + a ** 2 - b ** 2)/(2 * c * a))
        
        return [angle_ab, angle_bc, angle_ca]

    def side_classification(self):
        """Classifica um triângulo com base nos lados"""

        a, b, c = self.side_lengths()

        if(compare_floats(a, b) and compare_floats(a, c)):
            return 'equilateral'

        elif(compare_floats(a, b) or compare_floats(b, c) or compare_floats(a, c)):
            return 'isosceles'

        return 'scalene'

    def angle_classification(self):
        """Classifica um triângulo por meio do ângulo"""

        angle = max(self.angles())
        
        if compare_floats(angle, math.pi / 2):
            return 'right'
        
        elif angle > math.pi / 2:
            return 'obtuse'
        
        elif compare_floats(angle, math.pi / 3) :
            return 'equiangular'
    
        return 'acute'

    def is_right(self):
        """Verifica se o triângulo é retângulo"""

        return True if self.angle_classification() == 'right' else False 

    def area(self):
        """Calcula a área de um triângulo"""

        semi_perimeter = self.perimeter()/2
        a, b, c = self.side_lengths()

        return (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))**0.5

    def perimeter(self):
        """Calcula o perímetro de um triângulo"""

        ab, bc, ca = self.side_lengths()
        return ab + bc + ca

def compare_floats(value1: float, value2: float):
    """Função que compara 2 floats"""

    return True if abs(value1 - value2) <= 10**-6 else False