
while True:
    i = int(input("Bir sayı giriniz"))
    while  i % 2 != 0 and  i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        if  i % 2 != 0 and  i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print("girdiğiniz sayı asal sayıdır")
            i = int(input("bir sayı giriniz"))




    else:
        if i != 2 and i != 3 and i != 5 and i != 7:
            print("girdiğiniz sayı asal sayı değildir")
        else:
            print("Girdiğiniz sayı asal sayıdır")