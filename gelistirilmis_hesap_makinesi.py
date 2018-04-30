print("""Math modülündeki hazır fonksiyonları kullanarak gelişmiş
bir hesap makinesi geliştirmeye çalışın.""")

import math
while True:
    print('*'*20, "MENÜ",'*'*20)
    print('0 --> Çıkış')
    print('1 --> Cos (kosinüs)')
    print('2 --> Exp (e üssü)')
    print('3 --> Factorial (faktöriyel)')
    print('4 --> Ceil (tavan değer)')
    print('5 --> Floor (taban değer)')
    print('6 --> Log10 (10 tabanına göre logaritma)')
    print('7 --> Pow (üs alma fonksiyonu)')
    print('8 --> Sin (sinüs)')
    print('9 --> Tan (tanjant)')
    print('10 --> Sqrt (karekök)')
    print('*'*20, "MENÜ",'*'*20)
    secim = int(input("Lütfen bir yöntem seçiniz... "))
    if secim < 0 or secim > 10:
        print("Yanlış seçim yaptınız, lütfen tekrar deneyiniz... ")
        continue
    elif secim == 0:
        print("Programdan çıkılıyor... ")
        break
    elif secim == 1:
        print('\n\n','*'*20, "KOSİNÜS MENÜSÜ", '*'*20)
        sayi = int(input("Radyan olarak bir değer giriniz: "))
        print("Girdiğiniz sayının kosinüsü: {}".format(math.cos(sayi)))
        print('\n\n','*'*20, "KOSİNÜS MENÜSÜ", '*'*20)
        print("\n\n")
    elif secim == 2:
        print('\n\n','*'*20, "e ÜZERİ DEĞER MENÜSÜ", '*'*20)
        sayi = int(input("e üzeri değeri hesaplanmak üzere bir değer giriniz: "))
        print("Girdiğiniz sayının e üzeri değeri: {}".format(math.exp(sayi)))
        print('*'*20, "e ÜZERİ DEĞER MENÜSÜ", '*'*20)
        print("\n\n")
    elif secim == 3:
        print('\n\n','*'*20, "FAKTÖRİYEL MENÜSÜ", '*'*20)
        sayi = int(input("Faktöriyeli hesaplanmak üzere bir değer giriniz: "))
        print("Girdiğiniz sayının faktöriyeli: {}".format(math.factorial(sayi)))
        print('*'*20, "FAKTÖRİYEL MENÜSÜ", '*'*20)
        print("\n\n")
    elif secim == 4:
        print('\n\n','*'*20, "TAVAN DEĞER MENÜSÜ", '*'*20)
        sayi = float(input("Tavan değeri hesaplanmak üzere bir değer giriniz: "))
        print("Girdiğiniz sayının tavan değeri: {}".format(math.ceil(sayi)))
        print('*'*20, "TAVAN DEĞER MENÜSÜ", '*'*20)
        print("\n\n")
    elif secim == 5:
        print('\n\n','*'*20, "TABAN DEĞER MENÜSÜ", '*'*20)
        sayi = float(input("Taban değeri hesaplanmak üzere bir değer giriniz: "))
        print("Girdiğiniz sayının taban değeri: {}".format(math.floor(sayi)))
        print('*'*20, "TABAN DEĞER MENÜSÜ", '*'*20)
        print("\n\n")
    elif secim == 6:
        print('\n\n','*'*20, "10 TABANINA GÖRE LOGARİTMA MENÜSÜ", '*'*20)
        sayi = int(input("10 tabanına göre logaritma değeri hesaplanmak üzere bir değer giriniz: "))
        print("Girdiğiniz sayının 10 tabanına göre logaritma değeri: {}".format(math.log10(sayi)))
        print('*'*20, "10 TABANINA GÖRE LOGARİTMA MENÜSÜ", '*'*20)
        print("\n\n")
    elif secim == 7:
        print('\n\n','*'*20, "ÜS ALMA MENÜSÜ", '*'*20)
        sayi = int(input("Üssü alınacak değeri giriniz: "))
        sayi2 = int(input("Üs değerini giriniz: "))
        print("Girdiğiniz sayının üssü: {}".format(math.pow(sayi, sayi2)))
        print('*'*20, "ÜS ALMA MENÜSÜ", '*'*20)
    elif secim == 8:
        print('\n\n','*'*20, "SİNÜS MENÜSÜ", '*'*20)
        sayi = int(input("Sinüsü alınacak değeri giriniz: "))
        print("Girdiğiniz sayının sinüsü: {}".format(math.sin(sayi)))
        print('*'*20, "SİNÜS MENÜSÜ", '*'*20)
        print("\n\n")
    elif secim == 9:
        print('\n\n','*'*20, "TANJANT MENÜSÜ", '*'*20)
        sayi = int(input("Tanjantı alınacak değeri giriniz: "))
        print("Girdiğiniz sayının tanjantı: {}".format(math.tan(sayi)))
        print('*'*20, "TANJANT MENÜSÜ", '*'*20)
        print("\n\n")
    elif secim == 10:
        print('\n\n','*'*20, "KAREKÖK MENÜSÜ", '*'*20)
        sayi = int(input("Karekökü alınacak değeri giriniz: "))
        print("Girdiğiniz sayının karekökü: {}".format(math.sqrt(sayi)))
        print('*'*20, "KAREKÖK MENÜSÜ", '*'*20)
        print("\n\n")
    else:
        print("Düzgün bir giriş yapmadınız, ana menüye yönlendiriliyorsunuz...")
        continue
