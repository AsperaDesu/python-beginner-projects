from fractions import Fraction
class PersamaanGarisLurus:
    def __init__(self, m, c):
        self.m = Fraction(m)
        self.c = Fraction(c)
        
    @property
    def m(self):
        return self._m
    
    @m.setter
    def m(self, m):
        self._m = m
        
    @property
    def c(self):
        return self._c
    
    @c.setter
    def c(self, c):
        self._c = c
        self._tandaC = (1 if c > 0 else -1)
        
    def __str__(self):
        operator = '-' if self._tandaC < 0 else '+'
        m = f'{"-" if self._m <= 0 else ""}{"" if (value := abs(self._m)) == 1 else value}'
        m_str = f'y = {m}x {operator} {abs(self._c)}'
        
        return m_str

pers1 = PersamaanGarisLurus(-0.25, 3.5) 
pers2 = PersamaanGarisLurus(-5, 7.5)
pers3 = PersamaanGarisLurus(3, -6)
pers4 = PersamaanGarisLurus(1, -8)
pers5 = PersamaanGarisLurus(-1, 9)

print(pers1)
print(pers2)
print(pers3)
print(pers4)
print(pers5)
