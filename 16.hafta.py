import random

def tkm():
    tas = 1
    makas = 2
    kagit = 3
    print("1-Taş - 2-Makas - 3-Kağıt")
    while True:

        tahmin = int(input("hamleni gir"))
        x = random.randint(1, 3)
        if x == 1 and tahmin == 1:
            print("Berabere kaldık","hamlem",x)

        if x == 1 and tahmin == 2:
            print("kaybettin","hamlem",x)

        if x == 1 and tahmin == 3:
            print("kazandın","hamlem",x)

        if x == 2 and tahmin == 1:
            print("kazandın","hamlem",x)

        if x == 2 and tahmin == 2:
            print("berabere","hamlem",x)

        if x == 2 and tahmin == 3:
            print("kaybettin","hamlem",x)

        if x == 3 and tahmin == 1:
            print("kaybettin","hamlem",x)
        if x == 3 and tahmin == 2:
            print("kazandın","hamlem",x)

        if x == 3 and tahmin == 3:
            print("berabere","hamlem",x)


tkm()


