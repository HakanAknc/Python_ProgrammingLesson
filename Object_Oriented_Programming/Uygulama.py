class Oyun:
    def __init__(self):
        self.enerji = 50
        self.para = 100
        self.fabrika = 4
        self.isci = 10
    def goster(self):
        print("enerji: ", self.enerji)
        print("para: ", self.para)
        print("fabrika: ", self.fabrika)
        print("işci: ", self.isci)
    def fabrikakur(self,miktar):
        if self.enerji > 3 and self.para > 10:
            self.fabrika = miktar + self.fabrika
            self.enerji = self.enerji - 3
            self.para = self.para - 10
            print(miktar, " adet fabrika kurdunuz!\nTebrikler.")
        else:
            print("Yeni fabrika kuramazsınız.\nYeterli enerjiniz/paranız yok!")

macera = Oyun()

class Dusman(Oyun):   # Dusman sınıfı oyun sınıfını miras aldı
    def __init__(self):
        Oyun.__init__(self)
        self.ego = 0

    def goster(self):
        Oyun.goster(self)
        print("ego: ", self.ego)

dusman = Dusman()

# dusman.goster()
# print()
# print(dusman.enerji)
# print()
# dusman.fabrikakur(4)
# print()
# dusman.goster()
# print()
# macera.goster()

dusman.goster()