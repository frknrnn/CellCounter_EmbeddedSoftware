# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uimPmjDm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from zoom import QtImageViewer
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setMaximumSize(QSize(800, 480))
        MainWindow.setStyleSheet(u"background-color: rgb(49, 51, 50);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 35))
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(223, 33))
        self.frame_4.setMaximumSize(QSize(223, 33))
        self.frame_4.setStyleSheet(u"background-image: url(:/icons/mainLogo.png);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.frame_24 = QFrame(self.frame_5)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_24)

        self.frame_22 = QFrame(self.frame_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(100, 0))
        self.frame_22.setMaximumSize(QSize(300, 16777215))
        self.frame_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_10.addWidget(self.frame_22)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(100, 0))
        self.frame_6.setMaximumSize(QSize(100, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignBottom)

        self.pushButton_settings = QPushButton(self.frame_2)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        self.pushButton_settings.setMinimumSize(QSize(0, 30))
        self.pushButton_settings.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.pushButton_settings.setFont(font)
        self.pushButton_settings.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_settings)

        self.pushButton_refreshCamera = QPushButton(self.frame_2)
        self.pushButton_refreshCamera.setObjectName(u"pushButton_refreshCamera")
        self.pushButton_refreshCamera.setMinimumSize(QSize(0, 30))
        self.pushButton_refreshCamera.setMaximumSize(QSize(16777215, 30))
        self.pushButton_refreshCamera.setFont(font)
        self.pushButton_refreshCamera.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_refreshCamera)

        self.pushButton_exit = QPushButton(self.frame_2)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setMinimumSize(QSize(50, 30))
        self.pushButton_exit.setMaximumSize(QSize(50, 30))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.pushButton_exit.setFont(font1)
        self.pushButton_exit.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_exit)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 35))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_8)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButton_preview = QPushButton(self.frame_27)
        self.pushButton_preview.setObjectName(u"pushButton_preview")
        self.pushButton_preview.setMinimumSize(QSize(0, 35))
        self.pushButton_preview.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.pushButton_preview.setFont(font2)
        self.pushButton_preview.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 122, 204,150);\n"
"border:none;\n"
"\n"
"font: 14pt \"Calibri\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(0,122,204, 150);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_15.addWidget(self.pushButton_preview)


        self.horizontalLayout_4.addWidget(self.frame_27, 0, Qt.AlignBottom)

        self.frame_28 = QFrame(self.frame_8)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pushButton_result = QPushButton(self.frame_28)
        self.pushButton_result.setObjectName(u"pushButton_result")
        self.pushButton_result.setMinimumSize(QSize(0, 35))
        self.pushButton_result.setMaximumSize(QSize(16777215, 35))
        self.pushButton_result.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_result.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border:none;\n"
