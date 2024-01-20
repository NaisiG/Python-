#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

frac1 = "1/2"
 frac2 = "1/3"

# Введите ваше решение ниже
numer1, gen1 = frac1.split("/")
a = int(numer1)
b = int(gen1)
numer2, gen2 = frac2.split("/")
c = int(numer2)
d = int(gen2)

from fractions import Fraction

num1 = Fraction(a, b)
num2 = Fraction(c, d)
result = num1 + num2
result2 = num1 * num2

print("Сумма дробей:", result)
print("Произведение дробей:", result2)
print("Сумма дробей:", result)
print("Произведение дробей:", result2)