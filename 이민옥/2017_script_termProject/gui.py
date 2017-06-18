# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Eom Dongyeon\Documents\GitHub\2017-Scripts\엄동연\2017_script_termProject\gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(436, 698)
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 200, 401, 451))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.selectMenuComboBox = QtGui.QComboBox(Dialog)
        self.selectMenuComboBox.setEnabled(True)
        self.selectMenuComboBox.setGeometry(QtCore.QRect(20, 70, 111, 22))
        self.selectMenuComboBox.setAcceptDrops(False)
        self.selectMenuComboBox.setEditable(False)
        self.selectMenuComboBox.setObjectName(_fromUtf8("selectMenuComboBox"))
        self.selectMenuComboBox.addItem(_fromUtf8(""))
        self.selectMenuComboBox.addItem(_fromUtf8(""))
        self.SearchPushButton = QtGui.QPushButton(Dialog)
        self.SearchPushButton.setGeometry(QtCore.QRect(330, 130, 93, 28))
        self.SearchPushButton.setCheckable(True)
        self.SearchPushButton.setObjectName(_fromUtf8("SearchPushButton"))
        self.sidoLabel = QtGui.QLabel(Dialog)
        self.sidoLabel.setGeometry(QtCore.QRect(20, 100, 41, 21))
        self.sidoLabel.setObjectName(_fromUtf8("sidoLabel"))
        self.sigunguLabel = QtGui.QLabel(Dialog)
        self.sigunguLabel.setGeometry(QtCore.QRect(200, 100, 61, 21))
        self.sigunguLabel.setObjectName(_fromUtf8("sigunguLabel"))
        self.detailPushButton = QtGui.QPushButton(Dialog)
        self.detailPushButton.setGeometry(QtCore.QRect(300, 660, 121, 28))
        self.detailPushButton.setObjectName(_fromUtf8("detailPushButton"))
        self.sidoLineEdit = QtGui.QLineEdit(Dialog)
        self.sidoLineEdit.setGeometry(QtCore.QRect(70, 100, 121, 21))
        self.sidoLineEdit.setObjectName(_fromUtf8("sidoLineEdit"))
        self.sigunguLineEdit = QtGui.QLineEdit(Dialog)
        self.sigunguLineEdit.setGeometry(QtCore.QRect(270, 100, 151, 21))
        self.sigunguLineEdit.setObjectName(_fromUtf8("sigunguLineEdit"))
        self.startDateEdit = QtGui.QDateEdit(Dialog)
        self.startDateEdit.setGeometry(QtCore.QRect(90, 170, 110, 22))
        self.startDateEdit.setDate(QtCore.QDate(2017, 5, 1))
        self.startDateEdit.setTime(QtCore.QTime(0, 0, 0))
        self.startDateEdit.setObjectName(_fromUtf8("startDateEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 64, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(220, 170, 64, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.endDateEdit = QtGui.QDateEdit(Dialog)
        self.endDateEdit.setGeometry(QtCore.QRect(290, 170, 110, 22))
        self.endDateEdit.setDate(QtCore.QDate(2017, 6, 10))
        self.endDateEdit.setObjectName(_fromUtf8("endDateEdit"))
        self.radioButtonDog = QtGui.QRadioButton(Dialog)
        self.radioButtonDog.setGeometry(QtCore.QRect(20, 130, 41, 19))
        self.radioButtonDog.setObjectName(_fromUtf8("radioButtonDog"))
        self.radioButtonAll = QtGui.QRadioButton(Dialog)
        self.radioButtonAll.setGeometry(QtCore.QRect(220, 130, 91, 19))
        self.radioButtonAll.setMouseTracking(True)
        self.radioButtonAll.setCheckable(True)
        self.radioButtonAll.setChecked(True)
        self.radioButtonAll.setObjectName(_fromUtf8("radioButtonAll"))
        self.radioButtonCat = QtGui.QRadioButton(Dialog)
        self.radioButtonCat.setGeometry(QtCore.QRect(80, 130, 71, 19))
        self.radioButtonCat.setObjectName(_fromUtf8("radioButtonCat"))
        self.radioButtonEtc = QtGui.QRadioButton(Dialog)
        self.radioButtonEtc.setGeometry(QtCore.QRect(160, 130, 61, 19))
        self.radioButtonEtc.setObjectName(_fromUtf8("radioButtonEtc"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 371, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Corbel"))
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.NextPagePushButton = QtGui.QPushButton(Dialog)
        self.NextPagePushButton.setGeometry(QtCore.QRect(222, 660, 71, 28))
        self.NextPagePushButton.setObjectName(_fromUtf8("NextPagePushButton"))
        self.PrevPagePushButton = QtGui.QPushButton(Dialog)
        self.PrevPagePushButton.setGeometry(QtCore.QRect(140, 660, 71, 28))
        self.PrevPagePushButton.setObjectName(_fromUtf8("PrevPagePushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.selectMenuComboBox.setItemText(0, _translate("Dialog", "보호소 찾기", None))
        self.selectMenuComboBox.setItemText(1, _translate("Dialog", "유기동물 검색", None))
        self.SearchPushButton.setText(_translate("Dialog", "검색", None))
        self.sidoLabel.setText(_translate("Dialog", "시/도", None))
        self.sigunguLabel.setText(_translate("Dialog", "시/군/구", None))
        self.detailPushButton.setText(_translate("Dialog", "상세정보보기", None))
        self.sidoLineEdit.setText(_translate("Dialog", "경기도", None))
        self.sigunguLineEdit.setText(_translate("Dialog", "시흥시", None))
        self.label_3.setText(_translate("Dialog", "시작일", None))
        self.label_4.setText(_translate("Dialog", "종료일", None))
        self.radioButtonDog.setText(_translate("Dialog", "개", None))
        self.radioButtonAll.setText(_translate("Dialog", "상관없음", None))
        self.radioButtonCat.setText(_translate("Dialog", "고양이", None))
        self.radioButtonEtc.setText(_translate("Dialog", "기타", None))
        self.label_5.setText(_translate("Dialog", "Don\'t Buy Do Adopt", None))
        self.NextPagePushButton.setText(_translate("Dialog", "다음>>", None))
        self.PrevPagePushButton.setText(_translate("Dialog", "<< 이전", None))

