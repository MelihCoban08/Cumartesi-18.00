with open("bilgiler.txt","a",encoding="utf-8") as file:
    print("Çıkmak için 1 yazın")
    while True:
        a = str(input("Bilgi giriniz"))
        if a != str(1):
            file.write(a)
            file.write("\n")

        else:
            break