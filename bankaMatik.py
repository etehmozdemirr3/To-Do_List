import time

print("""
***************************************************************************************
      
                                BANKAMATİK PROGRAMI
      İŞLEMLER :

      1-) BAKİYE GÖR

      2-) PARA YATIR

      3-) PARA ÇEK

      4-) PARA GÖNDER

      5-) KREDİ ÇEK 

      6-) KREDİ BORCU ÖDE

      7-) UYGULAMDAN ÇIKMAK İÇİN Q YA BASIN

      BAKİYENİZ = 10.000 TL DİR.

      ÇEKİLEBİLİR KREDİ TUTARI = 100.000 TL DİR.

***************************************************************************************

""")

bakiye = 10000
kredi_limiti = 100000
kredi_borcu = 0  # Kullanıcının çektiği krediyi takip etmek için

while True:
    işlemler = input("Yapmak İstediğiniz İşlemi Seçiniz :")

    if işlemler == "q":
        print("Programdan Çıkılıyor...")
        time.sleep(1)
        print("Program Sona Erdi.")
        break

    elif işlemler == "1":
        print("Güncel Bakiyeniz: {} TL".format(bakiye))

    elif işlemler == "2":
        miktar = int(input("Yatırmak İstediğiniz Miktarı Giriniz: "))
        bakiye += miktar
        print("Bakiyeniz Güncellendi. Yeni Bakiye: {} TL".format(bakiye))

    elif işlemler == "3":
        miktar = int(input("Çekmek İstediğiniz Miktarı Giriniz: "))
        if bakiye < miktar:
            print("Yetersiz Bakiye..")
        else:
            bakiye -= miktar
            print("Hesabınızdan Para Çekildi. Güncel Bakiyeniz: {} TL".format(bakiye))

    elif işlemler == "4":
        miktar = int(input("Göndermek İstediğiniz Miktarı Giriniz: "))
        if bakiye < miktar:
            print("Göndermek İstediğiniz Miktar Bakiyenizi Geçmektedir..")
        else:
            bakiye -= miktar
            print("Hesabınızdan {} TL Gönderildi. Güncel Bakiyeniz: {} TL".format(miktar, bakiye))

    elif işlemler == "5":
        miktar = int(input("Çekmek İstediğiniz Kredi Tutarını Giriniz: "))
        if miktar > kredi_limiti - kredi_borcu:
            print("Hesabınıza Tanımlanan Krediden Fazla Kredi Çekemezsiniz..")
        else:
            bakiye += miktar
            kredi_borcu += miktar
            print("Kredi Tutarınız Hesabınıza Yatırılmıştır. Güncel Bakiyeniz: {} TL".format(bakiye))

    elif işlemler == "6":
        miktar = int(input("Ödemek İstediğiniz Kredi Tutarını Giriniz: "))
        if miktar > bakiye:
            print("Yetersiz Bakiye! Önce Hesabınıza Para Yatırın.")
        elif miktar > kredi_borcu:
            print("Borçtan Fazla Ödeme Yapamazsınız!")
        else:
            bakiye -= miktar
            kredi_borcu -= miktar
            print("Kredi Borcunuzun {} TL'si Ödenmiştir. Güncel Bakiyeniz: {} TL".format(miktar, bakiye))

    else:
        print("Geçersiz İşlem! Lütfen tekrar deneyin.")