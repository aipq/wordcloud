from PyQt6 import QtCore, QtWidgets


class Ui_wordcloud(object):
    def setupUi(self, wordcloud):
        wordcloud.setObjectName("wordcloud")
        wordcloud.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(wordcloud)
        self.pushButton.setGeometry(QtCore.QRect(160, 240, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.inputpath_file = QtWidgets.QPushButton(wordcloud)
        self.inputpath_file.setGeometry(QtCore.QRect(290, 30, 61, 26))
        self.inputpath_file.setObjectName("inputpath_file")
        self.inputpath = QtWidgets.QLineEdit(wordcloud)
        self.inputpath.setGeometry(QtCore.QRect(92, 30, 201, 26))
        self.inputpath.setObjectName("inputpath")
        self.txt_label = QtWidgets.QLabel(wordcloud)
        self.txt_label.setGeometry(QtCore.QRect(30, 30, 58, 21))
        self.txt_label.setObjectName("txt_label")
        self.pacture_label = QtWidgets.QLabel(wordcloud)
        self.pacture_label.setGeometry(QtCore.QRect(30, 70, 58, 21))
        self.pacture_label.setObjectName("pacture_label")
        self.pactuer_path = QtWidgets.QLineEdit(wordcloud)
        self.pactuer_path.setGeometry(QtCore.QRect(90, 70, 201, 26))
        self.pactuer_path.setObjectName("pactuer_path")
        self.input_wallpaper = QtWidgets.QPushButton(wordcloud)
        self.input_wallpaper.setGeometry(QtCore.QRect(290, 70, 61, 26))
        self.input_wallpaper.setObjectName("input_wallpaper")
        self.out_label = QtWidgets.QLabel(wordcloud)
        self.out_label.setGeometry(QtCore.QRect(30, 110, 58, 21))
        self.out_label.setObjectName("out_label")
        self.output_path = QtWidgets.QLineEdit(wordcloud)
        self.output_path.setGeometry(QtCore.QRect(90, 110, 201, 26))
        self.output_path.setObjectName("output_path")
        self.outputpath_file = QtWidgets.QPushButton(wordcloud)
        self.outputpath_file.setGeometry(QtCore.QRect(290, 110, 71, 26))
        self.outputpath_file.setObjectName("outputpath_file")
        self.switch_stopword = QtWidgets.QCheckBox(wordcloud)
        self.switch_stopword.setGeometry(QtCore.QRect(270, 270, 121, 24))
        self.switch_stopword.setObjectName("switch_stopword")
        self.stopword_file = QtWidgets.QPushButton(wordcloud)
        self.stopword_file.setGeometry(QtCore.QRect(290, 150, 61, 26))
        self.stopword_file.setObjectName("stopword_file")
        self.stopword_path = QtWidgets.QLineEdit(wordcloud)
        self.stopword_path.setGeometry(QtCore.QRect(202, 150, 91, 26))
        self.stopword_path.setObjectName("stopword_path")
        self.select_font = QtWidgets.QComboBox(wordcloud)
        self.select_font.setGeometry(QtCore.QRect(90, 150, 101, 26))
        self.select_font.setObjectName("select_font")
        self.label = QtWidgets.QLabel(wordcloud)
        self.label.setGeometry(QtCore.QRect(50, 150, 31, 21))
        self.label.setObjectName("label")
        self.backcolor_lable = QtWidgets.QLabel(wordcloud)
        self.backcolor_lable.setGeometry(QtCore.QRect(40, 190, 41, 18))
        self.backcolor_lable.setObjectName("backcolor_lable")
        self.select_backbox = QtWidgets.QComboBox(wordcloud)
        self.select_backbox.setGeometry(QtCore.QRect(90, 190, 61, 26))
        self.select_backbox.setObjectName("select_backbox")

        # 设置默认值为True
        self.switch_stopword.setChecked(True)

        self.retranslateUi(wordcloud)
        self.pushButton.clicked.connect(wordcloud.run)  # type: ignore
        self.inputpath_file.clicked.connect(wordcloud.open)  # type: ignore
        self.input_wallpaper.clicked.connect(wordcloud.open)  # type: ignore
        self.outputpath_file.clicked.connect(wordcloud.openpath)  # type: ignore
        self.inputpath.editingFinished.connect(wordcloud.inputpath_txt)  # type: ignore
        self.pactuer_path.editingFinished.connect(wordcloud.inputpath_wallpaper)  # type: ignore
        self.output_path.editingFinished.connect(wordcloud.inputpath_out)  # type: ignore
        self.stopword_file.clicked.connect(wordcloud.open_stopword)  # type: ignore
        self.stopword_path.editingFinished.connect(wordcloud.input_stopword_path)  # type: ignore
        #self.pushButton.clicked.connect(self.select_font.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(wordcloud)

    def retranslateUi(self, wordcloud):
        _translate = QtCore.QCoreApplication.translate
        wordcloud.setWindowTitle(_translate("wordcloud", "wordcloud"))
        self.pushButton.setText(_translate("wordcloud", "运行"))
        self.inputpath_file.setText(_translate("wordcloud", "浏览文件"))
        self.txt_label.setText(_translate("wordcloud", "文本文件"))
        self.pacture_label.setText(_translate("wordcloud", "背景图片"))
        self.input_wallpaper.setText(_translate("wordcloud", "浏览文件"))
        self.out_label.setText(_translate("wordcloud", "输出文件"))
        self.outputpath_file.setText(_translate("wordcloud", "输出文件夹"))
        self.switch_stopword.setText(_translate("wordcloud", "开启/关闭停用词"))
        self.stopword_file.setText(_translate("wordcloud", "停用词"))
        self.label.setText(_translate("wordcloud", "字体"))
        self.backcolor_lable.setText(_translate("wordcloud", "背景色"))


