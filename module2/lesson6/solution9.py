s: list[int] = input('Введите цены: ').split(', ')
# s = 50, 45, 30, 25
s.sort()
print('Отсортированные цены: ' + ', '.join(s[:]))