#random modülü ve kartlar listeleri
import random

#kart oluşturmak için
suits = ('Kupa','Karo','Maça','Sinek')
rutbeler = ('İki','Üç','Dört','Beş','Altı','Yedi','Sekiz','Dokuz','On','Vale','Kız','Papaz','As')
degerler = {"İki":2,"Üç":3,"Dört":4,"Beş":5,"Altı":6,"Yedi":7,"Sekiz":8,"Dokuz":9,"On":10,"Vale":10,"Kız":10,"Papaz":10,"As":11}

oynuyor = True

#kart sınıfını oluşturalım. bu sınıf deste oluşturmada işe yarayacak
class Kart:
    def __init__(self,suit,rutbe):
        self.suit = suit
        self.rutbe = rutbe

    #kartları yazmak için
    def __str__(self):
        return f"{self.suit} {self.rutbe}"


class Deste:
    def __init__(self):
        self.deste = []
        for suit in suits:
            for rutbe in rutbeler:
                yeni_kart = Kart(suit,rutbe)
                self.deste.append(yeni_kart)

    #desteyi yazdırmak için
    def __str__(self):
        komple_kartlar = ' '
        for kart in self.deste:
            komple_kartlar += "\n" + kart.__str__()

        return "Tüm kartlar: " + komple_kartlar

    #desteyi karıştırmak için
    def karistir(self):
        random.shuffle(self.deste)

    #desteden bir kart çekmek için
    def kart_cek(self):
        tek_kart = self.deste.pop()
        return tek_kart


#bilgisayar ve oyuncunun elini hesaplamak için el sınıfı
class El:
    def __init__(self):
        self.el = []
        #oyuncunun elindeki kart değerleri toplamı
        self.deger = 0
        self.as_sayisi = 0

    #ele kart ekler ve değerini hesaplar
    def kart_ekle(self,kart):
        self.el.append(kart)
        self.deger += degerler[kart.rutbe]
        if kart.rutbe == "As":
            self.as_sayisi+=1

    #asları saymak için
    def aslar(self):
        #değer 21 den büyükse ve elde as varsa
        while self.deger > 21 and self.as_sayisi:
            #değeri 10 azaltır
            self.deger -= 10
            #asların sayısını azaltır
            self.as_sayisi -= 1

#chipleri ayarlayalım
class Chipler:
    def __init__(self):
        #iki oyuncunun total çipi 100 kaybedip kazandıkça bu artacak veya azalacak
        self.total = 100
        self.bahis = 0

    def bahis_kazanma(self):
        self.total += self.bahis

    def bahis_kaybetme(self):
        self.total -= self.bahis

#kullanıcıdan bahis değeri alalım
def bahis_al(çipler):
    while True:
        try:
            çipler.bahis = int(input("Bahis değeri giriniz: "))

        except ValueError:
            print("Özür dilerim, lütfen tam sayı değeri giriniz.")

        else:
            if çipler.bahis > çipler.total:
                print("Bahsiniz total parayı geçemez.",çipler.total)
            else:
                break

#desteden kart çekip ele ekler
def hit(deste,el):
    el.kart_ekle(deste.kart_cek())
    el.aslar()
    return el

#oyuncuya hit mi stand mı sormak için
def hit_veya_stand(deste,el):
    global oynuyor #kodun ilerisinde olcak bir değişken

    while True:
        cevap = input("Hit için h, stand için s: ")

        if cevap.lower() == "h":
            hit(deste,el)

        elif cevap.lower() == "s":
            print("Oyuncu bekliyor. Krupiye oynuyor.")
            oynuyor = False

        else:
            print("Yanlış giriş lütfen tekrar giriniz")
            continue

        break

#bazı kartları göstermek için
def bazıKartları_goster(oyuncu,krupiye):
    print("Krupiye eli: ")
    print("Gizli kart")
    print(krupiye.el[1],"\n")

    print("Oyuncu eli: ")
    for i in oyuncu.el:
        print(i)

    print(f"Oyuncu eli değeri: {oyuncu.deger}")

