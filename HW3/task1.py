"""
На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
Предметы не должны дублироваться.

Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.

Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.

Пример

На входе:


items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
На выходе, например, один из допустимых вариантов может быть таким:


{'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}
"""
items = {
    "спальник": 1.5,
    "палатка": 3.2,
    "термос": 0.6,
    "карта": 0.1,
    "фонарик": 0.3,
    "котелок": 0.8,
    "еда": 2.5,
    "одежда": 1.7,
    "обувь": 1.2,
    "нож": 0.2
}
max_weight = 7.0
backpack = {}

# Введите ваше решение ниже
"""def find_items(items, max_weight):
  backpack = {}
  for item, weight in items.items():
    if sum(backpack.values()) + weight <= max_weight:
      backpack[item] = weight
    return backpack

backpack = find_items(items, max_weight)
print(backpack)"""
""""backpack = {}

for item in items:
  if items[item] <= max_weight and item not in backpack:
    backpack[item] = items[item]
  else:
    print("Предмет " + item + " не может быть добавлен в рюкзак")
print(backpack)"""

backpacks_test = []
sorted_result = []
for i in range(2**len(items)):
    backpack_test = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack_test[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks_test.append(backpack_test)

full_result = [backpack_test for backpack_test in backpacks_test if backpack_test]
result = []
for item in full_result:
    if item not in result:
        result.append(item)

x = max_weight
for i in result:
    if dict(sorted(i.items(), key=lambda item: item[1], reverse=True)) == dict(sorted(backpack.items(), 
                                                                                      key=lambda item: item[1], reverse=True)):
        x += 1
if x > 0:  
    print(True)
else:
    print(False)
"""
Решение с сайта
backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight


"""