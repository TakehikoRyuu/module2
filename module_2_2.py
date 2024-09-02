# Условная конструкция. Операторы if, elif, else.
first = input('Введите число №1: ')
second = input('Введите число №2: ')
third = input('Введите число №3: ')
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
