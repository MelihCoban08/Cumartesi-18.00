meyveler = ["muz","elma","kiraz"]
for x in meyveler:
    print(x)
    rakamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in rakamlar:
        if i <= 6 and i != 0:
            print(i)
        else:
            pass
rakamlar = [1,2,3,4,5,6,7,8,9,0]
toplam = 0
for i in rakamlar:
    toplam = toplam+i
print(toplam)


rakamlar = [1,2,3]
sifre = "abcd1234"
guvenlikkodu = "4853"
for i in rakamlar:
    Girilen_Sifre = str(input("şifrenizi girin"))
    if Girilen_Sifre == sifre:
        print("Giriş Yapıldı")
        break
    elif i == 3:
        print("3 Hatalı Giriş yaptınız. Güvenlik kodunu giriniz")
        Gkd = (input("Güvenlik kodunu girin"))
        if Gkd == guvenlikkodu:
            print("Giriş Başarılı")
            yenisifre = str(input("Yeni şifrenizi giriniz"))
            sifre = yenisifre
        else: Gkd == guvenlikkodu
        print("Giriş yapıldı")





