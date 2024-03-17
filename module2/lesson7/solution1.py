s = input('Введите строку: ').split(' ')
print(' '.join([s[i][::-1] for i in range(len(s))]))