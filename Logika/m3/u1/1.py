with open('m3/u1/1.txt', 'r', encoding='utf8') as File:
    data = File.read()
    print(data)

widpowid = input('Хто автор')

with open('m3/u1/1.txt', 'a', encoding='utf8') as File:
    File.write(widpowid)