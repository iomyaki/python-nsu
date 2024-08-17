number = 543354
a = number // 10 ** 5 % 10
b = number // 10 ** 4 % 10
c = number // 10 ** 3 % 10
d = number // 10 ** 2 % 10
e = number // 10 ** 1 % 10
f = number // 10 ** 0 % 10
if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')
