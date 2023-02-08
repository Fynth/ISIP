#import math 
#  
# a = [9, 20] 
# b = [13, 5] 
# c = [14, 17] 
# print ("A:",end = " ") 
# for i in range(len(a)): 
#     print(a[i], end = " ") 
#  
# print("") 
# print ("B:",end = " ") 
# for i in range(len(a)): 
#     print(b[i], end = " ") 
#  
# print("") 
# print ("C:",end = " ") 
# for i in range(len(a)): 
#     print(c[i], end = " ") 
#  
# Ma = [(b[0]+c[0])/2, (b[1]+c[1])/2] 
# Mb = [(a[0]+c[0])/2, (a[1]+c[1])/2] 
# Mc = [(b[0]+a[0])/2, (b[1]+a[1])/2] 
#  
#  
# AM = math.sqrt((Ma[0] - a[0])**2 + (Ma[1] - a[1])**2) 
# BM = math.sqrt((Mb[0] - b[0])**2 + (Mb[1] - b[1])**2) 
# CM = math.sqrt((Mc[0] - c[0])**2 + (Mc[1] - c[1])**2) 
#  
# print("") 
# print ("AM:",end = " ") 
# for i in range(len(a)): 
#     print(Ma[i], end = " ") 
#      
# print("") 
# print ("BM:",end = " ") 
# for i in range(len(a)): 
#     print(Mb[i], end = " ") 
#  
# print("") 
# print ("CM:",end = " ") 
# for i in range(len(a)): 
#     print(Mc[i], end = " ") 
#  
# print("") 
# print("") 
# print("AM =", AM) 
# print("BM =", BM) 
# print("CM =", CM) 
#  
# AH = (abs((b[1]-c[1])*a[0]+(c[0]-b[0])*a[1]+(b[0]*c[1]-c[0]*b[1]))/math.sqrt((b[1]-c[1])**2+(c[0]-b[0])**2)) 
# BH = (abs((a[1]-c[1])*b[0]+(c[0]-a[0])*b[1]+(a[0]*c[1]-c[0]*a[1]))/math.sqrt((a[1]-c[1])**2+(c[0]-a[0])**2)) 
# CH = (abs((a[1]-b[1])*c[0]+(b[0]-a[0])*c[1]+(a[0]*b[1]-b[0]*a[1]))/math.sqrt((a[1]-b[1])**2+(b[0]-a[0])**2)) 
#  
#
#
# print("") 
# print("AH =", AH) 
# print("BH =", BH) 
# print("CH =", CH)
#def exist(a, b, c): 
#         if a + b > c and a + c > b and b + c > a: 
#                 return 1 
#         else: return 0 
#  
# def correct(a, b, c): 
#         if a > 0 and b > 0 and c > 0: 
#                 return 1 
#         else: return 0 
#  
# def ravnobed(a, b, c): 
#         if a == b or a == c or b == c: return 1 
#         else: return 0 
#  
# def ravnostor(a, b, c): 
#         if a == b == c: return 1 
#         else: return 0 
#  
# a = int(input("введите сторону А:")) 
# b = int(input("введите сторону В:")) 
# c = int(input("введите сторону С:")) 
# if correct(a, b, c) == 1: 
#         if exist(a, b, c) == 1: 
#                 if ravnobed(a, b, c) == 1: 
#                         if ravnostor(a, b, c) == 1: 
#                                 print("треугольник равносторонний") 
#                         else: 
#                                 print("треугольник равнобедренный") 
#                          
#         else: print("треугольникa с такими значениями не существует") 
# else: print("некорректные данные")
class Triangle:
	def __init__(self, a, b, c):
		AB = ((b[0] - a[0])**2 - (b[1] - a[1])**2)**0.5
		BC = ((c[0] - b[0])**2 - (c[1] - b[1])**2)**0.5
		AC = ((c[0] - a[0])**2 - (c[1] - a[1])**2)**0.5
	
	def medians(self, a, b, c):
		Ma = [(b[0]+c[0])/2, (b[1]+c[1])/2] 
		Mb = [(a[0]+c[0])/2, (a[1]+c[1])/2] 
		Mc = [(b[0]+a[0])/2, (b[1]+a[1])/2] 
		AM = math.sqrt((Ma[0] - a[0])**2 + (Ma[1] - a[1])**2) 
		BM = math.sqrt((Mb[0] - b[0])**2 + (Mb[1] - b[1])**2) 
		CM = math.sqrt((Mc[0] - c[0])**2 + (Mc[1] - c[1])**2) 
		meridians = [AM, BM, CM]
		return meridians
		
	def heights(self, a, b, c):
		
		 AH = (abs((b[1]-c[1])*a[0]+(c[0]-b[0])*a[1]+(b[0]*c[1]-c[0]*b[1]))/math.sqrt((b[1]-c[1])**2+(c[0]-b[0])**2)) 
		 BH = (abs((a[1]-c[1])*b[0]+(c[0]-a[0])*b[1]+(a[0]*c[1]-c[0]*a[1]))/math.sqrt((a[1]-c[1])**2+(c[0]-a[0])**2)) 
		 CH = (abs((a[1]-b[1])*c[0]+(b[0]-a[0])*c[1]+(a[0]*b[1]-b[0]*a[1]))/math.sqrt((a[1]-b[1])**2+(b[0]-a[0])**2)) 
		
	def equilateral:
		
	def isosceles:
		
	def perimetr:
		
	def area: