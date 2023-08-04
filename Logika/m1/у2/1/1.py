while 1:
    try:
        a = int(input('Введіть довжину першої сторони:'))
        break
    except:
        print('вказуйте тільки числа')
        
while 1:
    try:
        b = int(input('Введіть довжину другої сторони:'))
        break
    except:
        print('вказуйте тільки числа')
        


s = a * b
print('Площа прямокутника:', s)
