#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

num = 0

# Введите ваше решение ниже
def int_to_hex(num):
  if num > 0:
    return hex(num)[2:]
  else:
    return ""
result = int_to_hex(num)
print("Шестнадцатеричное представление числа:", result.upper())
print("Проверка результата:", hex(num))