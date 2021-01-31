n = int(input('Введите число 1-99: '))
if n < 10:
    x = n * 11
    y = n * 111
    z = n + x + y
if n >= 10:
    x = n * 101
    y = x * 100 + n
    z = n + x + y
print("ИТОГО: " + str(z))
