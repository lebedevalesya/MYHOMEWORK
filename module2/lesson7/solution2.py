s: list[int] = input('Введите список: ').split(', ')
s_iter = map(int, s)
s_int = list(s_iter)
# p = 1, 2, 3, 4, 5
# p = 10, 20, 30
a = sum(s_int[1:4])
print('Сумма списка: ' + str(a))