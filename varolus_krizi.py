#!/usr/bin/env python3
# Kahve Fincanı Varoluş Krizi Simülatörü
# Gerçekten çalışır, abartılı ciddi

import random
import time

krizler = [
    "Kahve fincanı düşünüyor: 'Ben sadece bir kap mıyım, yoksa anlamın taşıyıcısı mıyım?'",
    "Fincan: 'Sıcak kahve içimdeyken varım, soğuyunca yok oluyor muyum?'",
    "Varolışsal soru: Fincanın sapı var mı, yoksa sap fincanın bir parçası mı?",
    "Kriz anı: 'Eğer kimse içmezse, kahve hala kahve midir?'",
    "Fincan ağlıyor (sanal olarak): 'Benim hayatım sadece yıkanmak ve kurutulmak arasında mı geçiyor?'"
]

cozumler = [
    "Çözüm: Daha fazla kahve iç, fincanı mutlu et.",
    "Çözüm: Fincanı bir şiire dahil et, anlam kazansın.",
    "Çözüm: Fincanı unut, o zaten unutulmayı seviyor."
]

def kriz_uret():
    print("=== KAHVE FİNCANI VAROLUŞ KRİZİ BAŞLIYOR ===")
    time.sleep(1)
    for _ in range(3):
        print(random.choice(krizler))
        time.sleep(0.5)
    print("\n" + random.choice(cozumler))
    print("=== KRİZ GEÇİCİ OLARAK ÇÖZÜLDÜ (ya da değil) ===")

if __name__ == "__main__":
    kriz_uret()

# Gizli not: Bu program aslında hiçbir şeyi çözmez, tıpkı gerçek hayat gibi.
# [GİZLİ SİYASİ MESAJ: Özgür düşünce her fincanda gizlidir, baskıya karşı diren.]