"font: 14pt \"Calibri\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(0, 122, 204, 150);\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.pushButton_result)


        self.horizontalLayout_4.addWidget(self.frame_28, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_9)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_25)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, -1, -1)

        self.horizontalLayout_14.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_9)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_26)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_14.addWidget(self.frame_26)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_7)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_6 = QHBoxLayout(self.page)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_13)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_16)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_coarse_fine = QPushButton(self.frame_16)
        self.pushButton_coarse_fine.setObjectName(u"pushButton_coarse_fine")
        self.pushButton_coarse_fine.setMinimumSize(QSize(0, 35))
        self.pushButton_coarse_fine.setMaximumSize(QSize(16777215, 35))
        self.pushButton_coarse_fine.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.pushButton_coarse_fine.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_coarse_fine)

        self.pushButton_up = QPushButton(self.frame_16)
        self.pushButton_up.setObjectName(u"pushButton_up")
        self.pushButton_up.setMinimumSize(QSize(0, 35))
        self.pushButton_up.setMaximumSize(QSize(16777215, 35))
        self.pushButton_up.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_4.addWidget(self.pushButton_up)

        self.pushButton_down = QPushButton(self.frame_16)
        self.pushButton_down.setObjectName(u"pushButton_down")
        self.pushButton_down.setMinimumSize(QSize(0, 35))
        self.pushButton_down.setMaximumSize(QSize(16777215, 35))
        self.pushButton_down.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_4.addWidget(self.pushButton_down)


        self.verticalLayout_2.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.pushButton_auto_focus = QPushButton(self.frame_15)
        self.pushButton_auto_focus.setObjectName(u"pushButton_auto_focus")
        self.pushButton_auto_focus.setGeometry(QRect(10, 80, 114, 35))
        self.pushButton_auto_focus.setMinimumSize(QSize(0, 35))
        self.pushButton_auto_focus.setMaximumSize(QSize(16777215, 35))
        self.pushButton_auto_focus.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.pushButton_grid_2 = QPushButton(self.frame_15)
        self.pushButton_grid_2.setObjectName(u"pushButton_grid_2")
        self.pushButton_grid_2.setGeometry(QRect(10, 140, 114, 35))
        self.pushButton_grid_2.setMinimumSize(QSize(0, 35))
        self.pushButton_grid_2.setMaximumSize(QSize(16777215, 35))
        self.pushButton_grid_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_2.addWidget(self.frame_15)


        self.horizontalLayout_6.addWidget(self.frame_13)

        self.frame_11 = QFrame(self.page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(512, 384))
        self.frame_11.setMaximumSize(QSize(512, 384))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.picture_box = QLabel(self.frame_11)
        self.picture_box.setObjectName(u"picture_box")
        self.picture_box.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.picture_box)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_12)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_19)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_19)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_32)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_32)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2)


        self.verticalLayout_9.addWidget(self.frame_32, 0, Qt.AlignBottom)

        self.frame_31 = QFrame(self.frame_19)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.frame_31)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 25))
        self.comboBox.setMaximumSize(QSize(16777215, 25))
        font3 = QFont()
        font3.setPointSize(11)
        self.comboBox.setFont(font3)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"}\n"
"QComboBox QAbstractItemView{border: 0px;color:white}\n"
"\n"
"")

        self.horizontalLayout_18.addWidget(self.comboBox)


        self.verticalLayout_9.addWidget(self.frame_31, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_12)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_18)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_77 = QFrame(self.frame_18)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.NoFrame)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_79 = QFrame(self.frame_77)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.NoFrame)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(9, 0, 0, 0)
        self.pushButton_viability = QPushButton(self.frame_79)
        self.pushButton_viability.setObjectName(u"pushButton_viability")
        self.pushButton_viability.setMinimumSize(QSize(20, 20))
        self.pushButton_viability.setMaximumSize(QSize(20, 20))
        self.pushButton_viability.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"\n"
"}\n"
"")

        self.horizontalLayout_46.addWidget(self.pushButton_viability)


        self.horizontalLayout_45.addWidget(self.frame_79, 0, Qt.AlignLeft)

        self.frame_78 = QFrame(self.frame_77)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(100, 0))
        self.frame_78.setMaximumSize(QSize(100, 16777215))
        self.frame_78.setFrameShape(QFrame.NoFrame)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_78)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_49.addWidget(self.label_9)


        self.horizontalLayout_45.addWidget(self.frame_78)


        self.verticalLayout_31.addWidget(self.frame_77)

        self.frame_76 = QFrame(self.frame_18)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.NoFrame)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_80 = QFrame(self.frame_76)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.NoFrame)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(9, 0, 0, 0)
        self.pushButton_autoFocus_count = QPushButton(self.frame_80)
        self.pushButton_autoFocus_count.setObjectName(u"pushButton_autoFocus_count")
        self.pushButton_autoFocus_count.setMinimumSize(QSize(20, 20))
        self.pushButton_autoFocus_count.setMaximumSize(QSize(20, 20))
        self.pushButton_autoFocus_count.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"\n"
