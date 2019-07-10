import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import sqlite3
from sklearn.tree import DecisionTreeClassifier


kidneybasarikneighbors3 = 0
kidneybasarikneighbors5 = 0
kidneybasarikneighbors7 = 0
kidneybasarinaive = 0
kidneybasaridecision = 0
diabeticbasarikneighbors3=0
diabeticbasarikneighbors5=0
diabeticbasarikneighbors7=0
diabeticbasarinaive=0
diabeticbasaridecision =0



def makineogrenmesi(gelenveritabanı,ayırma):
    con = sqlite3.connect("kidneydisease.db")
    cursor = con.cursor()

    gelenveri=pd.read_sql("select * from kidney",con)
    gelenveri=gelenveri.drop(["Yas"],axis=1)
    #print(gelenveri)


    y=np.array(gelenveri.Sonuc)
    x=np.array(gelenveri.drop(["Sonuc"],axis=1))
    #print((y))
    #print(x)



    kidneykneighbors3=KNeighborsClassifier(n_neighbors=3)
    kidneykneighbors5=KNeighborsClassifier(n_neighbors=5)
    kidneykneighbors7=KNeighborsClassifier(n_neighbors=7)
    kidneynaive = GaussianNB()
    kidneydecision= DecisionTreeClassifier()


    X_train,X_test,y_train,y_test=cross_validation.train_test_split(x,y,train_size=ayırma)


    kidneykneighbors3.fit(X_train,y_train)              #knearest için
    kidneykneighbors5.fit(X_train,y_train)
    kidneykneighbors7.fit(X_train,y_train)
    kidneynaive.fit(X_train,y_train)         #naive içim
    kidneydecision.fit(X_train,y_train)       #desicion için



    kidneybasarikneighbors3=kidneykneighbors3.score(X_test,y_test)
    kidneybasarikneighbors5=kidneykneighbors5.score(X_test,y_test)
    kidneybasarikneighbors7=kidneykneighbors7.score(X_test,y_test)
    kidneybasarinaive=kidneynaive.score(X_test,y_test)
    kidneybasaridecision =kidneydecision.score(X_test,y_test)


    a=np.array([80,1.020,1,0,1,1,0,0,121,36,1.2,137,4,15.4,44,7800,5.2,1,1,0,1,0,0]).reshape(1,-1)

    kidneyytahminkne3=kidneykneighbors3.predict(X_test)
    kidneyytahminkne5=kidneykneighbors5.predict(X_test)
    kidneyytahminkne7=kidneykneighbors7.predict(X_test)
    kidneyytahminnaive = kidneynaive.predict(X_test)
    kidneyytahmindecision= kidneydecision.predict(X_test)

    print("yüzde",kidneybasarikneighbors3*100,"oranında:")
    print("Kidney Disease kneigbors k sayısı 3=\n",kidneyytahminkne3)

    print("yüzde",kidneybasarikneighbors5*100,"oranında:")
    print("Kidney Disease kneigbors k sayısı 5=\n",kidneyytahminkne5)

    print("yüzde",kidneybasarikneighbors7*100,"oranında:")
    print("Kidney Disease kneigbors k sayısı 7=\n",kidneyytahminkne7)

    print("yüzde",kidneybasarinaive*100,"oranında:")
    print("Kidney Disease naive =\n ",kidneyytahminnaive)


    print("yüzde",kidneybasaridecision*100,"oranında:")
    print("Kidney Disease Decision =\n ",kidneyytahmindecision)



    # VERİLERİN KARSILASTIRILMASI İÇİN VERİTABANINA TABLO OLUŞTURMA
    con = sqlite3.connect("SonuclarKidney.db")
    cursor = con.cursor()

    #for i in range(0,len(y_test)):
     #   print(y_test[i],ytahminkne[i],ytahminnaive[i])


    def sonuctabloolustur():
        con.execute("DROP TABLE  IF EXISTS SonuclarKidney")
        con.commit()
        con.execute("CREATE TABLE IF NOT EXISTS SonuclarKidney(Test_Verisi INTEGER,Kneigbors3 INTEGER,Kneigbors5 INTEGER,Kneigbors7 INTEGER,Naive_Bayes INTEGER,Decision INTEGER)")
        con.commit()
        for i in range(len(y_test)):
            con.execute("INSERT INTO SonuclarKidney(Test_Verisi,Kneigbors3,Kneigbors5,Kneigbors7,Naive_Bayes, Decision) VALUES (?,?,?,?,?,?)",(y_test[i],kidneyytahminkne3[i],kidneyytahminkne5[i],kidneyytahminkne7[i],kidneyytahminnaive[i],kidneyytahmindecision[i]))
            con.commit()
        con.close()

    sonuctabloolustur()
    print("Kidney Disease Sonuclari VeriTabanına kaydedilmiştir")


    #######################################################################################################################################################
     ### 2. VERİSETİ İÇİN ###

    con2 = sqlite3.connect("diabeticretinopathy.db")
    cursor2 = con2.cursor()

    gelenveri2=pd.read_sql("select * from diabeticretinopathy",con2)
    b=np.array(gelenveri2.Sonuc)
    a=np.array(gelenveri2.drop(["Sonuc"],axis=1))


    diabetickneighbors3=KNeighborsClassifier(n_neighbors=3)
    diabetickneighbors5=KNeighborsClassifier(n_neighbors=5)
    diabetickneighbors7=KNeighborsClassifier(n_neighbors=7)
    diabeticnaive= GaussianNB()
    diabeticdecision= DecisionTreeClassifier()


    X_train2,X_test2,y_train2,y_test2=cross_validation.train_test_split(a,b,train_size=ayırma)

    diabetickneighbors3.fit(X_train2,y_train2)              #knearest için
    diabetickneighbors5.fit(X_train2,y_train2)
    diabetickneighbors7.fit(X_train2,y_train2)
    diabeticnaive.fit(X_train2,y_train2)         #naive içim
    diabeticdecision.fit(X_train2,y_train2)      #desicion için


    diabeticbasarikneighbors3=diabetickneighbors3.score(X_test2,y_test2)
    diabeticbasarikneighbors5=diabetickneighbors5.score(X_test2,y_test2)
    diabeticbasarikneighbors7=diabetickneighbors7.score(X_test2,y_test2)
    diabeticbasarinaive=diabeticnaive.score(X_test2,y_test2)
    diabeticbasaridecision =diabeticdecision.score(X_test2,y_test2)


    diabeticytahminkne3=diabetickneighbors3.predict(X_test2)
    diabeticytahminkne5=diabetickneighbors3.predict(X_test2)
    diabeticytahminkne7=diabetickneighbors3.predict(X_test2)
    diabeticytahminnaive = diabeticnaive.predict(X_test2)
    diabeticytahmindecision= diabeticdecision.predict(X_test2)


    print("yüzde",diabeticbasarikneighbors3*100,"oranında:")
    print("Diabetic Retinopathy kneigbors=\n",diabeticytahminkne3)

    print("yüzde",diabeticbasarikneighbors5*100,"oranında:")
    print("Diabetic Retinopathy kneigbors=\n",diabeticytahminkne5)

    print("yüzde",diabeticbasarikneighbors7*100,"oranında:")
    print("Diabetic Retinopathy kneigbors=\n",diabeticytahminkne7)

    print("yüzde",diabeticbasarinaive*100,"oranında:")
    print("Diabetic Retinopathy  naive =\n ",diabeticytahminnaive)


    print("yüzde",diabeticbasaridecision*100,"oranında:")
    print("Diabetic Retinopathy  Decision =\n ",diabeticytahmindecision)


    # VERİLERİN KARSILASTIRILMASI İÇİN VERİTABANINA TABLO OLUŞTURMA
    con2 = sqlite3.connect("SonuclarDiabetic.db")
    cursor2 = con2.cursor()

    #for i in range(0,len(y_test2)):
    #    print(y_test2[i],ytahminkne2[i],ytahminnaive2[i],ytahmindecision2[i])


    def sonuctabloolustur2():
        con2.execute("DROP TABLE  IF EXISTS SonuclarDiabetic")
        con2.commit()
        con2.execute("CREATE TABLE IF NOT EXISTS SonuclarDiabetic(Test_Verisi INTEGER,Kneigbors3 INTEGER,Kneigbors5 INTEGER,Kneigbors7 INTEGER,Naive_Bayes INTEGER,Decision INTEGER)")
        con2.commit()
        for i in range(len(y_test2)):
            con2.execute("INSERT INTO SonuclarDiabetic(Test_Verisi,Kneigbors3,Kneigbors5,Kneigbors7,Naive_Bayes, Decision) VALUES (?,?,?,?,?,?)",(y_test2[i],diabeticytahminkne3[i],diabeticytahminkne5[i],diabeticytahminkne7[i],diabeticytahminnaive[i],diabeticytahmindecision[i]))
            con2.commit()
        con2.close()

    sonuctabloolustur2()

    print("Diabetic Retinopathy Sonuclari VeriTabanına kaydedilmiştir")

    if gelenveritabanı == "kidney":
        #print(kidneybasarikneighbors3, kidneybasarikneighbors5, kidneybasarikneighbors7, kidneybasarinaive, kidneybasaridecision)
        return kidneybasarikneighbors3, kidneybasarikneighbors5, kidneybasarikneighbors7, kidneybasarinaive, kidneybasaridecision
    elif gelenveritabanı== "diabeticretinopathy":
        return diabeticbasarikneighbors3, diabeticbasarikneighbors5, diabeticbasarikneighbors7, diabeticbasarinaive, diabeticbasaridecision


