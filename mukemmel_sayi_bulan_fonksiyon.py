print("""1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana
yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane
fonksiyon yazın. Bir sayının bölenlerinin toplamı kendine eşitse bu sayı
mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).""")

def MukemmelSayi(sayi):
    liste = []
    toplam = 0
    orijinal_sayi = sayi
    sayac = 1
    while sayac <= sayi - 1:
        if sayi % sayac == 0:
            liste.append(sayac)
            print(liste)
            sayi /= sayac
            print("Sayi = ",sayi)
            sayac += 1
            print("Sayac = ",sayac)
        else:
            sayac += 1
            print("Sayac = ", sayac)
        for m in liste:
            toplam += m
            print("Toplam: ",toplam)
            if toplam == orijinal_sayi:
                print("{} mükemmel bir sayıdır... Çarpanları: {}".format(orijinal_sayi, liste))
            else:
                continue

for o in range(1, 1001):
    print(MukemmelSayi(o))
