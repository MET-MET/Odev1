#Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

#int : Tam sayıları ifade eder. Örneğin 14, 58, 25
#long : Uzun olan tam sayıları ifade eder. Örneğin 123456
#float : Ondalıklı sayıları ifade eder. Örneğin 5.5, 44.5
#str (string) : Harf, rakam, kombinasyonlardan oluşur. Örneğin 
yazı= "kodlama.io ödev1"
#bool : Mantıksal veri tipidir. İçerisinde True yada False değeri alabilmektedir. Bir ifadenin doğruluğu veya bir döngönün kontrolü için kullanılabilmektedir.
kontrol=True
#kontrol isimli değişkene true değeri girildiğinde otomatik olarak bool veeri tipi olmaktadır.


#internet sitesinde araçlara bakılır, araçlar fiyatlanır ve fiyatlanan fiyata göre sıralanır.
arac1=100
arac2=200
arac3=200 
arac4=400
if arac1 < arac2 < arac3 < arac4 :
    print("dizilim doğrudur")
    # Eğer if bloğuna girilmez ise
elif arac2 == arac3 :
    print("arac2 ve arac3 birbirine eşittir")