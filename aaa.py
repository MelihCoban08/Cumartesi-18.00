toplam = 0
i = 0
while i < 20:
    i += 1
    toplam = i + toplam
    if toplam >= 102:
        print(i , "bu sayıdan sonra toplam 102 den büyük")
        break
        i = 0
        while i < 6:
            i += 1
            if i == 3:
                continue
            print(i)