# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anaekran.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 740, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 120, 790, 431))
        self.tableWidget.setMaximumSize(QtCore.QSize(790, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu_yonetim = QtWidgets.QMenu(self.menubar)
        self.menu_yonetim.setObjectName("menu_yonetim")
        self.menu_uyelik_islemleri = QtWidgets.QMenu(self.menubar)
        self.menu_uyelik_islemleri.setObjectName("menu_uyelik_islemleri")
        self.menu_egitmen_islemleri = QtWidgets.QMenu(self.menubar)
        self.menu_egitmen_islemleri.setObjectName("menu_egitmen_islemleri")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_yonetici_ekle = QtWidgets.QAction(MainWindow)
        self.action_yonetici_ekle.setObjectName("action_yonetici_ekle")
        self.action_yonetici_guncelle = QtWidgets.QAction(MainWindow)
        self.action_yonetici_guncelle.setObjectName("action_yonetici_guncelle")
        self.action_cikis = QtWidgets.QAction(MainWindow)
        self.action_cikis.setObjectName("action_cikis")
        self.action_uye_ekle = QtWidgets.QAction(MainWindow)
        self.action_uye_ekle.setObjectName("action_uye_ekle")
        self.action_uye_guncelle_sil = QtWidgets.QAction(MainWindow)
        self.action_uye_guncelle_sil.setObjectName("action_uye_guncelle_sil")
        self.action_egitmen_ekle = QtWidgets.QAction(MainWindow)
        self.action_egitmen_ekle.setObjectName("action_egitmen_ekle")
        self.action_egitmen_guncelle_sil = QtWidgets.QAction(MainWindow)
        self.action_egitmen_guncelle_sil.setObjectName("action_egitmen_guncelle_sil")
        self.action_giris = QtWidgets.QAction(MainWindow)
        self.action_giris.setObjectName("action_giris")
        self.menu_yonetim.addAction(self.action_giris)
        self.menu_yonetim.addAction(self.action_yonetici_ekle)
        self.menu_yonetim.addAction(self.action_yonetici_guncelle)
        self.menu_yonetim.addAction(self.action_cikis)
        self.menu_uyelik_islemleri.addAction(self.action_uye_ekle)
        self.menu_uyelik_islemleri.addAction(self.action_uye_guncelle_sil)
        self.menu_egitmen_islemleri.addAction(self.action_egitmen_ekle)
        self.menu_egitmen_islemleri.addAction(self.action_egitmen_guncelle_sil)
        self.menubar.addAction(self.menu_yonetim.menuAction())
        self.menubar.addAction(self.menu_uyelik_islemleri.menuAction())
        self.menubar.addAction(self.menu_egitmen_islemleri.menuAction())

        self.retranslateUi(MainWindow)
        self.action_cikis.triggered.connect(MainWindow.close)
        self.action_giris.triggered.connect(MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spor Salonu Otomasyonu"))
        self.label.setText(_translate("MainWindow", "KILIÇOĞLU Spor Salonuna Hoş Geldiniz"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Üye Adı Soyadı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Üyelik Bitiş Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kalan Gün"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Eğitmen"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Üye Notu"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Üyelik Durumu"))
        self.menu_yonetim.setTitle(_translate("MainWindow", "Yönetim"))
        self.menu_uyelik_islemleri.setTitle(_translate("MainWindow", "Üyelik İşlemleri"))
        self.menu_egitmen_islemleri.setTitle(_translate("MainWindow", "Eğitmen İşlemleri"))
        self.action_yonetici_ekle.setText(_translate("MainWindow", "Yönetici Ekle"))
        self.action_yonetici_guncelle.setText(_translate("MainWindow", "Yönetici Güncelle - Sil"))
        self.action_cikis.setText(_translate("MainWindow", "Çıkış"))
        self.action_uye_ekle.setText(_translate("MainWindow", "Üye Ekle"))
        self.action_uye_guncelle_sil.setText(_translate("MainWindow", "Üye Güncelle / Sil"))
        self.action_egitmen_ekle.setText(_translate("MainWindow", "Eğitmen Ekle"))
        self.action_egitmen_guncelle_sil.setText(_translate("MainWindow", "Eğitmen Güncelle / Sil"))
        self.action_giris.setText(_translate("MainWindow", "Giriş"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

