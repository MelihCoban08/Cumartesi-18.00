i = int(input("Bir sayı giriniz"))
while i % 2 != 0 and  i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
    print("girdiğiniz sayı asal sayıdır")

    break
else:
    if i != 2 and i != 3 and i != 5 and i != 7:
        print("girdiğiniz sayı asal sayı değildir")
    else:
        print("Girdiğiniz sayı asal sayıdır")