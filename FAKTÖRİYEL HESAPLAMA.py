def faktoriyel ():
    n = int(input("Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz\n"))
    faktoriyel = 1
    i = 1
    
    if n >= 0:
        while i <= n:
            faktoriyel *= i
            i += 1
    print(n,"sayısının faktoriyeli",faktoriyel,"budur")
    
    if n < 0:
        print("Girdiğiniz sayı 0 dan büyük olmalı")

faktoriyel()
