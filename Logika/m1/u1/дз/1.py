print('Хто написав пригоди Тома Соєра?')
widp = input('твій варінт')
i = 1
while widp != 'Марк Твен':
    print('спробуй ще раз')
    widp = input('твій варіант')
    i += 1
print("відповдь зарахована з", i ,"спроби")