from anaekran_ui import Ui_MainWindow as Anapencere_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from yonetici_ekleme import Yonetici_Ekleme
from yonetici_guncelle_sil import Yonetici_Gs
from uye_ekleme import Uye_Ekleme
from uye_guncelle_sil import Uye_Gs
from egitmen_guncelle_sil import Egitmen_Gs
from egitmen_ekleme import Egitmen_Ekleme
from randevu_ekleme import Randevu_Ekleme

# ana ekran girişi için
class Anaekran(QMainWindow, Anapencere_Ui):
    def __init__(self):
        super(Anaekran,self).__init__()
        self.fgiris()

    # menülerin aktivasyonu için
    def fgiris(self):
        self.setupUi(self)
        self.action_giris.triggered.connect(self.fgiris)
        self.action_yonetici_ekle.triggered.connect(self.fyonetici_ekle)
        self.action_yonetici_guncelle.triggered.connect(self.fyonetici_guncelle_sil)
        self.action_uye_ekle.triggered.connect(self.fuye_ekle)
        self.action_uye_guncelle_sil.triggered.connect(self.fuye_guncelle_sil)
        self.action_egitmen_ekle.triggered.connect(self.fegitmen_ekle)
        self.action_egitmen_guncelle_sil.triggered.connect(self.fegitmen_guncelle_sil)
        self.actionRandevu_Ekle.triggered.connect(self.frandevu_ekle)

        self.ftablo()

    def ftablo(self):
        uye_listesi =session.query(Uye).filter(Uye.uye_durum == 0).all()
        uye_sayisi = session.query(Uye).filter(Uye.uye_durum == 0).count()


        self.tableWidget.setRowCount(uye_sayisi)

        for uye, y in zip(uye_listesi,range(uye_sayisi)):
            self.tableWidget.setItem(y,0,QTableWidgetItem(uye.uye_adi_soyadi))
            self.tableWidget.setItem(y, 1, QTableWidgetItem(uye.uye_tarihi))
            self.tableWidget.setItem(y, 2, QTableWidgetItem(uye.uye_tel))
            self.tableWidget.setItem(y, 3, QTableWidgetItem(uye.egitmenid.egitmen_adi_soyadi))
            self.tableWidget.setItem(y, 4, QTableWidgetItem(uye.uye_notu))
            self.tableWidget.setItem(y, 5, QTableWidgetItem("Aktif"))



    # yönetici ekleme penceresinin getirilmesi için
    def fyonetici_ekle(self):
        self.setCentralWidget(Yonetici_Ekleme())

    # yonetici güncelleme ve silme işlemleri için
    def fyonetici_guncelle_sil(self):
        self.setCentralWidget(Yonetici_Gs())

    # üye ekleme penceresinin getirilmesi için
    def fuye_ekle(self):
        self.setCentralWidget(Uye_Ekleme())

    # uye güncelleme ve silme işlemleri için
    def fuye_guncelle_sil(self):
        self.setCentralWidget(Uye_Gs())

    # eğitmen ekleme penceresinin getirilmesi için
    def fegitmen_ekle(self):
        self.setCentralWidget(Egitmen_Ekleme())

    # egitmen güncelleme ve silme işlemleri için
    def fegitmen_guncelle_sil(self):
        self.setCentralWidget(Egitmen_Gs())

    def frandevu_ekle(self):
        self.setCentralWidget(Randevu_Ekleme())