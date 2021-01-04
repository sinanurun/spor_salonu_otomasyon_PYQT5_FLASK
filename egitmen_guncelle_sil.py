from egitmen_guncelle_sil_ui import Ui_Form as Egitmen_Gs_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *

class Egitmen_Gs(QWidget,Egitmen_Gs_Ui):
    def __init__(self):
        super(Egitmen_Gs,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.ftablo()

    def ftablo(self):
        self.sozluk = {}
        self.egitmenler = session.query(Egitmen).all()
        self.tableWidget.setRowCount(0)
        for egitmen, sira in zip(self.egitmenler, range(len(self.egitmenler))):
            self.tableWidget.insertRow(sira)
            self.tableWidget.setItem(sira, 0, QTableWidgetItem(egitmen.egitmen_adi_soyadi))
            self.tableWidget.setItem(sira, 1, QTableWidgetItem(egitmen.egitmen_tc))
            self.tableWidget.setItem(sira, 2, QTableWidgetItem(egitmen.egitmen_sifre))
            self.tableWidget.setItem(sira, 3, QTableWidgetItem(egitmen.egitmen_tel))
            self.tableWidget.setItem(sira, 4, QTableWidgetItem(egitmen.egitmen_adres))
            dcombo = QComboBox(self)
            self.durum = ["Aktif", "Pasif"]
            for x in self.durum:
                dcombo.addItem(x)
            dcombo.setObjectName("d" + str(egitmen.egitmen_durum))
            dcombo.setCurrentIndex(egitmen.egitmen_durum)

            self.tableWidget.setCellWidget(sira, 5, dcombo)

            guncelle = QPushButton(self)
            guncelle.setObjectName("g" + str(egitmen.egitmen_id))
            guncelle.setText("Güncelle")
            guncelle.clicked.connect(self.fguncelle)

            self.tableWidget.setCellWidget(sira, 6, guncelle)

            sil = QPushButton(self)
            sil.setObjectName("s" + str(egitmen.egitmen_id))
            sil.setText("Sil")
            sil.clicked.connect(self.fsil)

            self.tableWidget.setCellWidget(sira, 7, sil)
            self.sozluk[egitmen.egitmen_id] = [sira, dcombo]

    def fguncelle(self):
        gelen = self.sender()
        gelen = int(gelen.objectName()[1:])
        sira = self.sozluk[gelen][0]
        durum = self.sozluk[gelen][1]
        print(sira, durum.currentIndex(), durum.objectName())
        try:
            session.query(Egitmen).filter(Egitmen.egitmen_id == gelen).update({
                Egitmen.egitmen_adi_soyadi: self.tableWidget.item(sira, 0).text(),
                Egitmen.egitmen_tc: self.tableWidget.item(sira, 1).text(),
                Egitmen.egitmen_sifre: self.tableWidget.item(sira, 2).text(),
                Egitmen.egitmen_tel: self.tableWidget.item(sira, 3).text(),
                Egitmen.egitmen_adres: self.tableWidget.item(sira, 4).text(),
                Egitmen.egitmen_durum: durum.currentIndex()
            }, synchronize_session=False)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarısız")
            dialog.show()
        self.ftablo()

    def fsil(self):
        try:
            gelen = self.sender()
            gelen = int(gelen.objectName()[1:])
            session.query(Egitmen).filter(Egitmen.egitmen_id == gelen).delete()
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarısız")
            dialog.show()
        self.ftablo()
