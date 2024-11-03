import random
passw = [0,1,2,3,4,5,6,7,8,9,0,'!','@','#','$','%','a','s','d','q','w','e','r','r','t','y','u','i','o','p','f','g','h','j','k','l','z','x','c','v','b','n','m']
q = int(input('Сколько символов:'))
for i in range(q):
    gen = random.choice(passw)
    print(gen,end='')
print()
while True:
    q1 = int(input('Сгенерировать? 0.Да,1.Нет'))
    if q1 == 0:
        for i in range(q):
            gen = random.choice(passw)
            print(gen,end='')
        print()
    elif q1 == 1:
        print('Ок')
        break