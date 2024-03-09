file = open("notlar.txt","r+",encoding="utf-8")
for satir in file:
    a = satir.split(',')
    x = int(a[1])
    y = int(a[2])
    z = int(a[3])

    ortalama = x*0.3 + y*0.5 +z*0.2

    if int(ortalama) < 50:
        print(a[0])
        print("başarısız")

    else:
        print(a[0])
        print("başarılı")