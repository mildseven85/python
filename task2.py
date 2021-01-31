a = int(input("Введите время в секундах: "))
h = (a//3600) % 24
m = (a//60) % 60
s = (a % 60)
if h < 10:
    h = '0' + str(h)
else:
    h = h
if m < 10:
    m = '0' + str(m)
else:
    m = m
if s < 10:
    s = '0' + str(s)
else:
    s = str(s)
print("Ваше время в фрмате ЧЧ:ММ:СС: " + str(h) + ':' + str(m) + ':' + str(s))
