import math
class Triangle:

    def __init__(self, a, b, c):
        self.correctly = 1
        for i in range(0, 2):
             if type(a[i]) != float:
                  self.correctly = 0
                  break
        for i in range(0, 2):
             if type(b[i]) != float:
                  self.correctly = 0
                  break
        for i in range(0, 2):
             if type(c[i]) != float:
                  self.correctly = 0
                  break
        if self.correctly == 0: print("Неверные данные")
        else:
            self.a = a
            self.b = b
            self.c = c
            self.ab = ((self.b[0]-self.a[0])**2+(self.b[1]-self.a[1])**2)**(1/2)
            self.ac = ((self.c[0]-self.a[0])**2+(self.c[1]-self.a[1])**2)**(1/2)
            self.bc = ((self.c[0]-self.b[0])**2+(self.c[1]-self.b[1])**2)**(1/2)

    def medians(self):
        self.AM = [(self.b[0]+self.c[0])/2, (self.b[1]+self.c[1])/2] 
        self.BM = [(self.a[0]+self.c[0])/2, (self.a[1]+self.c[1])/2] 
        self.CM = [(self.b[0]+self.a[0])/2, (self.b[1]+self.a[1])/2] 
        self.am = math.sqrt((self.AM[0] - self.a[0])**2 + (self.AM[1] - self.a[1])**2) 
        self.bm = math.sqrt((self.BM[0] - self.b[0])**2 + (self.BM[1] - self.b[1])**2) 
        self.cm = math.sqrt((self.CM[0] - self.c[0])**2 + (self.CM[1] - self.c[1])**2)
        self.medians = (self.am, self.bm, self.cm)
        return self.medians
    
    def heights(self):
        self.ah = (abs((self.b[1]-self.c[1])*self.a[0]+(self.c[0]-self.b[0])*self.a[1]+(self.b[0]*self.c[1]-self.c[0]*self.b[1]))/math.sqrt((self.b[1]-self.c[1])**2+(self.c[0]-self.b[0])**2))
        self.bh = (abs((self.a[1]-self.c[1])*self.b[0]+(self.c[0]-self.a[0])*self.b[1]+(self.a[0]*self.c[1]-self.c[0]*self.a[1]))/math.sqrt((self.a[1]-self.c[1])**2+(self.c[0]-self.a[0])**2))
        self.ch = (abs((self.a[1]-self.b[1])*self.c[0]+(self.b[0]-self.a[0])*self.c[1]+(self.a[0]*self.b[1]-self.b[0]*self.a[1]))/math.sqrt((self.a[1]-self.b[1])**2+(self.b[0]-self.a[0])**2))
        self.heights = (self.ah, self.bh, self.ch)
        return self.heights
    
    def __eq__(self, other):
        return ((self.ab == other.ab) and (self.bc == other.bc) and (self.ac == other.ac))
    
    def isosceles(self):
        if self.ab == self.bc or self.ab == self.ac or self.bc == self.ac: return True
        else: return False
     
    def equilateral(self):
        if self.ab == self.bc == self.ac: return True
        else: return False

    def area(self):
        return self.ab*self.ch/2
    
    def perimetr(self):
        return self.ab + self.ac + self.bc
    
    def __repr__(self):
         self.trr = str("Треугольник" + str(self.a) + str(self.b) + str(self.c))
         return self.trr

t2 = Triangle((1., 0.), (1., 1.), (0., 1.))
t = Triangle((1., 0.), (0., 0.), (0., 1.))
print(t.medians()) # (1.118, 1.118, 0.707)
print(t.heights()) # (1.0, 1.0, 0.707)
print(t.equilateral()) # False
print(t.isosceles()) # True
print(t.perimetr()) # 3.414
print(t.area()) # 0.5
if t == t2:
        print('Треугольники равны') #Выполняется это условие
else:
        print('Треугольники   не равны')
print(t) # Треугольник (1.0, 0.0), (0.0, 0.0), (0.0, 1.0)