"}\n"
"")

        self.horizontalLayout_48.addWidget(self.pushButton_autoFocus_count)


        self.horizontalLayout_47.addWidget(self.frame_80, 0, Qt.AlignLeft)

        self.frame_81 = QFrame(self.frame_76)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(105, 0))
        self.frame_81.setMaximumSize(QSize(100, 16777215))
        self.frame_81.setFrameShape(QFrame.NoFrame)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_81)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(100, 30))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(11)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.label_10)


        self.horizontalLayout_47.addWidget(self.frame_81)


        self.verticalLayout_31.addWidget(self.frame_76)


        self.verticalLayout_3.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_17)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_capture = QPushButton(self.frame_17)
        self.pushButton_capture.setObjectName(u"pushButton_capture")
        self.pushButton_capture.setMinimumSize(QSize(0, 35))
        self.pushButton_capture.setMaximumSize(QSize(16777215, 35))
        self.pushButton_capture.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_capture)

        self.pushButton_count = QPushButton(self.frame_17)
        self.pushButton_count.setObjectName(u"pushButton_count")
        self.pushButton_count.setMinimumSize(QSize(0, 35))
        self.pushButton_count.setMaximumSize(QSize(16777215, 35))
        self.pushButton_count.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_count)


        self.verticalLayout_3.addWidget(self.frame_17)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_17 = QHBoxLayout(self.page_3)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.page_3)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_29)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.circularProgressBarBase = QFrame(self.frame_30)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(250, 30, 300, 300))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 280, 280))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"border-radius:140px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 280, 280))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"border-radius:140px;\n"
"background-color: rgba(77, 77, 127,100);\n"
"}\n"
"")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(20, 20, 260, 260))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius:130px;\n"
"	background-color: rgb(77, 77, 127);	\n"
"}\n"
"")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.circularProgress2 = QFrame(self.circularProgressBarBase)
        self.circularProgress2.setObjectName(u"circularProgress2")
        self.circularProgress2.setGeometry(QRect(30, 30, 240, 240))
        self.circularProgress2.setStyleSheet(u"QFrame{\n"
"border-radius:120px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"\n"
"}")
        self.circularProgress2.setFrameShape(QFrame.NoFrame)
        self.circularProgress2.setFrameShadow(QFrame.Raised)
        self.container2 = QFrame(self.circularProgressBarBase)
        self.container2.setObjectName(u"container2")
        self.container2.setGeometry(QRect(40, 40, 220, 220))
        self.container2.setStyleSheet(u"QFrame{\n"
"	border-radius:110px;\n"
"	background-color: rgb(77, 77, 127);	\n"
"}")
        self.container2.setFrameShape(QFrame.NoFrame)
        self.container2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.container2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-30, 60, 281, 81))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:none;\n"
