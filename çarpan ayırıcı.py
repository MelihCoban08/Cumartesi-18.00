lista = []
i = 0
a = int(input("sayı giriniz"))
i = a
while i%1 == 0:
    if i%2 == 0:
        lista.append(i//2)
        lista.append(2)
    if i %3 == 0:
        lista.append(i//3)
        lista.append(3)
    if i %4 == 0:
        lista.append(i//4)
        lista.append(4)
    if i %5 == 0:
        lista.append(i//5)
        lista.append(5)
    if i % 6 == 0:
        lista.append(i//6)
        lista.append(6)
    if i % 7 == 0:
        lista.append(i//7)
        lista.append(7)
    if i % 8 == 0:
        lista.append(i//8)
        lista.append(8)
    if i % 9 == 0:
        lista.append(i//9)
        lista.append(9)
    print(lista)
    break