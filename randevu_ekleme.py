from randevu_ekle_ui import Ui_Form as Randevu_Ekleme_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from PyQt5 import QtCore
import sys

class Randevu_Ekleme(QWidget,Randevu_Ekleme_Ui):
    def __init__(self):
        super(Randevu_Ekleme,self).__init__()
        self.fbaslangic()
        self.ftablo()

    def fbaslangic(self):
        self.setupUi(self)
        self.randevu_tarihi.setDateTime(QtCore.QDateTime.currentDateTime())
        egitmen_listesi = session.query(Egitmen).filter(Egitmen.egitmen_durum == 0).all()
        self.egitmen_bilgisi = {}
        for x, y in zip(egitmen_listesi,range(len(egitmen_listesi))):
            self.egitmen.addItem(x.egitmen_adi_soyadi)
            self.egitmen_bilgisi[y] = x.egitmen_id
        self.randevu_ekle_btn.clicked.connect(self.frandevu_ekle)

    # randevu ekleme işlemi fonksiyonu
    def frandevu_ekle(self):
        pass
        r_aralik = self.randevu_araligi.currentIndex()
        r_durum = self.randevu_durumu.currentIndex()
        r_egitmen = self.egitmen_bilgisi[self.egitmen.currentIndex()]
        r_tarih = datetime.strptime(self.randevu_tarihi.text(), '%d.%m.%Y').date()

        randevu = Randevu(randevu_araligi=r_aralik, egitmen_id=r_egitmen,
                          randevu_durum=r_durum, randevu_tarihi=r_tarih)
        session.add(randevu)
        session.commit()
        dialog = QMessageBox(self)
        islem = QLabel(dialog, text="Randevu Ekleme Başarılı")
        dialog.show()

        # randevu veri tabanına ekleme işlemi kontrol ve dönütü
        try:
            pass
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Randevu Ekleme Hatalı")
            dialog.show()
    def ftablo(self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.sozluk = {}
        self.randevular = session.query(Randevu).filter( Randevu.randevu_durum == 0).all()
        self.tableWidget.setRowCount(0)
        for randevu, sira in zip(self.randevular, range(len(self.randevular))):
            self.tableWidget.insertRow(sira)
            try:
                self.tableWidget.setItem(sira, 0, QTableWidgetItem(randevu.egitmenid.egitmen_adi_soyadi))
                self.tableWidget.setItem(sira, 1, QTableWidgetItem(str(randevu.randevu_tarihi)))
                saat_araligi = ["08:00 - 17:00","14:00 - 23:00","15:00 - 24:00"]


                self.tableWidget.setItem(sira, 2, QTableWidgetItem(str(saat_araligi[randevu.randevu_araligi])))
                self.tableWidget.setItem(sira, 3, QTableWidgetItem("Boş" if randevu.randevu_saat1 ==0 else randevu.randevuuye1.uye_adi_soyadi))
                self.tableWidget.setItem(sira, 4, QTableWidgetItem("Boş" if randevu.randevu_saat2 ==0 else randevu.randevuuye2.uye_adi_soyadi))
                self.tableWidget.setItem(sira, 5, QTableWidgetItem("Boş" if randevu.randevu_saat3 ==0 else randevu.randevuuye3.uye_adi_soyadi))
                self.tableWidget.setItem(sira, 6, QTableWidgetItem("Boş" if randevu.randevu_saat4 ==0 else randevu.randevuuye4.uye_adi_soyadi))
                self.tableWidget.setItem(sira, 7, QTableWidgetItem("Boş" if randevu.randevu_saat5 ==0 else randevu.randevuuye5.uye_adi_soyadi))
                self.tableWidget.setItem(sira, 8, QTableWidgetItem("Boş" if randevu.randevu_saat6 ==0 else randevu.randevuuye6.uye_adi_soyadi))
                self.tableWidget.setItem(sira, 9, QTableWidgetItem("Boş" if randevu.randevu_saat7 ==0 else randevu.randevuuye7.uye_adi_soyadi))
                self.tableWidget.setItem(sira, 10, QTableWidgetItem("Boş" if randevu.randevu_saat8 ==0 else randevu.randevuuye8.uye_adi_soyadi))

                sil = QPushButton(self)
                sil.setObjectName("s" + str(randevu.randevu_id))
                sil.setText("Sil")
                sil.clicked.connect(self.fsil)

                self.tableWidget.setCellWidget(sira, 11,sil)
            except:
                pass

    def fsil(self):
        try:
            gelen = self.sender()
            gelen = int(gelen.objectName()[1:])
            session.query(Randevu).filter(Randevu.randevu_id == gelen).delete()
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarısız")
            dialog.show()
        self.ftablo()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Randevu_Ekleme()
    pencere.show()
    sys.exit(app.exec_())