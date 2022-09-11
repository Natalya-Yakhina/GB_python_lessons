# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print("Программа, которая найдёт сумму элементов списка, стоящих на нечётной позиции.")

array = [2, 3, 5, 9, 3]

sum = 0

for i in range(len(array)) :
    if (i % 2 != 0):
        sum += array[i]

print(f'Сумма элементов списка - [2, 3, 5, 9, 3], стоящих на нечётной позиции = {sum}') 