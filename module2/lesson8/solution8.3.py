s = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
p = sorted(s.values())
ReverseS = dict(map(reversed, s.items()))
print('Самый дешевый:', ReverseS[p[0]], '–', str(p[0]), 'руб.')
print('Самый дорогой:', ReverseS[p[len(s)-1]], '–', str(p[len(s)-1]), 'руб.')
