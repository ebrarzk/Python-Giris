
sayi1 = input("Lütfen birinci sayıyı girin: ")


sayi2 = input("Lütfen ikinci sayıyı girin: ")


try:
    s1 = float(sayi1) 
    s2 = float(sayi2)
except ValueError:
    print("\n⚠️ Hata: Lütfen geçerli sayılar girdiğinizden emin olun!")
    exit()


toplam = s1 + s2
fark = s1 - s2
carpim = s1 * s2

if s2 != 0:
    bolum = s1 / s2
else:
    bolum = "Sıfıra bölme yapılamaz!"


print("\n--- SONUÇLAR ---")
print(f"Girdiğiniz sayılar: {s1} ve {s2}")
print(f"Toplam ( + ): {toplam}")
print(f"Fark ( - ): {fark}")
print(f"Çarpım ( * ): {carpim}")
print(f"Bölüm ( / ): {bolum}")
print("----------------")