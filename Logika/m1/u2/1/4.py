'''
Кожні півроку медсестра вимірює зріст учнів. В архіві вже є результати вимірювань 6 «А» класу. 
Ось результати вимірювань: 160, 158, 165, 169, 155, 159, 161.
Необхідно: 
підрахувати та надрукувати середній зріст;
визначити зріст найвищого учня.
'''
spusok =[160, 158, 165, 169, 155, 159, 161]
#print(spusok[0]+ spusok[1])
suma=0
for i in spusok:
    suma+=i
print(suma/len(spusok))
max_height = 0
for i in spusok:
    if max_height<i:
        max_height=i
print(max_height)