import math

class Triangle:
    def __init__(self, A, B, C):
        self._A = A
        self._B = B
        self._C = C

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            self._A = value
        else:
            raise TypeError('Точка должна быть кортежем с двумя координатами')

    @property
    def B(self):
        return self._B

    @B.setter
    def B(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            self._B = value
        else:
            raise TypeError('Точка должна быть кортежем с двумя координатами')

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            self._C = value
        else:
            raise TypeError('Точка должна быть кортежем с двумя координатами')

    @property
    def AB(self):
         return self.distance(self.A, self.B)
    
    @property
    def BC(self):
         return self.distance(self.B, self.C)
    
    @property
    def AC(self):
         return self.distance(self.A, self.B)
    
    @property
    def AH(self):
        return round((abs((self.B[1] - self.C[1]) * self.A[0] + (self.C[0] - self.B[0]) * self.A[1] + (self.B[0] * self.C[1] - self.C[0] * self.B[1])) / \
                math.sqrt((self.B[1] - self.C[1])**2 + (self.C[0] - self.B[0])**2)), 3)
    
    @property
    def BH(self):
        return round((abs((self.A[1] - self.C[1]) * self.B[0] + (self.C[0] - self.A[0]) * self.B[1] + (self.A[0] * self.C[1] - self.C[0] * self.A[1])) / \
                math.sqrt((self.A[1] - self.C[1])**2 + (self.C[0] - self.A[0])**2)), 3)

    @property
    def CH(self):
        return round((abs((self.A[1] - self.B[1]) * self.C[0] + (self.B[0] - self.A[0]) * self.C[1] + (self.A[0] * self.B[1] - self.B[0] * self.A[1])) / \
                math.sqrt((self.A[1] - self.B[1])**2 + (self.B[0] - self.A[0])**2)), 3)

    @property
    def AM(self):
            return (self.A[0] + self.C[0]) / 2, (self.B[1] + self.C[1]) / 2
    
    @property
    def BM(self):
            return (self.A[0] + self.C[0]) / 2, (self.A[1] + self.C[1]) / 2
    
    @property
    def CM(self):
            return (self.B[0] + self.A[0]) / 2, (self.B[1] + self.A[1]) / 2


    def distance(self, A, B):
        return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

    def perimeter(self):
        return round(self.distance(self._A, self._B) + self.distance(self._B, self._C) + self.distance(self._C, self._A), 3)
    
    def heights(self):
        return (self.AH, self.BH, self.CH)

    def medians(self):
        self.am = round(math.sqrt((self.AM[0] - self.A[0])**2 + (self.AM[1] - self.A[1])**2), 3)
        self.bm = round(math.sqrt((self.BM[0] - self.B[0])**2 + (self.BM[1] - self.B[1])**2), 3)
        self.cm = round(math.sqrt((self.CM[0] - self.C[0])**2 + (self.CM[1] - self.C[1])**2), 3)
        self.medians = (self.am, self.bm, self.cm)
        return self.medians
    
    def area(self):
        p = self.perimeter() / 2
        return round(math.sqrt(p * (p - self.distance(self._A, self._B)) * (p - self.distance(self._B, self._C)) * (p - self.distance(self._C, self._A))), 3)

    def isosceles(self):
        return self.distance(self._A, self._B) == self.distance(self._B, self._C) or \
               self.distance(self._B, self._C) == self.distance(self._C, self._A) or \
               self.distance(self._C, self._A) == self.distance(self._A, self._B)
    
    def equilateral(self):
        if self.AB == self.BC == self.AC: return True
        else: return False

    def __str__(self):
        return f'Треугольник {self._A}, {self._B}, {self._C}'

    def __gt__(self, other):
        return self.area() > other.area()

class ImmutableTriangle(Triangle):
    def __init__(self, A, B, C):
        super().__init__(A, B, C)
        self._initialized = True

    def __setattr__(self, name, value):
        if hasattr(self, '_initialized'):
            raise AttributeError('нельзя изменить')
        super().__setattr__(name, value)

class RightTriangle(Triangle):
    def __init__(self, A, B, C):
        super().__init__(A, B, C)
        if not self._is_right():
            raise ValueError('не прямой треугольник')

    def _is_right(self):
        A = self.distance(self._A, self._B)
        B = self.distance(self._B, self._C)
        C = self.distance(self._C, self._A)
        sides = [A, B, C]
        return round(sides[2]**2, 2) == round(round(sides[0]**2, 2) + round(sides[1]**2, 2), 2)
    

################################ проверка примером из лабы
t2 = Triangle((1., 0.), (1., 1.), (0., 1.))
t = Triangle((1., 0.), (0., 0.), (0., 1.))
print(t)
print(t2)
print(t.medians()) # (1.118, 1.118, 0.707)
print(t.heights()) # (1.0, 1.0, 0.707)
print(t.equilateral()) # False
print(t.isosceles()) # True
print(t.perimeter()) # 3.414
print(t.area()) # 0.5
if t == t2:
        print('Треугольники равны') # Выполняется это условие
else:
        print('Треугольники не равны')      
t = Triangle((1., 0.), (2., 4.), (0., 1.))
print(t.isosceles()) # False
print(t.A) # (1., 0.)
t.B = (0., 0.)
# t.B = [] # Эта строка выводит TypeError
print(t) # Треугольник (1.0, 0.0), (0.0, 0.0), (0.0, 1.0)
print(t.isosceles()) # True
t2 = Triangle((2., 0.), (0., 0.), (0., 1.))
if t > t2:
        print('Первый треугольник больше')
else:
        print('Второй треугольник больше или равен') #Выполняется это условие
t3 = ImmutableTriangle((1., 0.), (2., 0.), (0., 1.))
# t2.A = (2., 0.) # Эта строка выводит AttributeError
t4 = RightTriangle((1., 0.), (0., 0.), (0., 1.))
# t4 = RightTriangle((1., 0.), (0.25, 0.25), (0., 1.)) # ValueError
t4.A = (2.,0.)
# t3.A = (2.,0.5) # Эта строка выводит ValueError (не прямоугольный)
t.A = tuple(input("Введите значения первой точки через запятую: ").split(','))
t.A = tuple(map(lambda i: float(i), t.A))