#     başarılistesi=[kidneybasarikneighbors3, kidneybasarikneighbors5, kidneybasarikneighbors7, kidneybasarinaive, kidneybasaridecision]
#     isimler = ("Kneigbors3", "Kneigbors5", "Kneigbors7", "Naive_Bayes", "Decision")
#     for i in başarılistesi:
#         a=başarılistesi.index(i)
#         başarılistesi[a]=i*100
#     ydeger = np.arange(len(isimler))
#     plt.bar([0,1,2,3,4], başarılistesi)
#     plt.legend()
#     plt.xticks(ydeger, isimler)
#     plt.ylabel("Basarı yüzdesi")
#     plt.xlabel("Algoritma")
#     plt.title("Başarı Grafiği")
#     plt.show()
#
# makineogrenmesi("SonuclarKidney.db")

def veritabanıokuma(veritabanı, tabloadi, gösterilecekler):

    try:
        con = sqlite3.connect(veritabanı)
        cursor=con.cursor()
    except:
        print("hata olustu")
    k=0
    veri=""
    print("veritabanıokuma içinde",veritabanı,tabloadi,gösterilecekler)
    gelenler=gösterilecekler
    for i in gelenler:
        k=k+1
        print(k,i)
    #print("gelenler"+gelenler[0])
    if k==0:
        a="select Test_Verisi from "+tabloadi
        #print(a)
        cursor.execute(a)
        veri=cursor.fetchall()
        return veri
    if k==1:
        a="select Test_Verisi ,"+str(gelenler[0])+" from "+tabloadi
        cursor.execute(a)
        veri=cursor.fetchall()
        #veri=str(cursor.fetchall())
        #print(type(veri))
        #oku=con.execute(a)
        #print(oku.fetchall())
        #print(veri)
        return veri

    elif k==2:
        a = "select Test_Verisi ," + str(gelenler[0])+","+str(gelenler[1]) + " from " + tabloadi
        print(a)
        cursor.execute(a)
        #print(cursor.fetchall())
        veri = cursor.fetchall()
        return veri
        #oku=con.execute(a)
        #print(oku.fetchall())
    elif k==3:
        a = "select Test_Verisi ," + str(gelenler[0]) + "," + str(gelenler[1])+","+gelenler[2] + " from " + tabloadi
        cursor.execute(a)
        veri = cursor.fetchall()
        return veri
        #oku=con.execute(a)
        #print(oku.fetchall())
    elif k==4:
        a = "select Test_Verisi ," + str(gelenler[0]) + "," + str(gelenler[1]) + "," + gelenler[2]+","+gelenler[3] + " from " + tabloadi
        cursor.execute(a)
        veri = cursor.fetchall()
        return veri
        #oku=con.execute(a)
        #print(oku.fetchall())
    elif k==5:
        a = "select Test_Verisi ," + str(gelenler[0]) + "," + str(gelenler[1]) + "," + gelenler[2] + "," + gelenler[3]+","+gelenler[4] + " from " + tabloadi
        cursor.execute(a)
        veri = cursor.fetchall()
        return veri
        #oku=con.execute(a)
        #print(oku.fetchall())
    else:
        print("Bir hata oluştu")



