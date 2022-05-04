from math import pi, atan

class ComplexNumber:
    """Perform calculations on complex numbers in the form a+bi"""
    def __init__(self, a=0, b=0): self.a, self.b = a, b
    def __str__(self): 
        if self.a == 0:
            if self.b == 0: return "0"
            elif self.b == 1: return "i"
            elif self.b == -1: return "-i"
            else: return f"{self.b}i"
        else:
            if self.b == 0: return f"{self.a}"
            elif self.b == 1: return f"{self.a}+i"
            elif self.b == -1: return f"{self.a}-i"
            elif self.b > 0: return f"{self.a}+{self.b}i"
            elif self.b < 0: return f"{self.a}{self.b}i"
    def __add__(self, other): return ComplexNumber(self.a+other.a, self.b+other.b)
    def __sub__(self, other): return ComplexNumber(self.a-other.a, self.b-other.b)
    def __mul__(self, other): return ComplexNumber(self.a*other.a-self.b*other.b, self.a*other.b+self.b*other.a)
    def __truediv__(self, other): return ComplexNumber((self.a*other.conjugate().a-self.b*other.conjugate().b)/(other*other.conjugate()).real(), (self.a*other.conjugate().b+self.b*other.conjugate().a)/(other*other.conjugate()).real())
    def __pow__(self, val):
        assert type(val) == int, "Cannot raise complex number to a decimal (yet)"
        num = self
        if val == 0: return ComplexNumber(1)
        elif val > 0:
            for _ in range(val-1): num = self.__mul__(num)
            return num
        elif val < 0:
            for _ in range(-val-1): num = self.__mul__(num)
            return ComplexNumber(1).__truediv__(num)
    def __abs__(self): return (self.a**2+self.b**2)**0.5
    def __neg__(self): return ComplexNumber(-self.a, -self.b)
    def __pos__(self): return self
    def real(self) -> int: return self.a
    def imag(self) -> int: return self.b
    def conjugate(self): return ComplexNumber(self.a, -self.b)
    def modulus(self) -> float: return self.__abs__()
    def arg(self) -> float:
        """Returns the argument of the complex number from -pi to pi radians"""
        if self.a < 0 and self.b > 0: return pi+atan(self.b/self.a)
        elif self.a < 0 and self.b < 0: return -pi+atan(self.b/self.a)
        return atan(self.b/self.a)
    def convert_modulus_argument(self) -> str: 
        """Returns the complex number in modulus-argument form"""
        return f"{self.modulus()}(cos({self.argument()})+isin({self.argument()}))"

