# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randevu_ekle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 781, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(250, 50, 200, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.eItmenSeInizLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.eItmenSeInizLabel.setObjectName("eItmenSeInizLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.eItmenSeInizLabel)
        self.egitmen = QtWidgets.QComboBox(self.formLayoutWidget)
        self.egitmen.setObjectName("egitmen")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.egitmen)
        self.tarihSeInizLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.tarihSeInizLabel.setObjectName("tarihSeInizLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tarihSeInizLabel)
        self.randevu_tarihi = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.randevu_tarihi.setCalendarPopup(True)
        self.randevu_tarihi.setObjectName("randevu_tarihi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.randevu_tarihi)
        self.randevuSaatAralLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.randevuSaatAralLabel.setObjectName("randevuSaatAralLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.randevuSaatAralLabel)
        self.randevu_araligi = QtWidgets.QComboBox(self.formLayoutWidget)
        self.randevu_araligi.setObjectName("randevu_araligi")
        self.randevu_araligi.addItem("")
        self.randevu_araligi.addItem("")
        self.randevu_araligi.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.randevu_araligi)
        self.randevuDurumuLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.randevuDurumuLabel.setObjectName("randevuDurumuLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.randevuDurumuLabel)
        self.randevu_durumu = QtWidgets.QComboBox(self.formLayoutWidget)
        self.randevu_durumu.setObjectName("randevu_durumu")
        self.randevu_durumu.addItem("")
        self.randevu_durumu.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.randevu_durumu)
        self.randevu_ekle_btn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.randevu_ekle_btn.setObjectName("randevu_ekle_btn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.randevu_ekle_btn)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 790, 401))
        self.tableWidget.setMaximumSize(QtCore.QSize(790, 431))
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Eğitmen Randevu Ekleme Ekranı"))
        self.label.setText(_translate("Form", "Eğitmen Randevu Ekleme Ekranına Hoş Geldiniz"))
        self.eItmenSeInizLabel.setText(_translate("Form", "Eğitmen Seçiniz"))
        self.tarihSeInizLabel.setText(_translate("Form", "Tarih Seçiniz"))
        self.randevuSaatAralLabel.setText(_translate("Form", "Randevu Saat Aralığı"))
        self.randevu_araligi.setItemText(0, _translate("Form", "08:00 - 17:00"))
        self.randevu_araligi.setItemText(1, _translate("Form", "14:00 - 23:00"))
        self.randevu_araligi.setItemText(2, _translate("Form", "15:00 - 24:00"))
        self.randevuDurumuLabel.setText(_translate("Form", "Randevu Durumu"))
        self.randevu_durumu.setItemText(0, _translate("Form", "Aktif"))
        self.randevu_durumu.setItemText(1, _translate("Form", "Pasif"))
        self.randevu_ekle_btn.setText(_translate("Form", "Randevu ekle"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Eğitmen Adı Soyadı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Randevu Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Saat Aralığı"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Randevu 1"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Randevu 2"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Randevu 3"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Randevu 4"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Randevu 5"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Randevu 6"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Randevu 7"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Randevu 8"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Sil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
