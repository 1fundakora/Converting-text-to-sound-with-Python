from gtts import gTTS #ses kütüphanesi
import os

text = "Bir yazıyı şekil, anlatım ve noktalama özellikleriyle oluşturan kelimelerin bütününe metin adı verilir. Diğer bir ifadeyle metin, iletişim kurmak için oluşturulan cümleler topluluğudur. Sözlü ya da yazılı iletişim için üretilen anlamlı yapıdır. Yazar, iletmek istediği mesajı metin aracılığıyla ifade eder."


language="tr" #konuşma dili belirlendi

params=gTTS(text=text , lang=language,slow=False) #parametlere ayarlanıp atandı
params.save("text.mp3") #mp3 dosyası oluşturulup kaydedildi

os.system("start text.mp3")