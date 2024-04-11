from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(911, 642)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"resources/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLabel {\n"
"  	padding: 10px;\n"
"  	border: none;\n"
"  	border-radius: 5px;\n"
"  	background-color: #f5f5f5;\n"
"  	width: 100%;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	outline: none;\n"
" 	background-color: #fff;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	background-color: rgb(75, 75, 75);\n"
"	color: rgb(75, 75, 75);\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"	padding: 10px 20px;\n"
"}\n"
"    \n"
"QPushButton:hover {\n"
"	background-color: #686868;\n"
"}\n"
"\n"
"QTextEdit {\n"
"  	padding: 10px;\n"
"	padding-left: 24px;\n"
"	padding-top: 24px;\n"
"  	border: none;\n"
"  	border-radius: 5px;\n"
"  	background-color: #f5f5f5;\n"
"  	width: 100%;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"	outline: none;\n"
" 	background-color: #fff;\n"
"}")
        self.inpt = QTextEdit(self.centralwidget)
        self.inpt.setObjectName(u"inpt")
        self.inpt.setGeometry(QRect(2, 0, 909, 221))
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(18)
        self.inpt.setFont(font)
        self.inpt.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.inpt.setStyleSheet(u"")
        self.inpt.setFrameShape(QFrame.Box)
        self.inpt.setFrameShadow(QFrame.Plain)
        self.inpt.setLineWidth(1)
        self.inpt.setMidLineWidth(0)
        self.inpt.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.inpt.setAcceptRichText(False)
        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(800, 160, 101, 50))
        icon1 = QIcon()
        icon1.addFile(u"resources/generate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button.setIcon(icon1)
        self.button.setIconSize(QSize(48, 22))
        self.speak_button = QPushButton(self.centralwidget)
        self.speak_button.setObjectName(u"speak_button")
        self.speak_button.setGeometry(QRect(840, 580, 50, 50))
        icon2 = QIcon()
        icon2.addFile(u"resources/vol.png", QSize(), QIcon.Normal, QIcon.Off)
        self.speak_button.setIcon(icon2)
        self.speak_button.setIconSize(QSize(48, 20))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(1, 230, 909, 411))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 909, 411))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.output_label = QLabel(self.scrollAreaWidgetContents)
        self.output_label.setObjectName(u"output_label")
        font1 = QFont()
        font1.setFamilies([u"Dubai"])
        font1.setPointSize(16)
        self.output_label.setFont(font1)
        self.output_label.setCursor(QCursor(Qt.IBeamCursor))
        self.output_label.setWordWrap(True)
        self.output_label.setMargin(24)
        self.output_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.output_label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.talk_button = QPushButton(self.centralwidget)
        self.talk_button.setObjectName(u"talk_button")
        self.talk_button.setGeometry(QRect(740, 160, 50, 50))
        icon3 = QIcon()
        icon3.addFile(u"resources/talk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.talk_button.setIcon(icon3)
        self.talk_button.setIconSize(QSize(48, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.inpt.raise_()
        self.button.raise_()
        self.scrollArea.raise_()
        self.speak_button.raise_()
        self.talk_button.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Virtual Chef", None))
        self.inpt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Dubai'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.inpt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the name of a dish or the ingredients you have at hand", None))
#if QT_CONFIG(tooltip)
        self.button.setToolTip(QCoreApplication.translate("MainWindow", u"Submit", None))
#endif // QT_CONFIG(tooltip)
        self.button.setText("")
#if QT_CONFIG(tooltip)
        self.speak_button.setToolTip(QCoreApplication.translate("MainWindow", u"speak out the recipe", None))
#endif // QT_CONFIG(tooltip)
        self.speak_button.setText("")
        self.output_label.setText("")
#if QT_CONFIG(tooltip)
        self.talk_button.setToolTip(QCoreApplication.translate("MainWindow", u"Speech", None))
#endif // QT_CONFIG(tooltip)
        self.talk_button.setText("")
    # retranslateUi

