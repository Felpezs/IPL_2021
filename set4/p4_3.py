def greatest_common_divisor(value1: int, value2: int):
    """Calcula o maior divisor comum de dois valores"""

    value1 = abs(value1)
    value2 = abs(value2)

    if value1 < value2:
        value1, value2 = value2, value1
    
    remainder = value1 % value2

    if remainder == 0:
        return value2
    
    return greatest_common_divisor(value2, remainder)

class Rational():
    """Classe que representa os números racionais como frações"""

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        if isinstance(other, Rational):
            common_denominator = greatest_common_divisor(self.denominator, other.denominator)
            
            mmc = int(self.denominator * other.denominator/common_denominator)

            new_numerator = self.numerator * int(mmc / self.denominator) + other.numerator * int(mmc / other.denominator)
            
            rational_number = Rational(new_numerator, mmc)

            return rational_number.reduce()
        
        elif isinstance(other, int):
            new_numerator = self.numerator + self.denominator * other

            return Rational(new_numerator, self.denominator)
        
        elif isinstance(other, float):
            return self.to_float() + other

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        
        elif isinstance(other, int):
            return Rational(self.numerator * other, self.denominator)
        
        elif isinstance(other, float):
            return self.to_float() * other

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return self * other.reciprocal()
        
        elif isinstance(other, int):
            return Rational(self.numerator, self.denominator * other)
        
        elif isinstance(other, float):
            return self.to_float() / other

    def __sub__(self, other):
        if isinstance(other, Rational):
            common_denominator = greatest_common_divisor(self.denominator, other.denominator)
            
            mmc = int(self.denominator * other.denominator/common_denominator)
            
            new_numerator = self.numerator * int(mmc / self.denominator) - other.numerator * int(mmc / other.denominator)

            rational_number = Rational(new_numerator, mmc)

            return rational_number.reduce()
        
        elif isinstance(other, int):
            new_numerator = self.numerator - other * self.denominator

            return Rational(new_numerator, self.denominator)
        
        elif isinstance(other, float):
            return self.to_float() - other
        
    def get_numerator(self):
        """Retorna o numerador de uma fração"""

        return self.numerator
    
    def get_denominator(self):
        """Retorna o denominador de uma fração"""

        return self.denominator
    
    def to_float(self):
        """Retorna a fração em float"""
        return self.numerator / self.denominator
    
    def reciprocal(self):
        """Retorna um objeto Rational recíproco"""
        return Rational(self.denominator, self.numerator)
    
    def reduce(self):
        """Retorna o menor objeto Rational equivalente"""

        gcm = greatest_common_divisor(self.denominator, self.numerator)

        self.numerator = self.numerator // gcm
        self.denominator = self.denominator // gcm

        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1
            
        return Rational(self.numerator, self.denominator)