# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import getopt, parser, datetime, codecs, sqlite3
import analysis
import pandas as pd
import pandas
import matplotlib.pyplot as plt
import sqlite3
from PyQt5 import QtGui, QtWidgets

conn = sqlite3.connect('../TweetAnalysis.db')
conn.row_factory = lambda cursor, row: row[1]
c = conn.cursor()
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, So):
        So.setObjectName(_fromUtf8("So"))
        So.resize(735, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../.designer/backup/socailMediaTrends.jpg")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        So.setWindowIcon(icon)
        So.setStyleSheet(_fromUtf8("background-color:rgb(16, 170, 5)"))
        self.centralwidget = QtWidgets.QWidget(So)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 380, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(65, 65, 65); color:rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 380, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(65, 65, 65); color:rgb(255, 255, 255);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(480, 100, 113, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 150, 113, 27))
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 100, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 150, 71, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 200, 90, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 260, 90, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 320, 68, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(480, 320, 113, 27))
        self.lineEdit_5.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.lineEdit_5.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.label.setStyleSheet(_fromUtf8("color:white"))
        self.label_2.setStyleSheet(_fromUtf8("color:white"))
        self.label_3.setStyleSheet(_fromUtf8("color:white"))
        self.label_4.setStyleSheet(_fromUtf8("color:white"))
        self.label_5.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_5.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(480, 200, 113, 27))
        self.lineEdit_3.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(480, 260, 113, 27))
        self.lineEdit_4.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 20, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background-color:rgb(16, 170, 5); color: white;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pic_label = QtWidgets.QLabel(self.centralwidget)
        self.pic_label.setGeometry(QtCore.QRect(40, 70, 291, 361))
        self.pic_label.setPixmap(QtGui.QPixmap("../" + "/images/app_icon.png"))

        self.pic_label.setObjectName(_fromUtf8("pic_label"))
        So.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(So)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        So.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(So)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        So.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(So)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAnalysis = QtWidgets.QAction(So)
        self.actionAnalysis.setObjectName(_fromUtf8("actionAnalysis"))
        self.actionExit_2 = QtWidgets.QAction(So)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.pushButton_3 = QtWidgets.QAction(So)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/socailMediaTrends.jpg")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionAnalysis)
        self.menuFile.addAction(self.actionExit_2)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(So)
        QtCore.QMetaObject.connectSlotsByName(So)

    def retranslateUi(self, So):
        So.setWindowTitle(_translate("So", "Social Network Tracking And Analysis", None))
        self.pushButton.setText(_translate("So", "Tracking", None))
        self.pushButton.clicked.connect(self.tracking)  # When the button is pressed

        self.pushButton_2.setText(_translate("So", "Analysis", None))
        self.pushButton_2.clicked.connect(self.analysis_tweet)  # When the button is pressed

        self.label.setText(_translate("So", "Query:", None))
        self.label_2.setText(_translate("So", "Username:", None))
        self.label_3.setText(_translate("So", "Since:(y-d-m)", None))
        self.label_4.setText(_translate("So", "Until:(y-d-m)", None))
        self.label_5.setText(_translate("So", "Quantity:", None))
        self.label_6.setText(_translate("So", "Social Network  Tracking And Analysis", None))
        self.pic_label.setText(_translate("So", "", None))
        self.menuFile.setTitle(_translate("So", "File", None))
        self.menuHelp.setTitle(_translate("So", "Help", None))
        self.actionExit.setText(_translate("So", "Tracking", None))
        self.actionAnalysis.setText(_translate("So", "Analysis", None))
        self.actionExit_2.setText(_translate("So", "Exit", None))
        self.pushButton_3.setText(_translate("So", "deneme", None))

    def analysis_tweet(self):
        analysis.analysis_graph()

    def tracking(self):
        tweet_criteria = parser.operation.TweetCriteria()

        tweet_criteria.username = self.lineEdit_2.text()
        tweet_criteria.query = self.lineEdit.text()
        if (self.lineEdit_3.text() != ""):
            tweet_criteria.since = self.lineEdit_3.text()
        if (self.lineEdit_4.text() != ""):
            tweet_criteria.until = self.lineEdit_4.text()
        if (self.lineEdit_5.text() != ""):
            tweet_criteria.maxTweets = int(self.lineEdit_5.text())

        print('Searching...\n')

        def receiveBuffer(tweets):
            locationid = 1;
            hashtagid = 1;
            for t in tweets:
                hashtagstring = t.hashtags
                # userchefck = t.username
                str = hashtagstring.split()
                # print(usercheck)
                # serstr=usercheck.split()

                for hash in str:
                    # hash_list.append(hash)
                    paramsHashtag = (hashtagid, hash)
                    paramsHashagTweet = (hashtagid, t.id)
                    if hash != "":
                        hashtagid = hashtagid + 1
                        c.execute("SELECT * FROM hashtag where content = '%s'" % hash)
                        # aynı içeriğin olup olmama kontrolü
                        exits = c.fetchone()
                        if exits is None:
                            c.execute("SELECT hashtag FROM tweet ")

                            c.execute("INSERT OR IGNORE INTO HashtagTweet VALUES (?,?)", paramsHashagTweet)
                            c.execute("INSERT OR IGNORE INTO Hashtag  VALUES (?,?)", paramsHashtag)

                a = t.date.strftime('%H:%M')

                paramsTweet = (
                    t.id, t.text, t.username, t.hashtags, t.date.strftime('%Y-%m-%d'), t.date.strftime('%H:%M'),
                    t.retweets,
                    t.favorites, t.mentions, t.user_id, locationid)

                c.execute("SELECT * FROM Tweet where tweetid ='%s'" % t.id)
                userexist = c.fetchone()
                if userexist is None:
                    c.execute("INSERT INTO Tweet VALUES (?,?,?,?,?,?,?,?,?,?,?)", paramsTweet)

                # aynı içeriğin olup olmama kontrolü

                # geolocator = Nominatim()
                # location = geolocator.geocode("")
                # print(location)
                paramsLocation = (locationid, t.geo)
                c.execute("SELECT * FROM location where place = '%s'" % t.geo)
                locationexist = c.fetchone()
                if locationexist is None and t.geo != '':
                    c.execute("INSERT INTO Location VALUES(?,?)", paramsLocation)
                    locationid = locationid + 1

                c.execute("SELECT *FROM location where place = '%s'" % t.geo)
                locatuid = c.fetchone()
                paramsUser = (t.user_id, t.username, locatuid, t.follow, t.follower)
                c.execute("SELECT * FROM user where username ='%s'" % t.username)
                userexist = c.fetchone()
                if userexist is None:
                    c.execute("INSERT OR IGNORE INTO User VALUES(?,?,?,?,?)", paramsUser)

                conn.commit()
            print('Veritabanına %d tweet daha kaydedildi...\n' % len(tweets))

        parser.operation.TweetManager.get_tweets(tweet_criteria, receiveBuffer)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
