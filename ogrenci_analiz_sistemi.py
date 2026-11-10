print("BOOTCAMP ÖĞRENCİ ANALİZ SİSTEMİ")
print("--------------------------------")

ad=input("Adınızı giriniz: ")
yas=int(input("Yaşınızı giriniz: "))

print()
print("Aşağıdaki sorulara 1 ile 10 arasında puan veriniz.")
print("1 = Çok düşük, 10 = Çok iyi")
print()

python_puan=int(input("Python bilginiz kaç puan? "))
matematik_puan=int(input("Matematik bilginiz kaç puan? "))
ingilizce_puan=int(input("İngilizce seviyeniz kaç puan? "))
motivasyon=int(input("Motivasyonunuz kaç puan? "))

print()
calisma_suresi=int(input("Günde kaç saat çalışabilirsiniz? "))

print()
print("Hedef alan seçiniz:")
print("1 - Data Analyst")
print("2 - Data Scientist")
print("3 - Machine Learning Engineer")
print("4 - Backend Developer")
print("5 - Henüz bilmiyorum")

hedef_secim=int(input("Seçiminiz: "))

if hedef_secim==1:
    hedef_alan="Data Analyst"
elif hedef_secim==2:
    hedef_alan="Data Scientist"
elif hedef_secim==3:
    hedef_alan="Machine Learning Engineer"
elif hedef_secim==4:
    hedef_alan="Backend Developer"
else:
    hedef_alan="Kararsız"

alanlar= [
"Data Analyst",
"Data Scientist",
"Machine Learning Engineer",
"Backend Developer"
]

ogrenci= {
"ad":ad,
"yas":yas,
"python_puan":python_puan,
"matematik_puan":matematik_puan,
"ingilizce_puan":ingilizce_puan,
"motivasyon":motivasyon,
"calisma_suresi":calisma_suresi,
"hedef_alan":hedef_alan
}

toplam_puan=python_puan+matematik_puan+ingilizce_puan+motivasyon+calisma_suresi
ortalama_puan=toplam_puan/5

if ortalama_puan>=8:
    seviye ="İleri Seviye"
elif ortalama_puan>=5:
    seviye="Orta Seviye"
else:
    seviye="Başlangıç Seviyesi"

if python_puan>=7:
    python_durumu="Python seviyen iyi görünüyor."
elif python_puan>=4:
    python_durumu="Python seviyen orta. Bol tekrar yapmalısın."
else:
    python_durumu="Python temellerini baştan tekrar etmelisin."

if matematik_puan>=7:
    matematik_durumu="Matematik seviyen veri alanları için uygun."
elif matematik_puan>=4:
    matematik_durumu="Matematik seviyen orta. İstatistik ve temel matematik çalışmalısın."
else:
    matematik_durumu="Matematik seviyen düşük. Veri bilimi ve ML için önce matematik temeli kurmalısın."

if ingilizce_puan>=7:
    ingilizce_durumu="İngilizce seviyen teknik doküman okumak için iyi."
elif ingilizce_puan>=4:
    ingilizce_durumu="İngilizce seviyen orta. Teknik kelimeler öğrenmelisin."
else:
    ingilizce_durumu="İngilizce seviyen düşük. Günlük teknik İngilizce çalışmalısın."

if calisma_suresi>=5:
    calisma_durumu="Günlük çalışma süren çok iyi."
elif calisma_suresi>=3:
    calisma_durumu="Günlük çalışma süren yeterli."
else:
    calisma_durumu="Günlük çalışma süren düşük. Daha düzenli çalışmalısın."

if motivasyon>=8:
    motivasyon_durumu="Motivasyonun çok yüksek."
elif motivasyon>=5:
    motivasyon_durumu="Motivasyonun orta seviyede."
else:
    motivasyon_durumu="Motivasyonun düşük. Küçük hedeflerle başlamalısın."

if hedef_alan == "Data Analyst":
    if python_puan >= 5 and ingilizce_puan >= 4:
        alan_onerisi = "Data Analyst alanı senin için uygun. Sonraki aşamada Excel, SQL ve veri görselleştirme öğrenmelisin."
    else:
        alan_onerisi = "Data Analyst için önce Python temelleri ve İngilizce teknik terimleri çalışmalısın."

elif hedef_alan == "Data Scientist":
    if python_puan >= 6 and matematik_puan >= 6:
        alan_onerisi = "Data Scientist alanı için iyi bir başlangıcın var. Sonraki aşamada istatistik ve makine öğrenmesi öğrenmelisin."
    else:
        alan_onerisi = "Data Scientist için Python ve matematik seviyeni artırmalısın."

elif hedef_alan == "Machine Learning Engineer":
    if python_puan >= 7 and matematik_puan >= 7 and ingilizce_puan >= 5:
        alan_onerisi = "Machine Learning Engineer alanı için uygun görünüyorsun. Sonraki aşamada makine öğrenmesi algoritmalarına geçebilirsin."
    else:
        alan_onerisi = "Machine Learning Engineer olmak için Python, matematik ve İngilizce seviyeni güçlendirmelisin."

elif hedef_alan == "Backend Developer":
    if python_puan >= 6:
        alan_onerisi = "Backend Developer alanı için Python seviyen uygun. Sonraki aşamada veritabanı ve web framework öğrenebilirsin."
    else:
        alan_onerisi = "Backend Developer için önce Python koşullar, veri yapıları ve temel algoritma çalışmalısın."

else:
    
    if python_puan >= 6 and matematik_puan >= 6:
        alan_onerisi = "Senin için Data Analyst veya Data Scientist alanları uygun olabilir."
    elif python_puan >= 6 and matematik_puan < 6:
        alan_onerisi = "Senin için Backend Developer alanı daha uygun olabilir."
    else:
        alan_onerisi = "Şu an hedef seçmeden önce Python temellerini güçlendirmen daha doğru olur."


if ortalama_puan >= 8 and calisma_suresi >= 4:
    genel_yorum = "Bootcamp için oldukça hazırsın."
elif ortalama_puan >= 5 and calisma_suresi >= 3:
    genel_yorum = "Bootcamp için orta seviyede hazırsın. Düzenli çalışırsan başarılı olabilirsin."
else:
    genel_yorum = "Bootcamp öncesi temel tekrar yapman gerekiyor."

if calisma_suresi <3 or motivasyon <5:
    risk_durumu = "Riskli: Çalışma süresi veya motivasyon düşük."
elif python_puan < 4 or matematik_puan <4:
    risk_durumu = "Orta risk: Teknik temel eksik olabilir."
else:
    risk_durumu = "Risk düşük: Düzenli çalışma ile ilerleyebilirsin."

print ()
print("---------- ÖĞRENCİ ANALİZ RAPORU -----------")
print("Ad:", ogrenci["ad"])
print("Yaş:", ogrenci["yas"])
print("Hedef Alan:", ogrenci["hedef_alan"])
print("Ortalama Puan:", ortalama_puan)
print("Genel Seviye:",seviye)

print()
print("-------- DETAYLI DURUM ---------")
print("Matematik Durumu:",matematik_durumu)
print("İngilizce Durumu:", ingilizce_durumu)
print("Çalışma Durumu:",calisma_durumu)
print("Motivasyon Durumu:",motivasyon_durumu)


print()
print("---------- ALAN ÖNERİSİ ----------")
print(alan_onerisi)

print()
print("--------- GENEL YORUM -----------")
print(genel_yorum)

print()
print("---------- RİSK ANALİZİ ----------")
print(risk_durumu)

print()
print("--------- KAYITLI ALANLAR -----------")
print(alanlar)

print()
print("PROGRAM TAMAMLANDI")
