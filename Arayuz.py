# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Af.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from  MakineOgrenmesi import veritabanıokuma,makineogrenmesi
import numpy as np
import matplotlib.pyplot as plt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1108, 557)
        Form.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(290, 20, 801, 461))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidget.setObjectName("tableWidget")
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 260, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setCurrentText("Kidney Disease")
        self.comboBox.addItem("Kidney Disease")
        self.comboBox.addItem("Diabetic Retinopathy")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setCurrentText("10")
        self.comboBox_2.addItem("10")
        self.comboBox_2.addItem("9")
        self.comboBox_2.addItem("8")
        self.comboBox_2.addItem("7")
        self.comboBox_2.addItem("6")
        self.comboBox_2.addItem("5")
        self.comboBox_2.addItem("4")
        self.comboBox_2.addItem("3")
        self.comboBox_2.addItem("2")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.Kneigbors3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.Kneigbors3.setObjectName("Kneigbors3")
        self.verticalLayout.addWidget(self.Kneigbors3)
        self.Kneigbors5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.Kneigbors5.setObjectName("Kneigbors5")
        self.verticalLayout.addWidget(self.Kneigbors5)
        self.Kneigbors7 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.Kneigbors7.setObjectName("Kneigbors7")
        self.verticalLayout.addWidget(self.Kneigbors7)
        self.Naive_Bayes = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.Naive_Bayes.setObjectName("Naive_Bayes")
        self.verticalLayout.addWidget(self.Naive_Bayes)
        self.Desicion = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.Desicion.setObjectName("Desicion")
        self.verticalLayout.addWidget(self.Desicion)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Makine = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Makine.setObjectName("Makine")
        self.horizontalLayout.addWidget(self.Makine)
        self.goster = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.goster.setObjectName("goster")
        self.horizontalLayout.addWidget(self.goster)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.bilgi = QtWidgets.QLabel(Form)
        self.bilgi.setGeometry(QtCore.QRect(190, 510, 751, 20))
        self.bilgi.setObjectName("bilgi")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pyhton ile Makine Öğrenmesi"))
        self.label.setText(_translate("Form", "Görmek İstediğiniz Veri Tabanını Seçiniz"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p>Veriyi Kaç Bölüme Ayırmak İstersiniz</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Görmek İstediğiniz Makine Öğrenmesi </p><p>Sonuçlarını Seçiniz</p></body></html>"))
        self.Kneigbors3.setText(_translate("Form", "Kneighborsclassifier3"))
        self.Kneigbors5.setText(_translate("Form", "Kneighborsclassifier5"))
        self.Kneigbors7.setText(_translate("Form", "Kneighborsclassifier7"))
        self.Naive_Bayes.setText(_translate("Form", "Naive Bayes Classifier"))
        self.Desicion.setText(_translate("Form", "Decision Tree"))
        self.Makine.setText(_translate("Form", "Makine Öğrenmesi\n"
"Çalıştır"))
        self.goster.setText(_translate("Form", "Seçilen Algoritmaların\n"
"Sonuçlarını Göster"))
        self.bilgi.setText(_translate("Form", "TextLabel"))

        self.bilgi.setText(_translate("Form", ""))
        ###########################
        self.Makine.clicked.connect(lambda: self.makineogrenmesi())
        #########################
        #####
        self.goster.clicked.connect(lambda: self.veritabanıgoster(self.Kneigbors3.isChecked(),self.Kneigbors5.isChecked(),self.Kneigbors7.isChecked(),self.Naive_Bayes.isChecked(),self.Desicion.isChecked()))
        ####


        #gelenveri=veritabanıokuma("SonuclarKidney.db", "SonuclarKidney", ['Kneigbors3'])
        #print(gelenveri)


    def makineogrenmesi(self):
            gelen_veritabanı = self.comboBox.currentText()
            if gelen_veritabanı=="Kidney Disease":
                gelen_veritabanı="kidney"
            else:
                gelen_veritabanı="diabeticretinopathy"
            #print(gelen_veritabanı)

            gelen_ayırma=self.comboBox_2.currentText()
            ayırma_gönder=0.9
            if gelen_ayırma=="2":
                ayırma_gönder=0.5
            elif gelen_ayırma=="3":
                ayırma_gönder=0.66
            elif gelen_ayırma=="4":
                ayırma_gönder=0.75
            elif gelen_ayırma=="5":
                ayırma_gönder=0.8
            elif gelen_ayırma=="6":
                ayırma_gönder=0.835
            elif gelen_ayırma=="7":
                ayırma_gönder=0.85
            elif gelen_ayırma=="8":
                ayırma_gönder=0.875
            elif gelen_ayırma=="9":
                ayırma_gönder=0.88
            elif gelen_ayırma=="10":
                ayırma_gönder=0.9
            else:
                print("Beklenmeyen bir durum gercekleşti")

            başarılistesi=makineogrenmesi(gelen_veritabanı,ayırma_gönder)
            #print(başarılistesi)
            self.bilgi.setText("Olasılıklar hesaplandı ve Veri Tabanı Yenilendi... Grafik Ekrana yansıtılıyor...")

            isimler = ["Kneighbors3", "Kneighbors5", "Kneighbors7", "Naive_Bayes", "Decision"]
            print(type(başarılistesi))
            print(başarılistesi)
            #for i in başarılistesi:
             #   a = başarılistesi.index(i)
              #  başarılistesi[a] = float(float(i) * float(100))
               # print(başarılistesi)

            a=başarılistesi[0]*100
            b=başarılistesi[1]*100
            c=başarılistesi[2]*100
            d=başarılistesi[3]*100
            e=başarılistesi[4]*100
            print(başarılistesi)
            print(a,b,c,d,e)
            ydeger = np.arange(len(isimler))
            plt.bar([0, 1, 2, 3, 4], [a,b,c,d,e])
            #plt.legend()
            plt.xticks(ydeger, isimler)
            plt.ylabel("Basarı yüzdesi")
            plt.xlabel("Algoritma")
            plt.title("Başarı Grafiği")
            #fig=plt.figure()
            #fig = plt.gcf()
            #plot_url = py.plot_mpl(fig, filename='grafik')
            plt.show()








    def veritabanıgoster(self,Kneigbors3,Kneigbors5,Kneigbors7,Naive_Bayes,Desicion):
            #print("içerde")
            gelen_veritabanı = self.comboBox.currentText()
            veritabanı=gelen_veritabanı
            istenen_veri =[]

            if Kneigbors3==1 or Kneigbors5==1 or Kneigbors7==1 or Naive_Bayes==1 or Desicion==1:
                if Kneigbors3:
                    istenen_veri.append("Kneigbors3")
                if Kneigbors5:
                    istenen_veri.append("Kneigbors5")
                if Kneigbors7:
                    istenen_veri.append("Kneigbors7")
                if Naive_Bayes:
                    istenen_veri.append("Naive_Bayes")
                if Desicion:
                    istenen_veri.append("Decision")
                if gelen_veritabanı == "Kidney Disease":
                    gelen_veritabanı = "SonuclarKidney.db"
                    tablo_adi = "SonuclarKidney"
                else:
                    gelen_veritabanı = "SonuclarDiabetic.db"
                    tablo_adi = "SonuclarDiabetic"
                print(gelen_veritabanı, tablo_adi, istenen_veri)
                a = len(istenen_veri)
                if a == 0:
                    self.bilgi.setText("Yanlıs islem yaptınız Lütfen Seçim Yapınız")
                else:
                    self.bilgi.setText(veritabanı+" Bilgileri Gösteriliyor...")
                    gelenveri = veritabanıokuma(gelen_veritabanı, tablo_adi, istenen_veri)
                    # print(gelenveri)
                # print(gelenveri)

                #####################################################################
                a = "Test_Verisi"
                for i in istenen_veri:
                    a = a + ";" + i
                    # print(a)
                self.tableWidget.clear()
                self.tableWidget.setColumnCount(len(istenen_veri) + 1)
                self.tableWidget.setRowCount(0)
                self.tableWidget.setHorizontalHeaderLabels(a.split(";"))
                self.tableWidget.setRowCount(len(gelenveri))
                _translate = QtCore.QCoreApplication.translate
                for satır_sayısı, satır_data in enumerate(gelenveri):
                    # print(satır_sayısı)
                    for sutun_sayısı, veri in enumerate(satır_data):
                        # print("satır",satır_sayısı,"sutun",sutun_sayısı,"veri=",veri)
                        self.tableWidget.setItem(satır_sayısı, sutun_sayısı, QTableWidgetItem(str(veri)))

                for satır_sayısı, satır_data in enumerate(gelenveri):
                    for sutun_sayısı, veri in enumerate(satır_data):
                        if satır_data[0] == veri:
                            self.tableWidget.item(satır_sayısı, sutun_sayısı).setBackground(QtGui.QColor(139,10,80))
                        else:
                            self.tableWidget.item(satır_sayısı, sutun_sayısı).setBackground(QtGui.QColor(221,160,221))

            else:
                self.bilgi.setText("Yanlıs islem yaptınız Lütfen Seçim Yapınız")



            # self.tableWidget.setItem(0, 0, QTableWidgetItem(str("00")))
            # self.tableWidget.setItem(0, 1, QTableWidgetItem(str("01")))
            # self.tableWidget.setItem(1,0, QTableWidgetItem(str("10")))
            # self.tableWidget.setItem(1, 1, QTableWidgetItem(str("11")))
            # self.tableWidget.setItem(2, 0, QTableWidgetItem(str("20")))
            # self.tableWidget.setItem(2,1,QTableWidgetItem(str("21")))
            # #
            # while i<len(gelenveri):
            #     self.tableWidget.insertRow(i)
            #     for a in gelenveri[i]:
            #         sutun=gelenveri[i].index(a)
            #         self.tableWidget.setItem(i,sutun,QtWidgets.QTableWidgetItem(a))


            #for i in istenen_veri:
             #   self.tableWidget.setHorizontalHeaderItem(i)
            #print(gelenveri[0])
            #for i in gelenveri:
             #   self.tableWidget.insertRow(gelenveri[i])







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


