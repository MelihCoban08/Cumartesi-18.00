class hayvan():
    def __init__(self,isim,yas,tur):
        self.isim = isim
        self.yas = yas
        self.tur = tur
    def bilgilerigoster(self):
        print("isim:",self.isim,"Yas:",self.yas,)


class kopek(hayvan):
    def __init__(self, isim, yas,tur,renk="bilinmiyor"):
        super().__init__(isim,yas,tur)
        self.renk = renk
    def konus(self):
        print(self.isim + ": hav hav")
    def yask(self):
        a = 20 - self.yas
        print("Kalan ömür:",a,"yıl")
    def bilgilerigoster(self):
        print("isim:",self.isim,"Yas:",self.yas,"Tür:",self.tur)



class kedi(hayvan):
    def konus(self):
        print(self.isim + " :miyav")



kopek1 = kopek("rita",6,"Golden")
kedi1 = kedi("simba",4,"british")

kopek1.yask()
kopek1.bilgilerigoster()
kedi1.konus()
