import time 
print("""

*******************************************************************************
      
                    BASİT DÜZEY HESAP MAKİNASI

      İŞLEMLER :
      1-) TOPLAMA
      2-) ÇIKARMA
      3-) ÇARPMA
      4-) BÖLME

*******************************************************************************

""")
a = int(input("Birinci Sayıyı Giriniz :"))
b = int(input("İkinci Sayıyı Giriniz :"))


işlemler = int(input("Yapmak İstediğiniz İşlemi Seçiniz :"))

if(işlemler ==1):
        print("Sayılar Toplanıyor...")
        time.sleep(1)
        print("{} İle {} Toplamı = {}".format(a,b,a + b))
        


elif(işlemler ==2):
        print("Sayılar Çıkartılıyor...")
        time.sleep(1)
        print("{} İle {} Farkı = {}".format(a,b,a - b))
        


elif(işlemler ==3):
        print("Sayılar Çarplıyor...")
        time.sleep(1)
        print("{} İle {} Çarpımı = {}".format(a,b,a * b))
        


elif(işlemler ==4):
        print("Sayılar Bölünüyor...")
        time.sleep(1)
        print("{} İle {} Bölümü = {}".format(a,b,a / b))
        


else:
    print("Geçersiz İşlem Program Sona Eriyor...")
       