s = input('Введите цены и скидку: ').split(', ')
d = int(s[-1])
p = sum(map(int, (s[:-1])))
def calculate_discount(p:int, d:int) -> int:
    return p * d // 100
print('Сумма скидки:', calculate_discount(p, d))

# 100, 200, 300, 10
# 50, 150, 250, 20