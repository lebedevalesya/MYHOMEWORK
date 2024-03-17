p: list[int] = input('Введите цены: ').split(', ')
p_iter = map(int, p)
p_int = list(p_iter)
# p = 10, 20, 30, 40, 50
print('Средняя цена товаров: ', sum(p_int)//(len(p)))