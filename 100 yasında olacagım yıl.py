import datetime

# Şu anki yılı al
yil = datetime.datetime.now().year

isim = input("Ad: ")
yas = int(input("Yaş: "))

kalan = 100 - yas
yuz_yil = yil + kalan

print("Merhaba", isim)
print("100 yaşına geleceğin yıl:", yuz_yil)
