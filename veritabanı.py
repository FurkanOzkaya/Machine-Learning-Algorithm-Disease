import numpy as np
import sqlite3

dosya =open("kidney.txt","r")
veri=dosya.readline()
liste=veri.split(";")

### VERİTABANI OLUSTURMA
con = sqlite3.connect("kidneydisease.db")
cursor = con.cursor()
print(sqlite3.version)
### VERİTABANI OLUSTURMA


### TABLO OLUSTURMA
def tabloolustur():
    con.execute("DROP TABLE  IF EXISTS kidney")
    con.commit()
    con.execute("CREATE TABLE IF NOT EXISTS kidney(Yas TEXT, Kan_Basinci TEXT , Ozgun_agirlik TEXT , Albumin TEXT ,Seker TEXT , Kirmizi_Kan TEXT, Irin_Hucresi TEXT,Irin_Hucresi_Kumesi TEXT, Bakteri TEXT ,Kan_Sekeri TEXT ,Kan_ure_miktari TEXT ,Serum_Kreatinin TEXT ,Sodyum TEXT, Potasyum TEXT , Hemoglabin TEXT, Paketlenmis_Hucre TEXT, Beyaz_kan_sayisi TEXT ,Kirmizi_kan_sayisi TEXT, Hiper_Tansiyon TEXT ,Diyabet TEXT,Koroner_arter_hastaligi TEXT ,Istah TEXT, Odem TEXT ,Anemi TEXT,Sonuc TEXT)")
    con.commit()
    con.close()
tabloolustur()
### TABLO OLUSTURMA


#####  VERİ DÜZENLEME
while True:
    veri=dosya.readline()
    if veri == '':
        break
    else:
        liste=veri.split(";")
        for j in liste:
            if (j == 'normal' or j == "present" or j == "yes" or j == "good" or j=="yes" or j == "ckd\n"):
                a = liste.index(j)
                liste[a] = 1
            elif (j == 'abnormal' or j == "notpresent" or j == "no" or j == "poor" or j=="no" or j == "notckd\n"):
                a = liste.index(j)
                liste[a] = 0
        con = sqlite3.connect("kidneydisease.db")
        con.execute("INSERT INTO kidney(Yas, Kan_Basinci , Ozgun_agirlik , Albumin  ,Seker  , Kirmizi_Kan , Irin_Hucresi ,Irin_Hucresi_Kumesi, Bakteri  ,Kan_Sekeri  ,Kan_ure_miktari  ,Serum_Kreatinin  ,Sodyum , Potasyum  , Hemoglabin , Paketlenmis_Hucre , Beyaz_kan_sayisi  ,Kirmizi_kan_sayisi , Hiper_Tansiyon  ,Diyabet ,Koroner_arter_hastaligi  ,Istah , Odem  ,Anemi ,Sonuc ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",liste)
        con.commit()
#####  VERİ DÜZENLEME



dosya2 =open("Diabetic.txt","r")
veri2=dosya2.readline()
liste2=veri2.split(",")



### VERİTABANI OLUSTURMA
con2 = sqlite3.connect("diabeticretinopathy.db")
cursor2 = con2.cursor()
print(sqlite3.version)
### VERİTABANI OLUSTURMA


### TABLO OLUSTURMA
def tabloolustur2():
    con2.execute("DROP TABLE  IF EXISTS diabeticretinopathy")
    con2.commit()
    con2.execute("CREATE TABLE IF NOT EXISTS diabeticretinopathy(Kalite TEXT,On_tarama TEXT,MA_a TEXT,MA_b TEXT, MA_c TEXT,MA_d TEXT,MA_e TEXT,MA_f TEXT,Eksuda1 TEXT,Eksuda2 TEXT,Eksuda3 TEXT,Eksuda4 TEXT,Eksuda5 TEXT,Eksuda6 TEXT,Eksuda7 TEXT,Eksuda8 TEXT,Goz_oklid TEXT,Optik_disk_capı TEXT,AM_FM TEXT,Sonuc TEXT)")
    con2.commit()
    con2.close()
tabloolustur2()
### TABLO OLUSTURMA


#####  VERİ DÜZENLEME
while True:
    veri2=dosya2.readline()
    if veri2 == '':
        break
    else:
        liste2=veri2.split(",")
        for j in liste2:
            if (j == 'normal' or j == "present" or j == "yes" or j == "good" or j=="yes" or j == "1\n"):
                a = liste2.index(j)
                liste2[a] = 1
            elif (j == 'abnormal' or j == "notpresent" or j == "no" or j == "poor" or j=="no" or j == "0\n"):
                a = liste2.index(j)
                liste2[a] = 0
        con2 = sqlite3.connect("diabeticretinopathy.db")
        #print(liste2)
        con2.execute("INSERT INTO diabeticretinopathy(Kalite,On_tarama,MA_a,MA_b, MA_c,MA_d,MA_e,MA_f,Eksuda1,Eksuda2,Eksuda3,Eksuda4,Eksuda5,Eksuda6,Eksuda7,Eksuda8,Goz_oklid,Optik_disk_capı,AM_FM,Sonuc) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",liste2)
        con2.commit()
#####  VERİ DÜZENLEME

print("Başarılı bir şekilde veritabanı oluşturuldu")


