# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gym.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from typing import Any, Dict, Mapping, Optional, Type, Union
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTimeEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 828)
        self.actionFuncionarios = QAction(MainWindow)
        self.actionFuncionarios.setObjectName(u"actionFuncionarios")
        self.actionAlunos = QAction(MainWindow)
        self.actionAlunos.setObjectName(u"actionAlunos")
        self.actionTurmas = QAction(MainWindow)
        self.actionTurmas.setObjectName(u"actionTurmas")
        self.actionVoltar = QAction(MainWindow)
        self.actionVoltar.setObjectName(u"actionVoltar")
        self.actionSair = QAction(MainWindow)
        self.actionSair.setObjectName(u"actionSair")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pagesGeral = QStackedWidget(self.centralwidget)
        self.pagesGeral.setObjectName(u"pagesGeral")
        self.pageG_Home = QWidget()
        self.pageG_Home.setObjectName(u"pageG_Home")
        self.verticalLayout = QVBoxLayout(self.pageG_Home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.pageG_Home)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet(u"label{\n"
"	color: rgb(255,140,0)\n"
"	font-weight: bold\n"
"}")

        self.verticalLayout.addWidget(self.label_6)

        self.pagesGeral.addWidget(self.pageG_Home)
        self.pageG_CadFuncionario = QWidget()
        self.pageG_CadFuncionario.setObjectName(u"pageG_CadFuncionario")
        self.verticalLayout_12 = QVBoxLayout(self.pageG_CadFuncionario)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frmBuscaFuncionario = QFrame(self.pageG_CadFuncionario)
        self.frmBuscaFuncionario.setObjectName(u"frmBuscaFuncionario")
        self.frmBuscaFuncionario.setFrameShape(QFrame.Box)
        self.frmBuscaFuncionario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frmBuscaFuncionario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.lbl_cadFuncionario = QLabel(self.frmBuscaFuncionario)
        self.lbl_cadFuncionario.setObjectName(u"lbl_cadFuncionario")

        self.horizontalLayout_7.addWidget(self.lbl_cadFuncionario)

        self.btn_BackListFuncionario = QPushButton(self.frmBuscaFuncionario)
        self.btn_BackListFuncionario.setObjectName(u"btn_BackListFuncionario")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_BackListFuncionario.sizePolicy().hasHeightForWidth())
        self.btn_BackListFuncionario.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.btn_BackListFuncionario)

        self.btn_ExitCadFuncionario = QPushButton(self.frmBuscaFuncionario)
        self.btn_ExitCadFuncionario.setObjectName(u"btn_ExitCadFuncionario")
        sizePolicy1.setHeightForWidth(self.btn_ExitCadFuncionario.sizePolicy().hasHeightForWidth())
        self.btn_ExitCadFuncionario.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u"Images/icons/icons8-excluir.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ExitCadFuncionario.setIcon(icon)
        self.btn_ExitCadFuncionario.setCheckable(False)
        self.btn_ExitCadFuncionario.setAutoRepeat(False)
        self.btn_ExitCadFuncionario.setAutoExclusive(False)

        self.horizontalLayout_7.addWidget(self.btn_ExitCadFuncionario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.BuscaFuncionario = QFrame(self.frmBuscaFuncionario)
        self.BuscaFuncionario.setObjectName(u"BuscaFuncionario")
        self.BuscaFuncionario.setFrameShape(QFrame.StyledPanel)
        self.BuscaFuncionario.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.BuscaFuncionario)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_BuscaFuncionario = QLabel(self.BuscaFuncionario)
        self.lbl_BuscaFuncionario.setObjectName(u"lbl_BuscaFuncionario")

        self.horizontalLayout_2.addWidget(self.lbl_BuscaFuncionario)

        self.tpBusca_Funcionario = QComboBox(self.BuscaFuncionario)
        self.tpBusca_Funcionario.addItem("")
        self.tpBusca_Funcionario.addItem("")
        self.tpBusca_Funcionario.setObjectName(u"tpBusca_Funcionario")

        self.horizontalLayout_2.addWidget(self.tpBusca_Funcionario)

        self.Edit_BuscaFuncionario = QLineEdit(self.BuscaFuncionario)
        self.Edit_BuscaFuncionario.setObjectName(u"Edit_BuscaFuncionario")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Edit_BuscaFuncionario.sizePolicy().hasHeightForWidth())
        self.Edit_BuscaFuncionario.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.Edit_BuscaFuncionario)


        self.verticalLayout_2.addWidget(self.BuscaFuncionario)

        self.fmBtn_Funcionario = QFrame(self.frmBuscaFuncionario)
        self.fmBtn_Funcionario.setObjectName(u"fmBtn_Funcionario")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fmBtn_Funcionario.sizePolicy().hasHeightForWidth())
        self.fmBtn_Funcionario.setSizePolicy(sizePolicy3)
        self.fmBtn_Funcionario.setFrameShape(QFrame.StyledPanel)
        self.fmBtn_Funcionario.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fmBtn_Funcionario)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_CadFuncionario = QPushButton(self.fmBtn_Funcionario)
        self.btn_CadFuncionario.setObjectName(u"btn_CadFuncionario")
        sizePolicy2.setHeightForWidth(self.btn_CadFuncionario.sizePolicy().hasHeightForWidth())
        self.btn_CadFuncionario.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_CadFuncionario)

        self.btn_AlterFuncionario = QPushButton(self.fmBtn_Funcionario)
        self.btn_AlterFuncionario.setObjectName(u"btn_AlterFuncionario")
        sizePolicy2.setHeightForWidth(self.btn_AlterFuncionario.sizePolicy().hasHeightForWidth())
        self.btn_AlterFuncionario.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_AlterFuncionario)

        self.btn_ExclFuncionario = QPushButton(self.fmBtn_Funcionario)
        self.btn_ExclFuncionario.setObjectName(u"btn_ExclFuncionario")
        sizePolicy2.setHeightForWidth(self.btn_ExclFuncionario.sizePolicy().hasHeightForWidth())
        self.btn_ExclFuncionario.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_ExclFuncionario)

        self.btn_RelatFuncionario = QPushButton(self.fmBtn_Funcionario)
        self.btn_RelatFuncionario.setObjectName(u"btn_RelatFuncionario")
        sizePolicy2.setHeightForWidth(self.btn_RelatFuncionario.sizePolicy().hasHeightForWidth())
        self.btn_RelatFuncionario.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_RelatFuncionario)


        self.verticalLayout_2.addWidget(self.fmBtn_Funcionario)


        self.verticalLayout_12.addWidget(self.frmBuscaFuncionario)

        self.pagesFuncionario = QStackedWidget(self.pageG_CadFuncionario)
        self.pagesFuncionario.setObjectName(u"pagesFuncionario")
        self.pgCadFuncionario = QWidget()
        self.pgCadFuncionario.setObjectName(u"pgCadFuncionario")
        self.verticalLayout_10 = QVBoxLayout(self.pgCadFuncionario)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.pgCadFuncionario)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_12.addWidget(self.label_19)

        self.checkBox = QCheckBox(self.frame_4)
        self.checkBox.setObjectName(u"checkBox")
        font = QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_12.addWidget(self.checkBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_5.addWidget(self.label_22)

        self.lineEdit_14 = QLineEdit(self.frame_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy1.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.lineEdit_14)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_8 = QLineEdit(self.frame_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_3.addWidget(self.lineEdit_8)

        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_3.addWidget(self.label_20)

        self.comboBox_5 = QComboBox(self.frame_4)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_3.addWidget(self.comboBox_5)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.lineEdit_9 = QLineEdit(self.frame_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_3.addWidget(self.lineEdit_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_13 = QLineEdit(self.frame_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_4.addWidget(self.lineEdit_13)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        font1 = QFont()
        font1.setPointSize(10)
        self.dateEdit.setFont(font1)

        self.horizontalLayout_4.addWidget(self.dateEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_9.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.pgCadFuncionario)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_3.addWidget(self.label_18)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_8.addWidget(self.lineEdit_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.comboBox_3 = QComboBox(self.frame_5)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy2.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.comboBox_3)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.pushButton_3)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)

        self.horizontalLayout_10.addWidget(self.label_4)

        self.comboBox_4 = QComboBox(self.frame_5)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy2.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.comboBox_4)

        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        sizePolicy4.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy4)

        self.horizontalLayout_10.addWidget(self.label_21)

        self.comboBox_6 = QComboBox(self.frame_5)
        self.comboBox_6.setObjectName(u"comboBox_6")
        sizePolicy1.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.comboBox_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.frame_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_11.addWidget(self.lineEdit_5)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.comboBox = QComboBox(self.frame_5)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.comboBox)

        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.comboBox_2 = QComboBox(self.frame_5)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.comboBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")

        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_27 = QHBoxLayout(self.frame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_20.addWidget(self.label_13)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_20)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.tabWidget)


        self.horizontalLayout_27.addLayout(self.verticalLayout_5)


        self.horizontalLayout_28.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        self.label_17.setFont(font2)

        self.horizontalLayout_26.addWidget(self.label_17)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font1)

        self.horizontalLayout_26.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)

        self.horizontalLayout_26.addWidget(self.radioButton_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_21.addWidget(self.label_14)

        self.lineEdit_10 = QLineEdit(self.frame_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_21.addWidget(self.lineEdit_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_22.addWidget(self.label_15)

        self.lineEdit_11 = QLineEdit(self.frame_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_22.addWidget(self.lineEdit_11)


        self.verticalLayout_4.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_23.addWidget(self.label_16)

        self.lineEdit_12 = QLineEdit(self.frame_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_23.addWidget(self.lineEdit_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.btn_SaveFuncionario = QPushButton(self.frame_2)
        self.btn_SaveFuncionario.setObjectName(u"btn_SaveFuncionario")

        self.horizontalLayout_24.addWidget(self.btn_SaveFuncionario)

        self.btn_CancelFuncionario = QPushButton(self.frame_2)
        self.btn_CancelFuncionario.setObjectName(u"btn_CancelFuncionario")

        self.horizontalLayout_24.addWidget(self.btn_CancelFuncionario)


        self.verticalLayout_4.addLayout(self.horizontalLayout_24)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_28.addWidget(self.frame_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_28)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.pagesFuncionario.addWidget(self.pgCadFuncionario)
        self.pgListFuncionario = QWidget()
        self.pgListFuncionario.setObjectName(u"pgListFuncionario")
        self.horizontalLayout_6 = QHBoxLayout(self.pgListFuncionario)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.treeWidget = QTreeWidget(self.pgListFuncionario)
        self.treeWidget.setObjectName(u"treeWidget")

        self.horizontalLayout_6.addWidget(self.treeWidget)

        self.pagesFuncionario.addWidget(self.pgListFuncionario)

        self.verticalLayout_12.addWidget(self.pagesFuncionario)

        self.pagesGeral.addWidget(self.pageG_CadFuncionario)
        self.pageG_CadAluno = QWidget()
        self.pageG_CadAluno.setObjectName(u"pageG_CadAluno")
        self.verticalLayout_20 = QVBoxLayout(self.pageG_CadAluno)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frmBuscaAluno = QFrame(self.pageG_CadAluno)
        self.frmBuscaAluno.setObjectName(u"frmBuscaAluno")
        self.frmBuscaAluno.setFrameShape(QFrame.Box)
        self.frmBuscaAluno.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frmBuscaAluno)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)

        self.lbl_cadAluno = QLabel(self.frmBuscaAluno)
        self.lbl_cadAluno.setObjectName(u"lbl_cadAluno")

        self.horizontalLayout_13.addWidget(self.lbl_cadAluno)

        self.btn_BackListAluno = QPushButton(self.frmBuscaAluno)
        self.btn_BackListAluno.setObjectName(u"btn_BackListAluno")
        sizePolicy1.setHeightForWidth(self.btn_BackListAluno.sizePolicy().hasHeightForWidth())
        self.btn_BackListAluno.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.btn_BackListAluno)

        self.btn_ExitCadAluno = QPushButton(self.frmBuscaAluno)
        self.btn_ExitCadAluno.setObjectName(u"btn_ExitCadAluno")
        sizePolicy1.setHeightForWidth(self.btn_ExitCadAluno.sizePolicy().hasHeightForWidth())
        self.btn_ExitCadAluno.setSizePolicy(sizePolicy1)
        self.btn_ExitCadAluno.setIcon(icon)
        self.btn_ExitCadAluno.setCheckable(False)
        self.btn_ExitCadAluno.setAutoRepeat(False)
        self.btn_ExitCadAluno.setAutoExclusive(False)

        self.horizontalLayout_13.addWidget(self.btn_ExitCadAluno)


        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.BuscaAluno = QFrame(self.frmBuscaAluno)
        self.BuscaAluno.setObjectName(u"BuscaAluno")
        self.BuscaAluno.setFrameShape(QFrame.StyledPanel)
        self.BuscaAluno.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.BuscaAluno)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lbl_BuscaaAluno = QLabel(self.BuscaAluno)
        self.lbl_BuscaaAluno.setObjectName(u"lbl_BuscaaAluno")

        self.horizontalLayout_14.addWidget(self.lbl_BuscaaAluno)

        self.tpBusca_Aluno = QComboBox(self.BuscaAluno)
        self.tpBusca_Aluno.addItem("")
        self.tpBusca_Aluno.addItem("")
        self.tpBusca_Aluno.setObjectName(u"tpBusca_Aluno")

        self.horizontalLayout_14.addWidget(self.tpBusca_Aluno)

        self.Edit_BuscaAluno = QLineEdit(self.BuscaAluno)
        self.Edit_BuscaAluno.setObjectName(u"Edit_BuscaAluno")
        sizePolicy2.setHeightForWidth(self.Edit_BuscaAluno.sizePolicy().hasHeightForWidth())
        self.Edit_BuscaAluno.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.Edit_BuscaAluno)


        self.verticalLayout_11.addWidget(self.BuscaAluno)

        self.fmBtn_Aluno = QFrame(self.frmBuscaAluno)
        self.fmBtn_Aluno.setObjectName(u"fmBtn_Aluno")
        sizePolicy3.setHeightForWidth(self.fmBtn_Aluno.sizePolicy().hasHeightForWidth())
        self.fmBtn_Aluno.setSizePolicy(sizePolicy3)
        self.fmBtn_Aluno.setFrameShape(QFrame.StyledPanel)
        self.fmBtn_Aluno.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.fmBtn_Aluno)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_CadAluno = QPushButton(self.fmBtn_Aluno)
        self.btn_CadAluno.setObjectName(u"btn_CadAluno")
        sizePolicy2.setHeightForWidth(self.btn_CadAluno.sizePolicy().hasHeightForWidth())
        self.btn_CadAluno.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.btn_CadAluno)

        self.btn_AlterAluno = QPushButton(self.fmBtn_Aluno)
        self.btn_AlterAluno.setObjectName(u"btn_AlterAluno")
        sizePolicy2.setHeightForWidth(self.btn_AlterAluno.sizePolicy().hasHeightForWidth())
        self.btn_AlterAluno.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.btn_AlterAluno)

        self.btn_ExclAluno = QPushButton(self.fmBtn_Aluno)
        self.btn_ExclAluno.setObjectName(u"btn_ExclAluno")
        sizePolicy2.setHeightForWidth(self.btn_ExclAluno.sizePolicy().hasHeightForWidth())
        self.btn_ExclAluno.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.btn_ExclAluno)

        self.btn_RelatAluno = QPushButton(self.fmBtn_Aluno)
        self.btn_RelatAluno.setObjectName(u"btn_RelatAluno")
        sizePolicy2.setHeightForWidth(self.btn_RelatAluno.sizePolicy().hasHeightForWidth())
        self.btn_RelatAluno.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.btn_RelatAluno)


        self.verticalLayout_11.addWidget(self.fmBtn_Aluno)


        self.verticalLayout_20.addWidget(self.frmBuscaAluno)

        self.pagesAluno = QStackedWidget(self.pageG_CadAluno)
        self.pagesAluno.setObjectName(u"pagesAluno")
        self.pgCadAluno = QWidget()
        self.pgCadAluno.setObjectName(u"pgCadAluno")
        self.verticalLayout_13 = QVBoxLayout(self.pgCadAluno)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_6 = QFrame(self.pgCadAluno)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_16.addWidget(self.label_23)

        self.checkBox_2 = QCheckBox(self.frame_6)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)
        self.checkBox_2.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_16.addWidget(self.checkBox_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_15.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_6)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_15.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_6)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_15.addWidget(self.label_26)


        self.horizontalLayout_17.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_18.addWidget(self.lineEdit_3)

        self.label_27 = QLabel(self.frame_6)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_18.addWidget(self.label_27)

        self.lineEdit_15 = QLineEdit(self.frame_6)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy1.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.lineEdit_15)


        self.verticalLayout_16.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lineEdit_16 = QLineEdit(self.frame_6)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.horizontalLayout_25.addWidget(self.lineEdit_16)

        self.label_28 = QLabel(self.frame_6)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_25.addWidget(self.label_28)

        self.comboBox_7 = QComboBox(self.frame_6)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_25.addWidget(self.comboBox_7)

        self.label_29 = QLabel(self.frame_6)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_25.addWidget(self.label_29)

        self.lineEdit_17 = QLineEdit(self.frame_6)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.horizontalLayout_25.addWidget(self.lineEdit_17)


        self.verticalLayout_16.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lineEdit_18 = QLineEdit(self.frame_6)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.horizontalLayout_29.addWidget(self.lineEdit_18)

        self.label_30 = QLabel(self.frame_6)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_29.addWidget(self.label_30)

        self.dateEdit_2 = QDateEdit(self.frame_6)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setFont(font1)

        self.horizontalLayout_29.addWidget(self.dateEdit_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_17.addLayout(self.verticalLayout_16)


        self.verticalLayout_14.addLayout(self.horizontalLayout_17)


        self.verticalLayout_13.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.pgCadAluno)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_17 = QVBoxLayout(self.frame_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_17.addWidget(self.label_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_32 = QLabel(self.frame_7)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_30.addWidget(self.label_32)

        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_30.addWidget(self.lineEdit_4)


        self.verticalLayout_17.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_33 = QLabel(self.frame_7)
        self.label_33.setObjectName(u"label_33")
        sizePolicy4.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy4)

        self.horizontalLayout_31.addWidget(self.label_33)

        self.comboBox_8 = QComboBox(self.frame_7)
        self.comboBox_8.setObjectName(u"comboBox_8")
        sizePolicy2.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy2)

        self.horizontalLayout_31.addWidget(self.comboBox_8)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_31.addWidget(self.pushButton_4)

        self.label_34 = QLabel(self.frame_7)
        self.label_34.setObjectName(u"label_34")
        sizePolicy4.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy4)

        self.horizontalLayout_31.addWidget(self.label_34)

        self.comboBox_9 = QComboBox(self.frame_7)
        self.comboBox_9.setObjectName(u"comboBox_9")
        sizePolicy2.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy2)

        self.horizontalLayout_31.addWidget(self.comboBox_9)

        self.label_35 = QLabel(self.frame_7)
        self.label_35.setObjectName(u"label_35")
        sizePolicy4.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy4)

        self.horizontalLayout_31.addWidget(self.label_35)

        self.comboBox_10 = QComboBox(self.frame_7)
        self.comboBox_10.setObjectName(u"comboBox_10")
        sizePolicy1.setHeightForWidth(self.comboBox_10.sizePolicy().hasHeightForWidth())
        self.comboBox_10.setSizePolicy(sizePolicy1)

        self.horizontalLayout_31.addWidget(self.comboBox_10)


        self.verticalLayout_17.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_36 = QLabel(self.frame_7)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_32.addWidget(self.label_36)

        self.lineEdit_6 = QLineEdit(self.frame_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_32.addWidget(self.lineEdit_6)

        self.label_37 = QLabel(self.frame_7)
        self.label_37.setObjectName(u"label_37")
        sizePolicy4.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy4)

        self.horizontalLayout_32.addWidget(self.label_37)

        self.comboBox_11 = QComboBox(self.frame_7)
        self.comboBox_11.setObjectName(u"comboBox_11")
        sizePolicy5.setHeightForWidth(self.comboBox_11.sizePolicy().hasHeightForWidth())
        self.comboBox_11.setSizePolicy(sizePolicy5)

        self.horizontalLayout_32.addWidget(self.comboBox_11)

        self.label_38 = QLabel(self.frame_7)
        self.label_38.setObjectName(u"label_38")
        sizePolicy4.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy4)

        self.horizontalLayout_32.addWidget(self.label_38)

        self.comboBox_12 = QComboBox(self.frame_7)
        self.comboBox_12.setObjectName(u"comboBox_12")
        sizePolicy2.setHeightForWidth(self.comboBox_12.sizePolicy().hasHeightForWidth())
        self.comboBox_12.setSizePolicy(sizePolicy2)

        self.horizontalLayout_32.addWidget(self.comboBox_12)


        self.verticalLayout_17.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")

        self.verticalLayout_17.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy8)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_21 = QVBoxLayout(self.frame_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_39 = QLabel(self.frame_3)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_36.addWidget(self.label_39)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_8)


        self.verticalLayout_18.addLayout(self.horizontalLayout_36)


        self.verticalLayout_21.addLayout(self.verticalLayout_18)

        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        icon1 = QIcon()
        icon1.addFile(u"Images/icons/icons8-ok (1).svg", QSize(), QIcon.Selected, QIcon.On)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setIcon(icon1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_21.addWidget(self.tableWidget)


        self.horizontalLayout_34.addWidget(self.frame_3)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy8.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy8)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_19 = QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_40 = QLabel(self.frame_8)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)

        self.horizontalLayout_37.addWidget(self.label_40)


        self.verticalLayout_19.addLayout(self.horizontalLayout_37)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_2)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.btn_SaveAluno = QPushButton(self.frame_8)
        self.btn_SaveAluno.setObjectName(u"btn_SaveAluno")

        self.horizontalLayout_41.addWidget(self.btn_SaveAluno)

        self.btn_CancelAluno = QPushButton(self.frame_8)
        self.btn_CancelAluno.setObjectName(u"btn_CancelAluno")

        self.horizontalLayout_41.addWidget(self.btn_CancelAluno)


        self.verticalLayout_19.addLayout(self.horizontalLayout_41)


        self.horizontalLayout_34.addWidget(self.frame_8)


        self.verticalLayout_17.addLayout(self.horizontalLayout_34)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.pagesAluno.addWidget(self.pgCadAluno)
        self.pgListAluno = QWidget()
        self.pgListAluno.setObjectName(u"pgListAluno")
        self.horizontalLayout_42 = QHBoxLayout(self.pgListAluno)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.treeWidget_2 = QTreeWidget(self.pgListAluno)
        self.treeWidget_2.setObjectName(u"treeWidget_2")

        self.horizontalLayout_42.addWidget(self.treeWidget_2)

        self.pagesAluno.addWidget(self.pgListAluno)

        self.verticalLayout_20.addWidget(self.pagesAluno)

        self.pagesGeral.addWidget(self.pageG_CadAluno)
        self.pageG_CadTurma = QWidget()
        self.pageG_CadTurma.setObjectName(u"pageG_CadTurma")
        self.verticalLayout_31 = QVBoxLayout(self.pageG_CadTurma)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frmBuscaTurma = QFrame(self.pageG_CadTurma)
        self.frmBuscaTurma.setObjectName(u"frmBuscaTurma")
        self.frmBuscaTurma.setFrameShape(QFrame.Box)
        self.frmBuscaTurma.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frmBuscaTurma)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_12)

        self.lbl_cadTurma = QLabel(self.frmBuscaTurma)
        self.lbl_cadTurma.setObjectName(u"lbl_cadTurma")

        self.horizontalLayout_53.addWidget(self.lbl_cadTurma)

        self.btn_BackListTurma = QPushButton(self.frmBuscaTurma)
        self.btn_BackListTurma.setObjectName(u"btn_BackListTurma")
        sizePolicy1.setHeightForWidth(self.btn_BackListTurma.sizePolicy().hasHeightForWidth())
        self.btn_BackListTurma.setSizePolicy(sizePolicy1)

        self.horizontalLayout_53.addWidget(self.btn_BackListTurma)

        self.btn_ExitCadTurma = QPushButton(self.frmBuscaTurma)
        self.btn_ExitCadTurma.setObjectName(u"btn_ExitCadTurma")
        sizePolicy1.setHeightForWidth(self.btn_ExitCadTurma.sizePolicy().hasHeightForWidth())
        self.btn_ExitCadTurma.setSizePolicy(sizePolicy1)
        self.btn_ExitCadTurma.setIcon(icon)
        self.btn_ExitCadTurma.setCheckable(False)
        self.btn_ExitCadTurma.setAutoRepeat(False)
        self.btn_ExitCadTurma.setAutoExclusive(False)

        self.horizontalLayout_53.addWidget(self.btn_ExitCadTurma)


        self.verticalLayout_30.addLayout(self.horizontalLayout_53)

        self.BuscaTurma = QFrame(self.frmBuscaTurma)
        self.BuscaTurma.setObjectName(u"BuscaTurma")
        self.BuscaTurma.setFrameShape(QFrame.StyledPanel)
        self.BuscaTurma.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.BuscaTurma)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.lbl_BuscaTurma = QLabel(self.BuscaTurma)
        self.lbl_BuscaTurma.setObjectName(u"lbl_BuscaTurma")

        self.horizontalLayout_54.addWidget(self.lbl_BuscaTurma)

        self.tpBusca_Turma = QComboBox(self.BuscaTurma)
        self.tpBusca_Turma.addItem("")
        self.tpBusca_Turma.addItem("")
        self.tpBusca_Turma.setObjectName(u"tpBusca_Turma")

        self.horizontalLayout_54.addWidget(self.tpBusca_Turma)

        self.Edit_BuscaTurma = QLineEdit(self.BuscaTurma)
        self.Edit_BuscaTurma.setObjectName(u"Edit_BuscaTurma")
        sizePolicy2.setHeightForWidth(self.Edit_BuscaTurma.sizePolicy().hasHeightForWidth())
        self.Edit_BuscaTurma.setSizePolicy(sizePolicy2)

        self.horizontalLayout_54.addWidget(self.Edit_BuscaTurma)


        self.verticalLayout_30.addWidget(self.BuscaTurma)

        self.fmBtn_Turma = QFrame(self.frmBuscaTurma)
        self.fmBtn_Turma.setObjectName(u"fmBtn_Turma")
        sizePolicy3.setHeightForWidth(self.fmBtn_Turma.sizePolicy().hasHeightForWidth())
        self.fmBtn_Turma.setSizePolicy(sizePolicy3)
        self.fmBtn_Turma.setFrameShape(QFrame.StyledPanel)
        self.fmBtn_Turma.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.fmBtn_Turma)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.btn_CadTurma = QPushButton(self.fmBtn_Turma)
        self.btn_CadTurma.setObjectName(u"btn_CadTurma")
        sizePolicy2.setHeightForWidth(self.btn_CadTurma.sizePolicy().hasHeightForWidth())
        self.btn_CadTurma.setSizePolicy(sizePolicy2)

        self.horizontalLayout_55.addWidget(self.btn_CadTurma)

        self.btn_AlterTurma = QPushButton(self.fmBtn_Turma)
        self.btn_AlterTurma.setObjectName(u"btn_AlterTurma")
        sizePolicy2.setHeightForWidth(self.btn_AlterTurma.sizePolicy().hasHeightForWidth())
        self.btn_AlterTurma.setSizePolicy(sizePolicy2)

        self.horizontalLayout_55.addWidget(self.btn_AlterTurma)

        self.btn_ExclTurma = QPushButton(self.fmBtn_Turma)
        self.btn_ExclTurma.setObjectName(u"btn_ExclTurma")
        sizePolicy2.setHeightForWidth(self.btn_ExclTurma.sizePolicy().hasHeightForWidth())
        self.btn_ExclTurma.setSizePolicy(sizePolicy2)

        self.horizontalLayout_55.addWidget(self.btn_ExclTurma)

        self.btn_RelatTurma = QPushButton(self.fmBtn_Turma)
        self.btn_RelatTurma.setObjectName(u"btn_RelatTurma")
        sizePolicy2.setHeightForWidth(self.btn_RelatTurma.sizePolicy().hasHeightForWidth())
        self.btn_RelatTurma.setSizePolicy(sizePolicy2)

        self.horizontalLayout_55.addWidget(self.btn_RelatTurma)


        self.verticalLayout_30.addWidget(self.fmBtn_Turma)


        self.verticalLayout_31.addWidget(self.frmBuscaTurma)

        self.pagesTurma = QStackedWidget(self.pageG_CadTurma)
        self.pagesTurma.setObjectName(u"pagesTurma")
        self.pgCadTurma = QWidget()
        self.pgCadTurma.setObjectName(u"pgCadTurma")
        self.verticalLayout_22 = QVBoxLayout(self.pgCadTurma)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_9 = QFrame(self.pgCadTurma)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_24 = QVBoxLayout(self.frame_9)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_41 = QLabel(self.frame_9)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_35.addWidget(self.label_41)

        self.checkBox_3 = QCheckBox(self.frame_9)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font)
        self.checkBox_3.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_35.addWidget(self.checkBox_3)


        self.verticalLayout_24.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_42 = QLabel(self.frame_9)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_40.addWidget(self.label_42)

        self.lineEdit_7 = QLineEdit(self.frame_9)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy2.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy2)

        self.horizontalLayout_40.addWidget(self.lineEdit_7)

        self.label_45 = QLabel(self.frame_9)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_40.addWidget(self.label_45)

        self.lineEdit_19 = QLineEdit(self.frame_9)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        sizePolicy1.setHeightForWidth(self.lineEdit_19.sizePolicy().hasHeightForWidth())
        self.lineEdit_19.setSizePolicy(sizePolicy1)

        self.horizontalLayout_40.addWidget(self.lineEdit_19)


        self.verticalLayout_24.addLayout(self.horizontalLayout_40)

        self.label_43 = QLabel(self.frame_9)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_24.addWidget(self.label_43)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_44 = QLabel(self.frame_9)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_43.addWidget(self.label_44)

        self.timeEdit = QTimeEdit(self.frame_9)
        self.timeEdit.setObjectName(u"timeEdit")

        self.horizontalLayout_43.addWidget(self.timeEdit)

        self.label_46 = QLabel(self.frame_9)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_43.addWidget(self.label_46)

        self.timeEdit_2 = QTimeEdit(self.frame_9)
        self.timeEdit_2.setObjectName(u"timeEdit_2")

        self.horizontalLayout_43.addWidget(self.timeEdit_2)

        self.checkBox_4 = QCheckBox(self.frame_9)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_43.addWidget(self.checkBox_4)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_15)


        self.verticalLayout_24.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_50 = QLabel(self.frame_9)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_45.addWidget(self.label_50)

        self.checkBox_6 = QCheckBox(self.frame_9)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setFont(font1)

        self.horizontalLayout_45.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.frame_9)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setFont(font1)

        self.horizontalLayout_45.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.frame_9)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setFont(font1)

        self.horizontalLayout_45.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.frame_9)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setFont(font1)

        self.horizontalLayout_45.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(self.frame_9)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setFont(font1)

        self.horizontalLayout_45.addWidget(self.checkBox_10)

        self.checkBox_11 = QCheckBox(self.frame_9)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setFont(font1)

        self.horizontalLayout_45.addWidget(self.checkBox_11)

        self.checkBox_12 = QCheckBox(self.frame_9)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setFont(font1)

        self.horizontalLayout_45.addWidget(self.checkBox_12)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_16)


        self.verticalLayout_24.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_47 = QLabel(self.frame_9)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_38.addWidget(self.label_47)

        self.dateEdit_3 = QDateEdit(self.frame_9)
        self.dateEdit_3.setObjectName(u"dateEdit_3")

        self.horizontalLayout_38.addWidget(self.dateEdit_3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_13)


        self.verticalLayout_24.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_49 = QLabel(self.frame_9)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_44.addWidget(self.label_49)

        self.dateEdit_4 = QDateEdit(self.frame_9)
        self.dateEdit_4.setObjectName(u"dateEdit_4")

        self.horizontalLayout_44.addWidget(self.dateEdit_4)

        self.checkBox_5 = QCheckBox(self.frame_9)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_44.addWidget(self.checkBox_5)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_14)


        self.verticalLayout_24.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_51 = QLabel(self.frame_9)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_46.addWidget(self.label_51)

        self.comboBox_13 = QComboBox(self.frame_9)
        self.comboBox_13.setObjectName(u"comboBox_13")
        sizePolicy2.setHeightForWidth(self.comboBox_13.sizePolicy().hasHeightForWidth())
        self.comboBox_13.setSizePolicy(sizePolicy2)

        self.horizontalLayout_46.addWidget(self.comboBox_13)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_17)


        self.verticalLayout_24.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_52 = QLabel(self.frame_9)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_47.addWidget(self.label_52)

        self.label_53 = QLabel(self.frame_9)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_47.addWidget(self.label_53)

        self.EditVlTurma = QLineEdit(self.frame_9)
        self.EditVlTurma.setObjectName(u"EditVlTurma")
        sizePolicy1.setHeightForWidth(self.EditVlTurma.sizePolicy().hasHeightForWidth())
        self.EditVlTurma.setSizePolicy(sizePolicy1)

        self.horizontalLayout_47.addWidget(self.EditVlTurma)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_18)


        self.verticalLayout_24.addLayout(self.horizontalLayout_47)

        self.label_48 = QLabel(self.frame_9)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_24.addWidget(self.label_48)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.plainTextEdit = QPlainTextEdit(self.frame_9)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_39.addWidget(self.plainTextEdit)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalSpacer_3 = QSpacerItem(20, 234, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_3)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.btn_SaveTurma = QPushButton(self.frame_10)
        self.btn_SaveTurma.setObjectName(u"btn_SaveTurma")

        self.horizontalLayout_48.addWidget(self.btn_SaveTurma)

        self.btn_CancelTurma = QPushButton(self.frame_10)
        self.btn_CancelTurma.setObjectName(u"btn_CancelTurma")

        self.horizontalLayout_48.addWidget(self.btn_CancelTurma)


        self.verticalLayout_23.addLayout(self.horizontalLayout_48)


        self.horizontalLayout_39.addWidget(self.frame_10)


        self.verticalLayout_24.addLayout(self.horizontalLayout_39)


        self.verticalLayout_22.addWidget(self.frame_9)

        self.pagesTurma.addWidget(self.pgCadTurma)
        self.pgListTurma = QWidget()
        self.pgListTurma.setObjectName(u"pgListTurma")
        self.horizontalLayout_52 = QHBoxLayout(self.pgListTurma)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.treeWidget_3 = QTreeWidget(self.pgListTurma)
        self.treeWidget_3.setObjectName(u"treeWidget_3")

        self.horizontalLayout_52.addWidget(self.treeWidget_3)

        self.pagesTurma.addWidget(self.pgListTurma)

        self.verticalLayout_31.addWidget(self.pagesTurma)

        self.pagesGeral.addWidget(self.pageG_CadTurma)

        self.verticalLayout_6.addWidget(self.pagesGeral)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 830, 21))
        self.menuCadastros = QMenu(self.menubar)
        self.menuCadastros.setObjectName(u"menuCadastros")
        self.menuFinanceiro = QMenu(self.menubar)
        self.menuFinanceiro.setObjectName(u"menuFinanceiro")
        self.menuInicio = QMenu(self.menubar)
        self.menuInicio.setObjectName(u"menuInicio")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuInicio.menuAction())
        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuFinanceiro.menuAction())
        self.menuCadastros.addAction(self.actionFuncionarios)
        self.menuCadastros.addAction(self.actionAlunos)
        self.menuCadastros.addAction(self.actionTurmas)
        self.menuInicio.addAction(self.actionVoltar)
        self.menuInicio.addAction(self.actionSair)

        self.retranslateUi(MainWindow)

        self.pagesGeral.setCurrentIndex(0)
        self.pagesFuncionario.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.pagesAluno.setCurrentIndex(1)
        self.pagesTurma.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionFuncionarios.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rios", None))
        self.actionAlunos.setText(QCoreApplication.translate("MainWindow", u"Alunos", None))
        self.actionTurmas.setText(QCoreApplication.translate("MainWindow", u"Turmas", None))
        self.actionVoltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.actionSair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src = \"Images/GonSystem.png\"><br/></p></body></html>", None))
        self.lbl_cadFuncionario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Cadastros de Funcion\u00e1rios</span></p></body></html>", None))
        self.btn_BackListFuncionario.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.btn_ExitCadFuncionario.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.lbl_BuscaFuncionario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Buscar:</span></p></body></html>", None))
        self.tpBusca_Funcionario.setItemText(0, QCoreApplication.translate("MainWindow", u"Nome", None))
        self.tpBusca_Funcionario.setItemText(1, QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))

        self.btn_CadFuncionario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_AlterFuncionario.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_ExclFuncionario.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_RelatFuncionario.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Dados do Funcion\u00e1rio</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio Ativo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">RG:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Telefone:</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Matr\u00edcula:</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">UF:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">CPF:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Data de Nascimento:</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Endere\u00e7o</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Endere\u00e7o:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Bairro:</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Cidade:</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Estado:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">CEP:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Cargo:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Setor:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Permiss\u00f5es</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Cont\u00e9m Login?</span></p></body></html>", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Login:</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Senha:</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Confirmar Senha:</span></p></body></html>", None))
        self.btn_SaveFuncionario.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_CancelFuncionario.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Setor", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Cargo", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Nascimento", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None));
        self.lbl_cadAluno.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Cadastros de Alunos</span></p></body></html>", None))
        self.btn_BackListAluno.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.btn_ExitCadAluno.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.lbl_BuscaaAluno.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Buscar:</span></p></body></html>", None))
        self.tpBusca_Aluno.setItemText(0, QCoreApplication.translate("MainWindow", u"Nome", None))
        self.tpBusca_Aluno.setItemText(1, QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))

        self.btn_CadAluno.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_AlterAluno.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_ExclAluno.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_RelatAluno.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Dados do Aluno</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Aluno Ativo", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome:</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">RG:</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Telefone:</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Matr\u00edcula:</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">UF:</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">CPF:</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Data de Nascimento:</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Endere\u00e7o</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Endere\u00e7o:</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Bairro:</span></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Cidade:</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Estado:</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">CEP:</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Cargo:</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Setor:</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turmas</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Modalidade", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Instrutor", None));
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Planos</span></p></body></html>", None))
        self.btn_SaveAluno.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_CancelAluno.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        ___qtreewidgetitem1 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Nascimento", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None));
        self.lbl_cadTurma.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Cadastros de Turmas</span></p></body></html>", None))
        self.btn_BackListTurma.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.btn_ExitCadTurma.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.lbl_BuscaTurma.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Buscar:</span></p></body></html>", None))
        self.tpBusca_Turma.setItemText(0, QCoreApplication.translate("MainWindow", u"Nome", None))
        self.tpBusca_Turma.setItemText(1, QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))

        self.btn_CadTurma.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_AlterTurma.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_ExclTurma.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_RelatTurma.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Turma</span></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Turma Ativo", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome:</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">C\u00f3digo:</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hor\u00e1rios</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">In\u00edcio:</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Fim:</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Sem hor\u00e1rio fixo", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Dia:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.checkBox_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Domingo", None))
