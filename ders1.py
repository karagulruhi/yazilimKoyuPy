class Kedi():
  isim = "Kedi"
  renk = "Siyah"
  ayak_sayisi = 4
  cinsiyet = "Dişi"
  kilo = 3
  boy = 20
  yas = 2
  irk="Tekir"
  goz_rengi="Yeşil"
husniye = Kedi()
# constructor
# dunder metotlar
class Kedi():
  #constructor metotum
  # self nesnenin kendisi
  def __init__(self, isim, renk, cinsiyet, kilo, boy, yas, irk, goz_rengi):
    self.isim = isim
    self.renk = renk
    self.ayak_sayisi = 4
    self.cinsiyet = cinsiyet
    self.kilo = kilo
    self.boy = boy
    self.yas = yas
    self.irk = irk
    self.goz_rengi = goz_rengi
husniye = Kedi("Husniye", "Kahverengi", "Dişi", 4, 40, 2.5, "Tekir", "Yeşil")
ceku = Kedi("Ceku", "Gri", "Dişi", 4, 40, 1, "Tekir", "Yeşil")
class Kopek():
    def __init__(self, isim, renk, cinsiyet, kilo, boy, yas, irk, goz_rengi, ses):
      self.isim = isim
      self.renk = renk
      self.ayak_sayisi = 4
      self.cinsiyet = cinsiyet
      self.kilo = kilo
      self.boy = boy
      self.yas = yas
      self.irk = irk
      self.goz_rengi = goz_rengi
      self.ses = ses

    def SesCikar(self):
      return self.ses
karabas = Kopek("Karabas", "Beyaz", "Erkek", 5, 20,4,"Rotweiller", "Siyah","Hav hav")


class Hayvan():
    def __init__(self, isim, renk, ayak_sayisi, cinsiyet, kilo, boy, yas, irk, goz_rengi, ses):
      self.isim = isim
      self.renk = renk
      self.ayak_sayisi = ayak_sayisi
      self.cinsiyet = cinsiyet
      self.kilo = kilo
      self.boy = boy
      self.yas = yas
      self.irk = irk
      self.goz_rengi = goz_rengi
      self.ses = ses
# inherit alma - türetme
class ayaksizHayvanlar(Hayvan):
  def __init__(self, isim, renk, cinsiyet, kilo, boy, yas, irk, goz_rengi, ses):
    super().__init__(isim, renk, 0, cinsiyet, kilo, boy, yas, irk, goz_rengi, ses)
class Yilan(ayaksizHayvanlar):
  def __init__(self, isim, renk, cinsiyet, kilo, boy, yas, irk, goz_rengi, ses):
    super().__init__(isim, renk, cinsiyet, kilo, boy, yas, irk, goz_rengi, ses)
selami = Yilan("Selami","Beyaz","Erkek",3, 10, 4, "Tavuk", "Siyah","tısss")
# print(selami.ayak_sayisi)
## Sınıflarda Metot Tipleri
class Person():
  def __init__(self, isim, yas, cinsiyet,aile,pet):
    self.isim = isim
    self.yas = yas
    self.cinsiyet = cinsiyet
    self.aile = aile
    self.level = pet
   

  def SelfaileGetir(self):
    return self.aile

  def yasArttır(self):
    self.yas += 1


Tyron = Person("tyron", 42, "Erkek", "lannester","aslan")
# print(Tyron.aile)
# print (Tyron.SelfaileGetir())

class Person():
  def __init__(self, isim, yas, cinsiyet, pet):
    self.isim = isim
    self.yas = yas
    self.cinsiyet = cinsiyet
    self.pet = pet
    self.aile = self.__AileYerlestir()


  def SelfGucEkle(self, guc):
    self.guc = guc

  def SelfGucGetir(self):
    return self.guc

  @classmethod
  def ClsGucEkle(cls, guc):
    cls.guc = guc
    #parametre azaltmak için classmethod kullanılır
  @classmethod
  def ClsGucGetir(cls):
    return cls.guc




  def LevelArttir(self):
    self.level += 1

  def __AileYerlestir(self):
    if type(self) is Lannester:
      return "Lannester"
    if type(self) is Stark:
      return "Stark"

    else:
      return "-"
class Stark(Person):
  def __init__(self, isim, yas, cinsiyet,pet):
    super().__init__(isim, yas, cinsiyet,pet)
class Lannester(Person):
  def __init__(self, isim, yas, cinsiyet,pet):
    super().__init__(isim, yas, cinsiyet,pet)    
jon = Stark("jon", 23, "Erkek", "ulu_kurt")
print(jon.aile)