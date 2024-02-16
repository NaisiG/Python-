"""Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens), 
которая проверяет все возможные пары ферзей.
Известно, что на доске 8x8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.

Пример использования.
На входе:


queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)] 
На выходе:


False"""
"""
def check_queens(board):
    for i in range(8):
        for j in range(i + 1, 8):
            if is_attacking(board[i], board[j]):
                return False
    return True

def is_attacking(queen1, queen2):
    x1, y1 = queen1
    x2, y2 = queen2
    if x1 == x2:
        return y1 != y2
    elif y1 == y2:
        return x1 != x2
    else:
        return abs(x1 - x2) == abs(y1 - y2)

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)] 
result = check_queens(queens)
if result:
    print("True")
else:
  print("False")"""
 
"""import itertools

def is_attacking_pair(q1: tuple, q2: tuple) -> bool:
    # your code here
    pass

def check_queens(boards: list) -> bool:
    for board1 in boards:
        for board2 in boards:
            if board1 == board2:
                continue
            if is_attacking_pair(board1, board2):
                return False
    return True

if __name__ == '__main__':
    queens_input = [
        tuple(map(int, input().split()))
        for _ in range(161)
    ]

    boards = list(itertools.combinations(queens_input, r=2))
    result = check_queens(boards)

    if result:
        print("False")
    else:
        print("True")"""

'''
def check_attack(queen1, queen2):
    # Проверка, бьет ли первый ферзь второго
    x1, y1 = queen1
    x2, y2 = queen2
    if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
        return True
    else:
        return False

def check_all_attack(queens):
    for queen1 in queens:
        for queen2 in queens:
            if queen1 != queen2 and check_attack(queen1,queen2):
                return False
    return True

#group_of_queens = [[int(i) for i in input().split()] for _ in range(8)]
queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)] 
print(check_all_attack(queens))
'''
def are_queens_attacking_each_other(queens: list(tuple())):
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if queens[i][0] == queens[j][0] or \
               queens[i][1] == queens[j][1] or \
               abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
               return False
    return True

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]

if __name__ == '__main__':
    for i, value in enumerate(are_queens_attacking_each_other(queens), 1):
        print(f'{i} - {value}')

