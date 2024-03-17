s: list[int] = input('Введите список: ').split(', ')
k = int(s[1])
n = int(s[0])
print('Числа подсписка:', ', '.join(s[n::k]))