# Задача 10. Симметричная последовательность
# Что нужно сделать
#
# Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево.
# Например, следующие последовательности являются симметричными:
#
# 1 2 3 4 5 4 3 2 1
#
# 1 2 1 2 2 1 2 1
#
# Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет,
# какое минимальное количество и каких чисел надо приписать в конец этой последовательности, чтобы она стала симметричной.
#
#
#
# Пример 1:
#
# Кол-во чисел: 5
#
# Число: 1
#
# Число: 2
#
# Число: 1
#
# Число: 2
#
# Число: 2
#
#
#
# Последовательность: [1, 2, 1, 2, 2]
#
# Нужно приписать чисел: 3
#
# Сами числа: [1, 2, 1]
#
#
#
# Пример 2:
#
# Кол-во чисел: 5
#
# Число: 1
#
# Число: 2
#
# Число: 3
#
# Число: 4
#
# Число: 5
#
#
#
# Последовательность: [1, 2, 3, 4, 5]
#
# Нужно приписать чисел: 4
#
# Сами числа: [4, 3, 2, 1]
#
#
#
# Что оценивается
#
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

size = input("Введите количество цифр: ")
while not size.isdigit():
    size = input("Ошибка! Некорректный ввод. Введите количество цифр: ")
size = int(size)
list = []

for i in range(size):
    unit = input(f"Введите {i + 1} элемент: ")
    while not unit.isdigit():
        unit = input(f"Ошибка! Некорректный ввод. Введите {i + 1} элемент: ")
    unit = int(unit)
    list.append(int(unit))

print("Последовательность:", list)
check = -1
answer = []
for i in range(-len(list), 0):
    if list[i] == list[check]:
       check -= 1
if size + check + 1 == 0:
    print("\nПоследовательность симметрична. Добавлений не требуется.")
else:
    answer.extend(list[-len(list): check + 1])
    answer.reverse()
    print(f"Необходимо добавить чисел: {size + check + 1}\nЭти числа: {answer}")
