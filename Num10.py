a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

d = (b**2) - (4*a*c)

if d<0:
    print('no result')

elif d == 0:
    x = round((-b) / (2*a), 2)
    print(f'x = {x}')

else:
    x1 = round((-b + (d)) / (2*a), 2)
    x2 = round((-b - (d)) / (2*a), 2)

if x1 == x2:
    print(f'x1 = x2 = {x1}')

else:
    print(f'x1 = {x1}\nx2 = {x2}')
    \\не работает\\
    