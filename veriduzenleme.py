import  sqlite3


dosya =open("kidney.txt","r")
veri=dosya.readline()
liste1=veri.split(";")
#print(liste1)

def veriduzenle(i):
        con = sqlite3.connect("kidneydisease.db")
        cursor = con.cursor()
        cursor.execute("SELECT %s FROM kidney " % i)
        #print(cursor.fetchall())
        liste=cursor.fetchall()
        #print(i,liste)
        sayac=0
        a = 0
        for j in liste:
            temp = j[0]
            if temp != "?":
                sayac=sayac+1
                #print(temp)
                temp=float(temp)
                a=a+temp
        b=sayac
        a=a/b
        #print(type(a))
        #print(a)
        #print(i)
        a=str(a)
        con.execute("UPDATE  kidney  SET {}={}  WHERE {} = '?' ".format(i,str(a),i))
        con.commit()
        con.close()
        #print(i)


liste1.pop()
for i in liste1:
        veriduzenle(i)
        
print("Başarılı bir şekilde veritabanı düzenlendi")



