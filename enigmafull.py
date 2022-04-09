#ENIGMA

# imports
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QShortcut
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence, QImage, QPixmap 
from PyQt5.QtCore import QThread, QTime, QTimer
from PyQt5 import uic
import time
import sys
import requests
import datetime

# enigma's interface

class Ui_SCRAMBLEPY(object):
    def setupUi(self, SCRAMBLEPY):
        SCRAMBLEPY.setObjectName("SCRAMBLEPY")
        SCRAMBLEPY.setEnabled(True)
        width = 1206
        height = 905
        SCRAMBLEPY.setFixedSize(width, height)
        font = QtGui.QFont()
        font.setPointSize(16)
        SCRAMBLEPY.setFont(font)
        SCRAMBLEPY.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(SCRAMBLEPY)
        self.centralwidget.setStyleSheet("background-color: #22222e\n"
"")
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.ll = QPixmap("Enigma_logo.png")
        self.label.setGeometry(QtCore.QRect(20, 0, 231, 121))
        font = QtGui.QFont()
        font.setFamily("Genesys")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white\n"
"")
        self.label.setText("")
        self.label.setPixmap(self.ll) 
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(270, 100, 721, 191))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(19)
        self.textBrowser.setFont(font)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setStyleSheet("color: #c3c3c3;\n"
"border: 0px solid #000000;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 570, 371, 331))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")


        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 300, 501, 181))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(54)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: white;\n"
"border: 0px solid #000000;\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        

        #self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_2.setGeometry(QtCore.QRect(400, 430, 201, 71))
        #font = QtGui.QFont()
        #font.setFamily("Nirmala UI")
        #font.setPointSize(20)
        #self.pushButton_2.setFont(font)
        #self.pushButton_2.setStyleSheet("QPushButton {\n"
#"    color: black;\n"
#"    background-color: #eefe37;\n"
#"    border-radius: 15;\n"
#"\n"
#"}\n"
#"\n"
#"QPushButton:pressed {\n"
#"    background-color: #f1d500;\n"
#"}")
        #self.pushButton_2.setObjectName("pushButton_2")
        

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 130, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 15;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f1d500;\n"
"}")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        

        #self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_4.setGeometry(QtCore.QRect(630, 430, 191, 71))
        #font = QtGui.QFont()
        #font.setFamily("Nirmala UI")
        #font.setPointSize(20)
        #self.pushButton_4.setFont(font)
        #self.pushButton_4.setStyleSheet("QPushButton {\n"
