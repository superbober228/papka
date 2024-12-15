# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notes.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(877, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.field_text = QtWidgets.QTextEdit(self.centralwidget)
        self.field_text.setGeometry(QtCore.QRect(10, 260, 881, 301))
        self.field_text.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.field_text.setObjectName("field_text")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 256, 171))
        self.listWidget.setStyleSheet("background-color: rgb(121, 253, 255);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(280, 20, 256, 231))
        self.listWidget_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.button_note_create = QtWidgets.QPushButton(self.centralwidget)
        self.button_note_create.setGeometry(QtCore.QRect(0, 200, 121, 23))
        self.button_note_create.setObjectName("button_note_create")
        self.button_note_del = QtWidgets.QPushButton(self.centralwidget)
        self.button_note_del.setGeometry(QtCore.QRect(130, 200, 121, 23))
        self.button_note_del.setObjectName("button_note_del")
        self.button_note_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_note_save.setGeometry(QtCore.QRect(0, 230, 256, 23))
        self.button_note_save.setObjectName("button_note_save")
        self.button_tag_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_tag_add.setGeometry(QtCore.QRect(540, 50, 121, 23))
        self.button_tag_add.setObjectName("button_tag_add")
        self.button_tag_del = QtWidgets.QPushButton(self.centralwidget)
        self.button_tag_del.setGeometry(QtCore.QRect(540, 80, 121, 23))
        self.button_tag_del.setObjectName("button_tag_del")
        self.button_tag_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_tag_search.setGeometry(QtCore.QRect(540, 110, 256, 23))
        self.button_tag_search.setObjectName("button_tag_search")
        self.list_notes_label = QtWidgets.QLabel(self.centralwidget)
        self.list_notes_label.setGeometry(QtCore.QRect(0, 0, 256, 20))
        self.list_notes_label.setObjectName("list_notes_label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 0, 256, 20))
        self.label_2.setObjectName("label_2")
        self.field_tag = QtWidgets.QLineEdit(self.centralwidget)
        self.field_tag.setGeometry(QtCore.QRect(540, 20, 256, 23))
        self.field_tag.setText("")
        self.field_tag.setObjectName("field_tag")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_note_create.setText(_translate("MainWindow", "Створити замітку"))
        self.button_note_del.setText(_translate("MainWindow", "Видалити замітку"))
        self.button_note_save.setText(_translate("MainWindow", "Зберегти замітку"))
        self.button_tag_add.setText(_translate("MainWindow", "Додати до замітки"))
        self.button_tag_del.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.button_tag_search.setText(_translate("MainWindow", "Шукати замітки за тегом"))
        self.list_notes_label.setText(_translate("MainWindow", "Список заміток"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.field_tag.setPlaceholderText(_translate("MainWindow", "Введіть тег..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())