#tüm kartları göstermek için
def tumKartları_goster(oyuncu,krupiye):
    print("Krupiye eli: ")
    for j in krupiye.el:
        print(j)

    #for ile yapmak yerine print("Krupiye eli: ", *krupiye.el,sep="\n") şeklinde de olması mümkün aynı şey. sep alt satıra geçirir


    #krupiye eli değeri
    print(f"Krupiye eli değeri: {krupiye.deger}")

    print("Oyuncu eli: ")
    for i in oyuncu.el:
        print(i)

    #oyuncu eli değeri
    print(f"Oyuncu eli değeri: {oyuncu.deger}")

#oyuncu bust olursa
def oyuncu_bust(oyuncu,krupiye,chipler):
    print("Oyuncu bust oldu")
    chipler.bahis_kaybetme()

#oyuncu kazanırsa
def oyuncu_kazandı(oyuncu,krupiye,chipler):
    print("Oyuncu kazandı")
    chipler.bahis_kazanma()

#krupiye bust olursa
def krupiye_bust(oyuncu,krupiye,chipler):
    print("Krupiye bust oldu")
    chipler.bahis_kazanma()

#krupiye kazanırsa
def krupiye_kazandı(oyuncu,krupiye,chipler):
    print("Krupiye kazandı")
    chipler.bahis_kaybetme()

def berabere(oyuncu,krupiye):
    print("Oyuncu ve krupiye berabere! Push")

#oyun kısmı
while True:
    print("Blackjack oyununa hoşgeldiniz! Hedefiniz 21 olmadan mümkün olduğunca yaklaşmak veya 21 yapmak. Krupiye 17' ye ulaşana kadar hit yapar. Aslar 1 veya 11 yapar.")

    #deste oluşturma
    yeni_deste = Deste()
    yeni_deste.karistir()

    #oyuncu eli oluşturma
    oyuncu_el = El()
    oyuncu_el.kart_ekle(yeni_deste.kart_cek())
    oyuncu_el.kart_ekle(yeni_deste.kart_cek())

    #krupiye eli oluşturma
    krupiye_el = El()
    krupiye_el.kart_ekle(yeni_deste.kart_cek())
    krupiye_el.kart_ekle(yeni_deste.kart_cek())

    #chipleri oluşturma
    oyuncu_chip = Chipler()

    #oyuncudan bahis al
    bahis_al(oyuncu_chip)
    print("\n")

    #bazı kartları göster
    bazıKartları_goster(oyuncu_el,krupiye_el)

    while oynuyor:

        #stand gelirse oynuyor=False olcak hitte değişmiyor
        hit_veya_stand(yeni_deste,oyuncu_el)
        bazıKartları_goster(oyuncu_el,krupiye_el)

        #hit gelirse ve 21 geçerse oyuncu otomatikman kaybedecek
        if oyuncu_el.deger > 21:
            oyuncu_bust(oyuncu_el,krupiye_el,oyuncu_chip)
            break

    #oyuncu eli 21 den küçükse olacaklar
    if oyuncu_el.deger <= 21:

        #krupiye 17 olana kadar kart çekecek
        while krupiye_el.deger < 17:
            hit(yeni_deste,krupiye_el)

        print("\n")
        tumKartları_goster(oyuncu_el,krupiye_el)

        if krupiye_el.deger > 21:
            krupiye_bust(oyuncu_el,krupiye_el,oyuncu_chip)

        elif krupiye_el.deger > oyuncu_el.deger:
            krupiye_kazandı(oyuncu_el,krupiye_el,oyuncu_chip)

        elif krupiye_el.deger < oyuncu_el.deger:
            oyuncu_kazandı(oyuncu_el,krupiye_el,oyuncu_chip)

        else:
            berabere(oyuncu_el,krupiye_el)

    print("\nOyuncunun kazancı: ",oyuncu_chip.total)

    yeni_oyun = input("Yeniden oynamak ister misiniz? Evet için e, hayır için h: ")

    if yeni_oyun.lower() == "e":
        oynuyor = True
        continue

    else:
        print("Oynadığınız için teşekkürler")
        break