#"    color: black;\n"
#"    background-color: #eefe37;\n"
#"    border-radius: 15;\n"
#"\n"
#"}\n"
#"\n"
#"QPushButton:pressed {\n"
#"    background-color: #f1d500;\n"
#"}")
        #self.pushButton_4.setObjectName("pushButton_4")
        


        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 220, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 15;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f1d500;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 310, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 15;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f1d500;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 400, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 15;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f1d500;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 490, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 15;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f1d500;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 580, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 15;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f1d500;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1070, 530, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 15;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f1d500;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_9")
        self.pushButton_10.setText("Reset")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(910, 320, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(25)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #bfbfbf")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(910, 390, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #bfbfbf\n"
"")
        self.label_6.setObjectName("label_6")
        

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1040, 590, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #bfbfbf\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("1.")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1040, 640, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #bfbfbf\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_8.setText("2.")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1040, 690, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #bfbfbf\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_9.setText("3.")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1040, 740, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #bfbfbf\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_10.setText("4.")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1040, 790, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #bfbfbf\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_11.setText("5.")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.internet = QPixmap("int.png")
        self.no_internet = QPixmap("noint.png")
        self.label_12.setGeometry(QtCore.QRect(1120, 20, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #bfbfbf\n"
"")
        self.label_12.setObjectName("label_12")


        
        







        SCRAMBLEPY.setCentralWidget(self.centralwidget)
        self.retranslateUi(SCRAMBLEPY)
        QtCore.QMetaObject.connectSlotsByName(SCRAMBLEPY)

    def retranslateUi(self, SCRAMBLEPY):
        _translate = QtCore.QCoreApplication.translate
        SCRAMBLEPY.setWindowTitle(_translate("SCRAMBLEPY", "ENIGMA"))
        self.textBrowser.setHtml(_translate("SCRAMBLEPY", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nirmala UI\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        
        self.lineEdit.setText(_translate("SCRAMBLEPY", "00:00:00:00"))
        
        #self.pushButton_2.setText(_translate("SCRAMBLEPY", "Start"))
        
        self.pushButton_3.setText(_translate("SCRAMBLEPY", "Pyraminx"))
        
        #self.pushButton_4.setText(_translate("SCRAMBLEPY", "Stop"))
        
        self.pushButton_5.setText(_translate("SCRAMBLEPY", "2x2x2"))
        self.pushButton_6.setText(_translate("SCRAMBLEPY", "3x3x3"))
        self.pushButton_7.setText(_translate("SCRAMBLEPY", "4x4x4"))
        self.pushButton_8.setText(_translate("SCRAMBLEPY", "5x5x5"))
        self.pushButton_9.setText(_translate("SCRAMBLEPY", "6x6x6"))
        self.label_5.setText(_translate("SCRAMBLEPY", "ao5:"))
        self.label_6.setText(_translate("SCRAMBLEPY", "ao12:"))

        


####################################################################
#Logic

#Internet connection
def internet_connection():

        url_image = 'https://google.com/'

        timeout = 10
        try:
                request = requests.get(url_image, timeout=timeout)
                ui.label_12.setPixmap(ui.internet)
        except (requests.ConnectionError, requests.Timeout) as exception:
                ui.label_12.setPixmap(ui.no_internet)

###### Cube buttons
def cube2x2():

    url_image = 'https://google.com/'

    timeout = 10
    try:
        request = requests.get(url_image, timeout=timeout)
        ui.label_12.setPixmap(ui.internet)
        puzzle_api = "2"
        puzzle = "2x2x2"

        s = "http://scrambler-api.herokuapp.com/" + puzzle
        scramble = ""
        scramble = requests.get(s)
        scramble = scramble.text
        scramble = scramble.split(",")[0]
        scramble = scramble.replace("[", "")
        scramble = scramble.replace("]", "")
        scramble = scramble.replace('"', "")
        ui.textBrowser.setText(scramble)

        #Image genereation

        scramble_api = scramble.replace(' ', "")
        loadfrom = requests.get("http://cube.rider.biz/visualcube.php?fmt=png&size=370&sch=wrgyob&pzl=" + str(puzzle_api) + "&alg=" + str(scramble_api))
        image = QImage()
        image.loadFromData(loadfrom.content)
        ui.label_4.setPixmap(QPixmap(image))
        ui.label_4.show()

    except (requests.ConnectionError, requests.Timeout) as exception:
        ui.label_12.setPixmap(ui.no_internet)
        ui.textBrowser.setText("No internet connection or server is not avaible!")

    


def cube3x3():

    url_image = 'https://google.com/'

    timeout = 10
    try:
        request = requests.get(url_image, timeout=timeout)
        ui.label_12.setPixmap(ui.internet)
        puzzle_api = 3
        puzzle = "3x3x3"

        s = "http://scrambler-api.herokuapp.com/" + puzzle
        scramble = ""
        scramble = requests.get(s)
        scramble = scramble.text
        scramble = scramble.split(",")[0]
        scramble = scramble.replace("[", "")
        scramble = scramble.replace("]", "")
        scramble = scramble.replace('"', "")
        ui.textBrowser.setText(scramble)

        #Image genereation

        scramble_api = scramble.replace(' ', "")
        loadfrom = requests.get("http://cube.rider.biz/visualcube.php?fmt=png&size=370&sch=wrgyob&pzl=" + str(puzzle_api) + "&alg=" + str(scramble_api))
        image = QImage()
        image.loadFromData(loadfrom.content)
        ui.label_4.setPixmap(QPixmap(image))
        ui.label_4.show()

    except (requests.ConnectionError, requests.Timeout) as exception:
        ui.label_12.setPixmap(ui.no_internet)
        ui.textBrowser.setText("No internet connection or server is not avaible!")
    


def cube4x4():

    url_image = 'https://google.com/'

    timeout = 10
    try:
        request = requests.get(url_image, timeout=timeout)
        ui.label_12.setPixmap(ui.internet)
        puzzle_api = "4"
        puzzle = "4x4x4"

        s = "http://scrambler-api.herokuapp.com/" + puzzle
        scramble = ""
        scramble = requests.get(s)
        scramble = scramble.text
        scramble = scramble.split(",")[0]
        scramble = scramble.replace("[", "")
        scramble = scramble.replace("]", "")
        scramble = scramble.replace('"', "")
        ui.textBrowser.setText(scramble)

        #Image genereation

        scramble_api = scramble.replace(' ', "")
        loadfrom = requests.get("http://cube.rider.biz/visualcube.php?fmt=png&size=370&sch=wrgyob&pzl=" + str(puzzle_api) + "&alg=" + str(scramble_api))
        image = QImage()
        image.loadFromData(loadfrom.content)
        ui.label_4.setPixmap(QPixmap(image))
        ui.label_4.show()

    except (requests.ConnectionError, requests.Timeout) as exception:
        ui.label_12.setPixmap(ui.no_internet)
        ui.textBrowser.setText("No internet connection or server is not avaible!")

def cube5x5():

    url_image = 'https://google.com/'

    timeout = 10
    try:
        request = requests.get(url_image, timeout=timeout)
        ui.label_12.setPixmap(ui.internet)
        puzzle_api = "5"
        puzzle = "5x5x5"

        s = "http://scrambler-api.herokuapp.com/" + puzzle
        scramble = ""
        scramble = requests.get(s)
        scramble = scramble.text
        scramble = scramble.split(",")[0]
        scramble = scramble.replace("[", "")
        scramble = scramble.replace("]", "")
        scramble = scramble.replace('"', "")
        ui.textBrowser.setText(scramble)

        #Image genereation

        scramble_api = scramble.replace(' ', "")
        loadfrom = requests.get("http://cube.rider.biz/visualcube.php?fmt=png&size=370&sch=wrgyob&pzl=" + str(puzzle_api) + "&alg=" + str(scramble_api))
        image = QImage()
        image.loadFromData(loadfrom.content)
        ui.label_4.setPixmap(QPixmap(image))
        ui.label_4.show()

    except (requests.ConnectionError, requests.Timeout) as exception:
        ui.label_12.setPixmap(ui.no_internet)
        ui.textBrowser.setText("No internet connection or server is not avaible!")

def cube6x6():

    url_image = 'https://google.com/'

    timeout = 10
    try:
        request = requests.get(url_image, timeout=timeout)
        ui.label_12.setPixmap(ui.internet)
        puzzle_api = 6
        puzzle = "6x6x6"

        s = "http://scrambler-api.herokuapp.com/" + puzzle
        scramble = ""
        scramble = requests.get(s)
        scramble = scramble.text
        scramble = scramble.split(",")[0]
        scramble = scramble.replace("[", "")
        scramble = scramble.replace("]", "")
        scramble = scramble.replace('"', "")
        ui.textBrowser.setText(scramble)

        #Image genereation

        scramble_api = scramble.replace(' ', "")
        loadfrom = requests.get("http://cube.rider.biz/visualcube.php?fmt=png&size=370&sch=wrgyob&pzl=" + str(puzzle_api) + "&alg=" + str(scramble_api))
        image = QImage()
        image.loadFromData(loadfrom.content)
        ui.label_4.setPixmap(QPixmap(image))
        ui.label_4.show()

    except (requests.ConnectionError, requests.Timeout) as exception:
        ui.label_12.setPixmap(ui.no_internet)
        ui.textBrowser.setText("No internet connection or server is not avaible!")

def pyramidka():

    url_image = 'https://google.com/'

    timeout = 10
    try:
        request = requests.get(url_image, timeout=timeout)
        ui.label_12.setPixmap(ui.internet)
        

        puzzle = "pyraminx"

        s = "http://scrambler-api.herokuapp.com/" + puzzle
        scramble = ""
        scramble = requests.get(s)
        scramble = scramble.text
        scramble = scramble.split(",")[0]
        scramble = scramble.replace("[", "")
        scramble = scramble.replace("]", "")
        scramble = scramble.replace('"', "")
        ui.textBrowser.setText(scramble)
        ui.label_4.setText(".")

    except (requests.ConnectionError, requests.Timeout) as exception:
        ui.label_12.setPixmap(ui.no_internet)
        ui.textBrowser.setText("No internet connection or server is not avaible!")
    
    
    
###### Stopwatch

isStart = False
startTime = datetime.datetime.now()
time_delta = datetime.datetime.now()

def start():
        global timer, startTime
        startTime = datetime.datetime.now()
        timer.start( 1 )
        

def stop():
        global timer
        timer.stop()

        Avg5.append(time_delta)

        Avg12.append(time_delta)
        if len(Avg5) == 5:
           average_timedelta = sum(Avg5, datetime.timedelta(0)) / len(Avg5) 
           ui.label_5.setText("ao5: " + str(average_timedelta)[:-4]) 
        if len(Avg12) == 12:
                average_timedelta_2 = sum(Avg12, datetime.timedelta(0)) / len(Avg12) 
                ui.label_6.setText("ao12: " + str(average_timedelta_2)[:-4]) 
        
        #last 5 attempt

        if len(Avg5) == 1:
                ui.label_7.setText("1." + str(Avg5[0]))
        if len(Avg5) == 2:
                ui.label_8.setText("2." + str(Avg5[1]))
        if len(Avg5) == 3:
                ui.label_9.setText("3." + str(Avg5[2]))
        if len(Avg5) == 4:
                ui.label_10.setText("4." + str(Avg5[3]))
        if len(Avg5) == 5:
                ui.label_11.setText("5." + str(Avg5[4]))
        if len(Avg5) == 6:
                Avg5.clear()
                Avg5.append(time_delta)
                reset_lables()
                ui.label_7.setText("1." + str(Avg5[0]))
                ui.label_5.setText("ao5:")
        #Update Ao12
        if len(Avg12) == 13:
                Avg12.clear()
                Avg12.append(time_delta)
                ui.label_6.setText("ao12:")


def timerFunction():
        global time_delta, startTime
        time_delta = datetime.datetime.now() - startTime
        ui.lineEdit.setText(str(time_delta)[:-4] )


#Reset Lables

def reset_lables():
        ui.label_7.setText("1.")
        ui.label_8.setText("2.")
        ui.label_9.setText("3.")
        ui.label_10.setText("4.")
        ui.label_11.setText("5.")

#Reset all attempts with reset button
def ResetAttemtpsLablesAndAO5():
        reset_lables()
        Avg5.clear()
        ui.label_5.setText("ao5:")
        Avg12.clear()
        ui.label_6.setText("ao12:")

#For space bind
def OnKeyPressHandler():
    global isStart
    if isStart == False:
       start()
       isStart = True
    else:
       stop()
       isStart = False



#AO5 list
Avg5 = []

#AO12 list
Avg12 = []



#end logic
###################################



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SCRAMBLEPY = QtWidgets.QMainWindow()
    ui = Ui_SCRAMBLEPY()
    ui.setupUi(SCRAMBLEPY)
    SCRAMBLEPY.show()

    internet_connection()

    #Buttons
    ui.pushButton_6.clicked.connect( cube3x3 )
    ui.pushButton_5.clicked.connect( cube2x2 )
    #ui.pushButton_2.clicked.connect( start )
    #ui.pushButton_4.clicked.connect( stop )
    ui.pushButton_7.clicked.connect( cube4x4 )
    ui.pushButton_8.clicked.connect( cube5x5 )
    ui.pushButton_9.clicked.connect( cube6x6 )
    ui.pushButton_3.clicked.connect( pyramidka )
    ui.pushButton_10.clicked.connect( ResetAttemtpsLablesAndAO5 )

#####
#Bind
    SCRAMBLEPY.shortcut_open = QShortcut(QKeySequence('Space'), SCRAMBLEPY)
    SCRAMBLEPY.shortcut_open.activated.connect(OnKeyPressHandler)
######
    timer = QtCore.QTimer()
    timer.timeout.connect( timerFunction )
######
    

    sys.exit(app.exec_())