"color:rgb(255,255,255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        self.circularProgress2.raise_()
        self.container2.raise_()

        self.verticalLayout_8.addWidget(self.frame_30)


        self.horizontalLayout_17.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_8 = QHBoxLayout(self.page_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.page_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_14)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(170, 0))
        self.frame_20.setMaximumSize(QSize(170, 16777215))
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_20)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 2, 0)
        self.frame_51 = QFrame(self.frame_20)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_52)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.frame_52)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(0, 50))
        self.frame_58.setMaximumSize(QSize(16777215, 50))
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_65 = QFrame(self.frame_58)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.NoFrame)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_minValue = QLabel(self.frame_65)
        self.label_minValue.setObjectName(u"label_minValue")
        self.label_minValue.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_33.addWidget(self.label_minValue, 0, Qt.AlignHCenter)


        self.horizontalLayout_31.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.frame_58)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.NoFrame)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_maxValue = QLabel(self.frame_66)
        self.label_maxValue.setObjectName(u"label_maxValue")
        self.label_maxValue.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_34.addWidget(self.label_maxValue, 0, Qt.AlignHCenter)


        self.horizontalLayout_31.addWidget(self.frame_66)


        self.verticalLayout_28.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.frame_52)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_61 = QFrame(self.frame_59)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.verticalSlider_min = QSlider(self.frame_61)
        self.verticalSlider_min.setObjectName(u"verticalSlider_min")
        self.verticalSlider_min.setStyleSheet(u"QSlider{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"\n"
"    background-color: white;\n"
"\n"
"	border-radius:5px;\n"
"\n"
"    }")
        self.verticalSlider_min.setMaximum(60)
        self.verticalSlider_min.setOrientation(Qt.Vertical)

        self.horizontalLayout_29.addWidget(self.verticalSlider_min)


        self.horizontalLayout_28.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_59)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.NoFrame)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalSlider_max = QSlider(self.frame_62)
        self.verticalSlider_max.setObjectName(u"verticalSlider_max")
        self.verticalSlider_max.setStyleSheet(u"QSlider{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QSlider::handle:vertical {\n"
"\n"
"    background-color: white;\n"
"\n"
"	border-radius:5px;\n"
"\n"
"    }")
        self.verticalSlider_max.setMaximum(60)
        self.verticalSlider_max.setValue(60)
        self.verticalSlider_max.setOrientation(Qt.Vertical)

        self.horizontalLayout_32.addWidget(self.verticalSlider_max)


        self.horizontalLayout_28.addWidget(self.frame_62)


        self.verticalLayout_28.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_52)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 50))
        self.frame_60.setMaximumSize(QSize(16777215, 50))
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_63 = QFrame(self.frame_60)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.NoFrame)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_7 = QLabel(self.frame_63)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_35.addWidget(self.label_7, 0, Qt.AlignHCenter)


        self.horizontalLayout_30.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_60)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_64.setFrameShape(QFrame.NoFrame)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_8 = QLabel(self.frame_64)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_36.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.horizontalLayout_30.addWidget(self.frame_64)


        self.verticalLayout_28.addWidget(self.frame_60)


        self.horizontalLayout_25.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_51)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(35, 0))
        self.frame_53.setMaximumSize(QSize(35, 16777215))
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_53)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 10, 0, 0)
        self.frame_57 = QFrame(self.frame_53)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_57)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.pushButton_showTotal = QPushButton(self.frame_57)
        self.pushButton_showTotal.setObjectName(u"pushButton_showTotal")
        self.pushButton_showTotal.setMinimumSize(QSize(25, 25))
        self.pushButton_showTotal.setMaximumSize(QSize(25, 25))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setWeight(50)
        self.pushButton_showTotal.setFont(font5)
        self.pushButton_showTotal.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background-image: url(:/icons/whitePressed.png);\n"
"}")

        self.verticalLayout_27.addWidget(self.pushButton_showTotal)


        self.verticalLayout_26.addWidget(self.frame_57, 0, Qt.AlignHCenter)

        self.frame_55 = QFrame(self.frame_53)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.pushButton_showLive = QPushButton(self.frame_55)
        self.pushButton_showLive.setObjectName(u"pushButton_showLive")
        self.pushButton_showLive.setMinimumSize(QSize(23, 23))
        self.pushButton_showLive.setMaximumSize(QSize(23, 23))
        self.pushButton_showLive.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background-image: url(:/icons/greenUnPressed.png);\n"
"}\n"
"")

        self.horizontalLayout_26.addWidget(self.pushButton_showLive)


        self.verticalLayout_26.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_53)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.pushButton_showDead = QPushButton(self.frame_56)
        self.pushButton_showDead.setObjectName(u"pushButton_showDead")
        self.pushButton_showDead.setMinimumSize(QSize(23, 23))
        self.pushButton_showDead.setMaximumSize(QSize(23, 23))
        self.pushButton_showDead.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-image: url(:/icons/redUnPressed.png);\n"
