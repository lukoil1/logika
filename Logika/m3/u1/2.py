with open('m3/u1/2.txt', 'r', encoding='utf8') as File:
    suma = 0
    for line in File:
        data = line.split(' ')
        if int(data[2]) ==5:
            print(data[0])
            
        suma = suma + int(data[2])

    avg = suma/11
    print(avg)