gelenveri=veritabanıokuma("SonuclarKidney.db","SonuclarKidney",['Kneigbors3'])
print("makineögrenmesi##",gelenveri)






#pencere = Tk()
#
# cerceve1= Frame(pencere)
# cerceve1.pack(side =RIGHT)
#
# cerceve2= Frame(pencere)
# cerceve1.pack()
#
# cerceve3= Frame(pencere)
# cerceve1.pack(side =LEFT)
#
# veritabanı=StringVar(pencere)
# veritabanları={"Kidney Disease","Diabetic Disease"}
# veritabanısecim=OptionMenu(cerceve1,veritabanı,*veritabanları)
# veritabanı.set("Kidney Disease")
# veritabanısecim.pack(side=TOP)


#pencere.mainloop()
# VERİLERİN KARSILASTIRILMASI İÇİN VERİTABANINA TABLO OLUŞTURMA




#print("kneigbors",kneighbors.predict(a)[0]," naive", naive.predict(a)[0])


#basari=accuracy_score(y,ytahmin,normalize=True,sample_weight=None)
#print(basari)


#cursor.execute("select %s from kidney" % 0)
#con.commit()
#gelenveri=cursor.fetchall()
#sutunsayısı=baslıklar.__len__()
#satırsayısı =gelenveri.__len__()
##print(satırsayısı)
#print(sutunsayısı)
#gelenveri=""
#liste1=np.zeros(shape=(sutunsayısı,satırsayısı))

#for i in baslıklar:
    #sayac=baslıklar.index(i)
    #cursor.execute("select %s from kidney" % i)
    #con.commit()
    #gelenveri=cursor.fetchall()
    ##print(gelenveri)
    #for j in gelenveri:
        #k=j[0]
        ##print(k)
        #index=gelenveri.index(j)
        ##liste1[sayac][index]=k
        #print(liste1)
        #np.append(liste1,k,[sayac,index])
    #sayac=sayac+1


#y=liste1[sutunsayısı-1]
#np.delete(liste1,sutunsayısı-1)
#x=liste1
#print("x in yazılması",x[0])
#print("y nin yazılması",y)