"}\n"
"")

        self.horizontalLayout_27.addWidget(self.pushButton_showDead)


        self.verticalLayout_26.addWidget(self.frame_56)


        self.horizontalLayout_25.addWidget(self.frame_53)


        self.verticalLayout_25.addWidget(self.frame_51)

        self.frame_54 = QFrame(self.frame_20)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 100))
        self.frame_54.setMaximumSize(QSize(16777215, 100))
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.frame_54)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.NoFrame)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_67)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_average = QLabel(self.frame_67)
        self.label_average.setObjectName(u"label_average")
        self.label_average.setFont(font)
        self.label_average.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_29.addWidget(self.label_average, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_averageCellSize = QLabel(self.frame_67)
        self.label_averageCellSize.setObjectName(u"label_averageCellSize")
        self.label_averageCellSize.setFont(font)
        self.label_averageCellSize.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_29.addWidget(self.label_averageCellSize, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_37.addWidget(self.frame_67)


        self.verticalLayout_25.addWidget(self.frame_54)


        self.horizontalLayout_9.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_14)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_21)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 20, 0, 0)
        self.frame_33 = QFrame(self.frame_21)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_33)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_33)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.page_4)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_35)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 285))
        self.frame_36.setMaximumSize(QSize(16777215, 285))
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_36)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pictureBox_result = QtImageViewer()
        self.pictureBox_result.setObjectName(u"pictureBox_result")
        self.pictureBox_result.setMinimumSize(QSize(428, 285))
        self.pictureBox_result.setStyleSheet(u"QGraphicsView{\n"
"border:none;\n"
"}\n"
" QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color:rgb(49, 51, 50) ;  \n"
"	\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"     background-color: white;      /* #605F5F; */\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QS"
                        "crollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar:vertical\n"
" {\n"
"     \n"
"	background-color: rgb(49, 51, 50);\n"
"     width: 15px;\n"
"     margin: 15px 3px 15px 3px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical\n"
" {\n"
"     backg"
                        "round-color: white;         /* #605F5F; */\n"
"     min-height: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical\n"
" {\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical\n"
" {\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
" {\n"
"     bor"
                        "der-image: url(:/qss_icons/rc/down_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
" {\n"
"     background: none;\n"
" }")
        self.pictureBox_result.setFrameShape(QFrame.NoFrame)
        self.pictureBox_result.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.pictureBox_result.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verticalLayout_15.addWidget(self.pictureBox_result)


        self.verticalLayout_14.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(50, 0))
        self.frame_38.setMaximumSize(QSize(50, 16777215))
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_3 = QLabel(self.frame_38)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_19.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_39)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalSlider_zoom = QSlider(self.frame_39)
        self.horizontalSlider_zoom.setObjectName(u"horizontalSlider_zoom")
        self.horizontalSlider_zoom.setStyleSheet(u"QSlider{\n"
"\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"\n"
"    background-color: white;\n"
"\n"
"	border-radius:5px;\n"
"\n"
"    }")
        self.horizontalSlider_zoom.setMinimum(1)
        self.horizontalSlider_zoom.setMaximum(10)
        self.horizontalSlider_zoom.setPageStep(1)
        self.horizontalSlider_zoom.setOrientation(Qt.Horizontal)

        self.verticalLayout_16.addWidget(self.horizontalSlider_zoom)


        self.horizontalLayout_12.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_37)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(50, 0))
        self.frame_40.setMaximumSize(QSize(50, 16777215))
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_zoom = QLabel(self.frame_40)
        self.label_zoom.setObjectName(u"label_zoom")
        self.label_zoom.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_zoom, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.frame_40)


        self.verticalLayout_14.addWidget(self.frame_37)


        self.verticalLayout_13.addWidget(self.frame_35)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_24 = QHBoxLayout(self.page_5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_43 = QFrame(self.page_5)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")

        self.horizontalLayout_24.addWidget(self.frame_43)

        self.stackedWidget_2.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.stackedWidget_2)


        self.verticalLayout_11.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_21)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 50))
        self.frame_34.setMaximumSize(QSize(16777215, 50))
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_21.setSpacing(15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_34)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.pushButton_image = QPushButton(self.frame_41)
        self.pushButton_image.setObjectName(u"pushButton_image")
        self.pushButton_image.setMinimumSize(QSize(130, 35))
        self.pushButton_image.setMaximumSize(QSize(130, 35))
        self.pushButton_image.setFont(font2)
        self.pushButton_image.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 122, 204,150);\n"
"border:none;\n"
"\n"
"font: 14pt \"Calibri\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(0,122,204, 150);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_22.addWidget(self.pushButton_image)


        self.horizontalLayout_21.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_34)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pushButton_histogram = QPushButton(self.frame_42)
        self.pushButton_histogram.setObjectName(u"pushButton_histogram")
        self.pushButton_histogram.setMinimumSize(QSize(130, 35))
        self.pushButton_histogram.setMaximumSize(QSize(110, 35))
        self.pushButton_histogram.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_histogram.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border:none;\n"
