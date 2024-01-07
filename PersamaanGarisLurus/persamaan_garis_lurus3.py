from persamaan_garis_lurus2 import Point
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
        self._c = abs(c)
        self._tandaC = (1 if c > 0 else -1)
    
    
    @classmethod
    def gunakanDuaTitik(cls, A, B):
        try:    
            m = (B.y - A.y) / (B.x - A.x)
        except ZeroDivisionError:
            m = 0
        
        try:
            c = (-(B.y - A.y) * A.x) / (B.x - A.x) + A.y
            print(c)
        except ZeroDivisionError:
            c = 0

        try:
            m = int(m)
            c = int(c) 
        except ValueError:
            pass 
        return(cls(m, c))
    
    
    @classmethod
    def gunakanGradienTitik(cls, m, point):
        c = point.y - (m * point.x)
        return cls(m, c)
    
    
    def persamaanImplisit(self, bentuk = 3):
        return self.convertToEquation(self._m, self._c * self._tandaC, returnType = bentuk + 1)
        
        
    @staticmethod
    def convertToKoefisien(num, var):
        koef = ''
        opt = '+'
        
        if num == 1:
            pass
        elif num == -1:
            opt = '-'
        elif num == 0:
            pass
        else:
            koef = num
            opt = '+' if num > 0 else '-'
            
        if var != 'x':
            try:
                koef = abs(int(koef))
            except ValueError:
                pass 
    
        if num != 0:
            if var == 'x': 
                variable = f'{koef}{var}'
            else:
                variable = f'{koef}{var}'
        else:
            variable = ''
        return {'koefisien' : koef, 'operator' : opt, 'var' : variable}
    
    
    def titikPotongSbX(self):
        x = -1 * self._tandaC * self._c / self._m
        try:
            x = int(x)
        except ValueError:
            pass 
        return (x, 0)
    
    
    def titikPotongSbY(self): 
        y = self._tandaC * self._c
        try:
            y = int(y)
        except ValueError:
            pass
        
        return (0, y)
    
    
    @staticmethod
    def convertToEquation(x, z, y = 1, returnType = 1 ):
        X, Y, Z = map(lambda x,y: PersamaanGarisLurus.convertToKoefisien(x,y), [x, -y, z], ['x', 'y', ''])
        X2, Y2, Z2 = map(lambda x,y: PersamaanGarisLurus.convertToKoefisien(x,y), [-x, y, -z], ['x', 'y', ''])
        
        type2 = f'{X["var"]} {Y["operator"]} {Y["var"]} {Z["operator"]} {Z["var"]} = 0'        
        type3 = f'{X2["var"]} {Y2["operator"]} {Y2["var"]} {Z2["operator"]} {Z2["var"]} = 0'
        match returnType:
            case 1:
                return f'{Y["var"]} = {X["var"]} {Z["operator"]} {Z["var"]}'
            case 2:
                return type2
            case 3:        
                return type3
            case 4:
                return f'{type2}\n{type3}'
            
    def __str__(self):
        return self.convertToEquation(self._m, self._tandaC * self._c)
    
# pers = PersamaanGarisLurus(2, -12)
# print(pers.titikPotongSbX())
pers2 = PersamaanGarisLurus(11, -120)
print(pers2.persamaanImplisit())

pers = PersamaanGarisLurus(2, -12)
print(pers.titikPotongSbY())