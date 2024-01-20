"""
  В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов.

Пример

На входе:
text = 'Hello world. Hello Python. Hello again.'

На выходе:
[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
"""

"""text = "Hello world. Hello Python. Hello again."
words = text.lower().replace("'","").split()

# Разбиваем слово на две части, если в нем есть апостроф
for i in range(len(words)):
    if "'" in words[i]:
        words[i] = words[i].split("'")

# Считаем количество вхождений каждого слова
count = {}
for w in words:
    if w not in count:
        count[w] = 0
    count[w]+=1

# Сортируем по количеству вхождений
sorted_count = sorted(count.items(),key=lambda x:x[1],reverse=True)

result = []
for c,w in sorted_count:
    result.append((c,w))

print (result)

"""
import re
from collections import Counter
from itertools import chain


pattern = re.compile(r"\b\w+\b")
text = "Python is python, is, IS, and PYTHON, it's."
words = pattern.findall(text)

words_lower = (word.lower() for word in words)
words_split = (word.split("'") for word in words_lower)
words_clean = (word for word in chain(*words_split) if word)

word_counts = Counter(words_clean)
top_10_words = word_counts.most_common(10)

print(top_10_words)  