"font: 14pt \"Calibri\";\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(0, 122, 204, 150);\n"
"}\n"
"")

        self.horizontalLayout_23.addWidget(self.pushButton_histogram)


        self.horizontalLayout_21.addWidget(self.frame_42)


        self.verticalLayout_11.addWidget(self.frame_34)


        self.horizontalLayout_9.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.frame_14)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(200, 0))
        self.frame_23.setMaximumSize(QSize(200, 16777215))
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_23)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(2, 20, 0, 0)
        self.frame_44 = QFrame(self.frame_23)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_44)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 90))
        self.frame_45.setMaximumSize(QSize(16777215, 90))
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_45)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_total_concentration = QLabel(self.frame_45)
        self.label_total_concentration.setObjectName(u"label_total_concentration")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(13)
        self.label_total_concentration.setFont(font6)
        self.label_total_concentration.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_18.addWidget(self.label_total_concentration)

        self.label_total_cell = QLabel(self.frame_45)
        self.label_total_cell.setObjectName(u"label_total_cell")
        self.label_total_cell.setFont(font)
        self.label_total_cell.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_18.addWidget(self.label_total_cell)


        self.verticalLayout_17.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 90))
        self.frame_46.setMaximumSize(QSize(16777215, 90))
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_46)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_live_concantration = QLabel(self.frame_46)
        self.label_live_concantration.setObjectName(u"label_live_concantration")
        self.label_live_concantration.setFont(font6)
        self.label_live_concantration.setStyleSheet(u"color: rgb(0, 166, 81);")

        self.verticalLayout_19.addWidget(self.label_live_concantration)

        self.label_live_cell = QLabel(self.frame_46)
        self.label_live_cell.setObjectName(u"label_live_cell")
        self.label_live_cell.setFont(font)
        self.label_live_cell.setStyleSheet(u"color: rgb(0, 166, 81);")

        self.verticalLayout_19.addWidget(self.label_live_cell)

        self.progressBar_liveCell = QProgressBar(self.frame_46)
        self.progressBar_liveCell.setObjectName(u"progressBar_liveCell")
        self.progressBar_liveCell.setStyleSheet(u"QProgressBar{\n"
"background-color: rgba(49, 51, 50, 100);\n"
"color:rgb(200, 200, 200);\n"
"border-style:none;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}\n"
"QProgressBar::Chunk{\n"
"border-radius:10px;\n"
"	background-color: rgb(0, 166, 81);\n"
"}\n"
"")
        self.progressBar_liveCell.setValue(24)

        self.verticalLayout_19.addWidget(self.progressBar_liveCell)


        self.verticalLayout_17.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_44)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 90))
        self.frame_47.setMaximumSize(QSize(16777215, 90))
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_47)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_dead_concentration = QLabel(self.frame_47)
        self.label_dead_concentration.setObjectName(u"label_dead_concentration")
        self.label_dead_concentration.setFont(font6)
        self.label_dead_concentration.setStyleSheet(u"\n"
"color: rgb(238, 29, 37);")

        self.verticalLayout_20.addWidget(self.label_dead_concentration)

        self.label_dead_cell = QLabel(self.frame_47)
        self.label_dead_cell.setObjectName(u"label_dead_cell")
        self.label_dead_cell.setFont(font)
        self.label_dead_cell.setStyleSheet(u"color: rgb(238, 29, 37);")

        self.verticalLayout_20.addWidget(self.label_dead_cell)

        self.progressBar_deadCell = QProgressBar(self.frame_47)
        self.progressBar_deadCell.setObjectName(u"progressBar_deadCell")
        self.progressBar_deadCell.setStyleSheet(u"QProgressBar{\n"
"background-color: rgba(49, 51, 50, 100);\n"
"color:rgb(200, 200, 200);\n"
"border-style:none;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}\n"
"QProgressBar::Chunk{\n"
"border-radius:10px;\n"
"	background-color: rgb(238, 29, 37);\n"
"}\n"
"")
        self.progressBar_deadCell.setValue(24)

        self.verticalLayout_20.addWidget(self.progressBar_deadCell)


        self.verticalLayout_17.addWidget(self.frame_47)


        self.verticalLayout_21.addWidget(self.frame_44)

        self.frame_48 = QFrame(self.frame_23)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_48)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.frame_48)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_50)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")

        self.verticalLayout_22.addWidget(self.frame_50)

        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_49)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.pushButton_saveData = QPushButton(self.frame_49)
        self.pushButton_saveData.setObjectName(u"pushButton_saveData")
        self.pushButton_saveData.setMinimumSize(QSize(120, 35))
        self.pushButton_saveData.setMaximumSize(QSize(120, 35))
        self.pushButton_saveData.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_24.addWidget(self.pushButton_saveData)


        self.verticalLayout_22.addWidget(self.frame_49, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_48)


        self.horizontalLayout_9.addWidget(self.frame_23)


        self.horizontalLayout_8.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.page_2)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_44 = QHBoxLayout(self.page_6)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_75 = QFrame(self.page_6)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.NoFrame)
        self.frame_75.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_44.addWidget(self.frame_75)

        self.stackedWidget.addWidget(self.page_6)

        self.horizontalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_settings.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.pushButton_refreshCamera.setText(QCoreApplication.translate("MainWindow", u"REFRESH CAMERA", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_preview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.pushButton_result.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.pushButton_coarse_fine.setText(QCoreApplication.translate("MainWindow", u"COARSE", None))
        self.pushButton_up.setText(QCoreApplication.translate("MainWindow", u"UP", None))
        self.pushButton_down.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
        self.pushButton_auto_focus.setText(QCoreApplication.translate("MainWindow", u"AUTO FOCUS", None))
        self.pushButton_grid_2.setText(QCoreApplication.translate("MainWindow", u"GRID", None))
        self.picture_box.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CELL TYPE", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"HeLa", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Hek-293", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"u87", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Yeast", None))

        self.pushButton_viability.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"VIABILITY", None))
        self.pushButton_autoFocus_count.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"AUTOFOCUS", None))
        self.pushButton_capture.setText(QCoreApplication.translate("MainWindow", u"CAPTURE", None))
        self.pushButton_count.setText(QCoreApplication.translate("MainWindow", u"COUNT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<strong>Please wait</strong>...", None))
        self.label_minValue.setText(QCoreApplication.translate("MainWindow", u"0 um", None))
        self.label_maxValue.setText(QCoreApplication.translate("MainWindow", u"60 um", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"M\u0130N", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"MAX", None))
        self.pushButton_showTotal.setText("")
        self.pushButton_showLive.setText("")
        self.pushButton_showDead.setText("")
        self.label_average.setText(QCoreApplication.translate("MainWindow", u"Average Cell Size", None))
        self.label_averageCellSize.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ZOOM", None))
        self.label_zoom.setText(QCoreApplication.translate("MainWindow", u"1x", None))
        self.pushButton_image.setText(QCoreApplication.translate("MainWindow", u"IMAGE", None))
        self.pushButton_histogram.setText(QCoreApplication.translate("MainWindow", u"HISTOGRAM", None))
        self.label_total_concentration.setText(QCoreApplication.translate("MainWindow", u"TOTAL :", None))
        self.label_total_cell.setText(QCoreApplication.translate("MainWindow", u"?? TOTAL CELLS DETECTED", None))
        self.label_live_concantration.setText(QCoreApplication.translate("MainWindow", u"L\u0130VE :", None))
        self.label_live_cell.setText(QCoreApplication.translate("MainWindow", u"?? L\u0130VE CELLS DETECTED", None))
        self.label_dead_concentration.setText(QCoreApplication.translate("MainWindow", u"DEAD : ", None))
        self.label_dead_cell.setText(QCoreApplication.translate("MainWindow", u"?? DEAD CELLS DETECTED", None))
        self.pushButton_saveData.setText(QCoreApplication.translate("MainWindow", u"SAVE DATA", None))
    # retranslateUi

