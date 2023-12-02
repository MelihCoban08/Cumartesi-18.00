Kullanıc_Adı = "MelihCoban"
Sifre = "Mc2008d"
numara = 123456789
print("Kullanıcı Adı giriniz")
ka = input("")
print("Şifre giriniz")
sifre = input("")
if ka == Kullanıc_Adı and Sifre == sifre:
    print("giriş yapılıyor")
else:
    print("kullanıcı adı veya Şifre yanlış tekrar giriniz veya Şifreniz yada kullanıcı adını sıfırlamak için şifremi unuttum İşleminin numarasını girin")
    print("Sifremi unuttum")
    secim = input()
    if  secim != 2:
        print("telefon numarası giriniz")
        gnumara = int(input(""))
        if gnumara == numara:
            print("kod 123")
            kod = 123
            secim2 = int(input("SMS olarak gelen kodu giriniz"))
            if secim2 != kod:
                print("Kod yanlış hesaba giriş yapılamadı")
            else:
                input("Yeni şifrenizi girin")
                Sifre == yenisifre

        else:
            print("Numara yanlış hesaba giriş yapılamadı")
    elif secim != 1:
        print("İyi günler")


