"""Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

Пример

На входе:

lst = [1, 1, 2, 2, 3, 3]
На выходе:

[1, 2, 3]"""

from collections import Counter

def duplicates(lst):
    counter = Counter(lst)
    return [k for k, v in counter.items() if v > 1]

if __name__=="__main__":
    lst = [1, 2, 3, 2, 4, 5, 4]
    res = duplicates(lst)
    print(res)
    
"""
Решение с сайта:
duplicates = set()

for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)
"""