#if QT_CONFIG(tooltip)
        self.checkBox_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Segunda", None))
#if QT_CONFIG(tooltip)
        self.checkBox_8.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Ter\u00e7a", None))
#if QT_CONFIG(tooltip)
        self.checkBox_9.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Quarta", None))
#if QT_CONFIG(tooltip)
        self.checkBox_10.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Quinta", None))
#if QT_CONFIG(tooltip)
        self.checkBox_11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"Sexta", None))
#if QT_CONFIG(tooltip)
        self.checkBox_12.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"S\u00e1bado", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Data de in\u00edcio da turma:</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Data de finaliza\u00e7\u00e3o da turma:</span></p></body></html>", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Sem data de Finaliza\u00e7\u00e3o", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Instrutor:</span></p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Valor:</span></p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">R$</span></p></body></html>", None))
        self.EditVlTurma.setInputMask("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Descri\u00e7\u00e3o da Turma:</span></p></body></html>", None))
        self.btn_SaveTurma.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_CancelTurma.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        ___qtreewidgetitem2 = self.treeWidget_3.headerItem()
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"Hor\u00e1rio Fim", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Hor\u00e1rio In\u00edcio", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        self.menuCadastros.setTitle(QCoreApplication.translate("MainWindow", u"Cadastros", None))
        self.menuFinanceiro.setTitle(QCoreApplication.translate("MainWindow", u"Financeiro", None))
        self.menuInicio.setTitle(QCoreApplication.translate("MainWindow", u"Inicio", None))
    # retranslateUi

