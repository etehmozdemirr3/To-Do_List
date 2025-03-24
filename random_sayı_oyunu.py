import random
import time

print("""

1 DEN 100 E KADAR BİR SAYI TAHMİN ET

OYUNDA TOPLAM 10 HAKKINIZ BULUNACAK HAKKINIZ BİTİNCE OYUN OTOMATİK BİTECEKTİR
      

""")

rast_gele = random.randint(1,100)

tahmin_hakkı = 10

while True:
    tahmin = int(input("Tahmininizi Giriniz :"))

    if (tahmin < rast_gele):
        print("Tahmin Sorgulanıyor...")
        time.sleep(1)
        print("Daha Büyük Bir Sayı Tahmin Ediniz")


    elif (tahmin > rast_gele):
        print("Tahmin Sorgulanıyor...")
        time.sleep(1)
        print("Daha Küçük Bir Sayı Tahmin Ediniz")

    else:
        print("Tahmininiz Doğru Tebrikler Doğru Tahmin :",rast_gele)