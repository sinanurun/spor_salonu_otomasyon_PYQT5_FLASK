from egitmen_ekleme_ui import Ui_Form as Egitmen_Ekleme_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from PyQt5 import QtCore
import sys

class Egitmen_Ekleme(QWidget,Egitmen_Ekleme_Ui):
    def __init__(self):
        super(Egitmen_Ekleme,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.egitmen_ekle_btn.clicked.connect(self.fegitmen_ekle)

    # Eğitmen ekleme işlemi fonksiyonu
    def fegitmen_ekle(self):
        e_adi_soyadi = self.egitmen_adi_soyadi.text()
        e_tc = self.egitmen_tc.text()
        e_sifre = self.egitmen_sifre.text()
        e_telefon = self.egitmen_tel.text()
        e_adres = self.egitmen_adres.text()
        e_durum = self.egitmen_durum.currentIndex()

        # eğitmeni veri tabanına ekleme işlemi kontrol ve dönütü
        try:
            egitmen = Egitmen(egitmen_adi_soyadi=e_adi_soyadi,egitmen_tc=e_tc,
                              egitmen_sifre=e_sifre,egitmen_tel=e_telefon,egitmen_adres=e_adres,
                              egitmen_durum=e_durum)
            session.add(egitmen)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Eğitmen Ekleme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Eğitmen Ekleme Hatalı")
            dialog.show()
