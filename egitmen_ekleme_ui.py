# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'egitmen_ekleme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 110, 531, 200))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.yNeticiAdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yNeticiAdLabel.setObjectName("yNeticiAdLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.yNeticiAdLabel)
        self.egitmen_adi_soyadi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.egitmen_adi_soyadi.setObjectName("egitmen_adi_soyadi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.egitmen_adi_soyadi)
        self.yNeticiTCNoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yNeticiTCNoLabel.setObjectName("yNeticiTCNoLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.yNeticiTCNoLabel)
        self.egitmen_tc = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.egitmen_tc.setObjectName("egitmen_tc")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.egitmen_tc)
        self.yNeticiIfreLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yNeticiIfreLabel.setObjectName("yNeticiIfreLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.yNeticiIfreLabel)
        self.egitmen_sifre = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.egitmen_sifre.setObjectName("egitmen_sifre")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.egitmen_sifre)
        self.eItmenTelefonLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.eItmenTelefonLabel.setObjectName("eItmenTelefonLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.eItmenTelefonLabel)
        self.egitmen_tel = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.egitmen_tel.setObjectName("egitmen_tel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.egitmen_tel)
        self.eItmenAdresLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.eItmenAdresLabel.setObjectName("eItmenAdresLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.eItmenAdresLabel)
        self.egitmen_adres = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.egitmen_adres.setObjectName("egitmen_adres")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.egitmen_adres)
        self.yNeticiDurumuLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yNeticiDurumuLabel.setObjectName("yNeticiDurumuLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.yNeticiDurumuLabel)
        self.egitmen_durum = QtWidgets.QComboBox(self.formLayoutWidget)
        self.egitmen_durum.setObjectName("egitmen_durum")
        self.egitmen_durum.addItem("")
        self.egitmen_durum.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.egitmen_durum)
        self.yelikBitiTarihiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yelikBitiTarihiLabel.setText("")
        self.yelikBitiTarihiLabel.setObjectName("yelikBitiTarihiLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.yelikBitiTarihiLabel)
        self.egitmen_ekle_btn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.egitmen_ekle_btn.setObjectName("egitmen_ekle_btn")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.egitmen_ekle_btn)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 740, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Eğitmen Ekleme Ekranı"))
        self.yNeticiAdLabel.setText(_translate("Form", "Eğitmen Adı Soyadı"))
        self.yNeticiTCNoLabel.setText(_translate("Form", "Eğitmen T.C. No "))
        self.yNeticiIfreLabel.setText(_translate("Form", "Eğitmen Şifre"))
        self.eItmenTelefonLabel.setText(_translate("Form", "Eğitmen Telefon"))
        self.eItmenAdresLabel.setText(_translate("Form", "Eğitmen Adres"))
        self.yNeticiDurumuLabel.setText(_translate("Form", "Eğitmen Durumu"))
        self.egitmen_durum.setItemText(0, _translate("Form", "Aktif"))
        self.egitmen_durum.setItemText(1, _translate("Form", "Pasif"))
        self.egitmen_ekle_btn.setText(_translate("Form", "Eğitmeni Ekle"))
        self.label.setText(_translate("Form", "Yeni Eğitmen Ekleme Formu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

