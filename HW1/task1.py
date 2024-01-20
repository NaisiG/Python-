"""
a = 4
b = 3
c = 5
"""
# Введите ваше решение ниже
def check_triangle(a, b, c):
    if (a!=0) and (b!=0) and (c!=0) and (a+b>c) and (c+b>a) and (a+c>b):     
        if (a==b) or (a==c) or (b==c):
            if (a==b) and (b==c): 
                return "Треугольник равносторонний"
            return "Треугольник равнобедренный"
        else:
            return "Треугольник разносторонний"     
def check_triangle_2(a, b, c):
    if (a!=0) and (b!=0) and (c!=0) and (a+b>c) and (c+b>a) and (a+c>b): 
        return True
    else: 
        return False

a,b,c = int(input()), int(input()),int(input())
  
if check_triangle_2(a, b, c) == True:
    print("Треугольник существует")
    print(check_triangle(a,b,c))
else:
    print("Треугольник не существует")
    


"""
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")
"""

