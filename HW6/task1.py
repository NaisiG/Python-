"""Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.

Пример использования На входе:


date_to_prove = 15.4.2023
На выходе:


True
На входе:


date_to_prove = 31.6.2022
На выходе:


False"""

from datetime import datetime

def isValidDate(date_to_prove):
    try:
        datetime.strptime(date_to_prove,'%d.%m.%Y')
        return True
    except ValueError:
        return False

date_to_prove = "15.4.2023"
if isValidDate(date_to_prove):
    print('True')
else:
    print('False')


