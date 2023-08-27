import sys
# from PyQt5.QtWidgets import  QApplication,QWidget,QMainWindow
import time
import pymysql
import os

from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QSize
from PySide2.QtGui import QPainter, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget, QSizePolicy
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QFileDialog
from openCV import OCRcode

# os.environ["QT_FONT_DPI"] = "1" # FIX Pro


# blem for High DPI and Scale above 100%

class MainWindow(QMainWindow):
    def __init__(self):
        # super(MainWindow,self).__init__()
        # self.ui= Ui_MainWindow()
        # self.ui.setupUi(self)
        # self.band()
        self.ui=QUiLoader().load("test.ui")
        self.band()
        self.create_percentage_bar_chart()
        # con=pymysql.connect(host='127.0.0.1',port=3306,user="root",password="root",db='ocr')
        # cur=con.cursor()

        # 查询
        # cur.execute("select * from info")
        # info=[]
        # for i in cur.fetchall():
        #     info.append({"颜色":i[0],"电话":i[1],"日期":i[2],"时间":i[3],"行程":i[4]})
        # cur.close()
        # conn.close()
        # print(info)

        #     导出


        # data= OCRcode.OCR("img\\hebei.png", True)
        # self.insertList(data)
        # data = OCRcode.OCR("img\\testnew.jpg", True)
        # self.insertList(data)
        # 插入数据库
        # lenth = self.ui.tableWidget.rowCount()
        # for i in range(lenth):
        #     itemNow = []
        #     for j in range(5):
        #         tmp=self.ui.tableWidget.item(i,j).text()
        #         itemNow.append(tmp)
        #     cur.execute("insert into info values(%s,%s,%s,%s,%s)",(itemNow[0],itemNow[1],itemNow[2],itemNow[3],itemNow[4]))
        #
        # con.commit()
        # cur.close()
        #
        # QMessageBox.information(self.ui,"信息","额")


    # def insertList(self,data):


    def create_percentage_bar_chart(self):

        set0 = QtCharts.QBarSet("Tesla")
        set1 = QtCharts.QBarSet("Google")
        set2 = QtCharts.QBarSet("Amazon")
        set3 = QtCharts.QBarSet("Facebook")
        set4 = QtCharts.QBarSet("WeChat")

        set0.append([1, 2, 3,  4, 5, 6])
        set1.append([5, 0, 0,  4, 0, 7])
        set2.append([3, 5, 8, 13, 8, 5])
        set3.append([5, 6, 7,  3, 4, 5])
        set4.append([9, 7, 5,  3, 1, 2])

        series = QtCharts.QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Leading Tech Companies in 2021")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)


        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)


        self.ui.chart_view = QtCharts.QChartView(chart)
        self.ui.chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)
        # QChart.setTheme(theme)

        # print(self.ui.chart_view.chart().theme())
        # self.ui.chart_view.chart().setBackgroundBrush(QtGui.QColor("gray"))

        # self.setCentralWidget(chart_view)

        # self.lineEdit = QLineEdit(self.percentage_bar_chart_cont)
        # self.lineEdit.setObjectName(u"lineEdit")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.chart_view.sizePolicy().hasHeightForWidth())
        self.ui.chart_view.setSizePolicy(sizePolicy)
        self.ui.chart_view.setMinimumSize(QSize(0, 300))
        self.ui.percentage_bar_chart_cont.addWidget(self.ui.chart_view, 0, 0,  9, 9)
        self.ui.frame.setStyleSheet(u"background-color: transparent")


    def band(self):
        self.ui.pushButton.clicked.connect(self.handle_click)
        # self.ui.pushButton.clicked.connect(self.load)
        # self.ui.multiButton.clicked.connect(self.multiLoad)

    def handle_click(self):
        a=self.ui.input1.value()
        b=self.ui.input2.value()
        time_cost=self.ui.timeCost.value()
        self.ui.progressBar.setValue(0)
        for index,_ in enumerate(range(time_cost)):
            progress=index*100//time_cost
            self.ui.progressBar.setValue(progress)
            time.sleep(1)

        self.ui.progressBar.setValue(100)
        result=a+b
        self.ui.result.setNum(result)


    def load(self):
        FileDialog = QFileDialog(self.ui.pushButton)
        # 设置可以打开任何文件
        FileDialog.setFileMode(QFileDialog.AnyFile)
        # 文件过滤
        Filter = "(*.jpg,*.png,*.jpeg,*.bmp,*.gif)|*.jgp;*.png;*.jpeg;*.bmp;*.gif|All files(*.*)|*.*"
        image_file, _ = FileDialog.getOpenFileName(self.ui.pushButton, 'open file', './',
                                                   'Image files (*.jpg *.gif *.png *.jpeg)')  # 选择目录，返回选中的路径 'Image files (*.jpg *.gif *.png *.jpeg)'
        # 判断是否正确打开文件
        if not image_file:
            QMessageBox.warning(self.ui.pushButton, "警告", "文件错误或打开文件失败！", QMessageBox.Yes)
            return

        print("读入文件成功")
        print(image_file)  # 默认打开当前路径   输出文件路径
        print(OCRcode.OCR(image_file))
    def multiLoad(self):
         # FileDialog=QFileDialog(self.ui.multiButton)
        # FileDialog.setFileMode(QFileDialog.Directory)
        # Filter = "(*.jpg,*.png,*.jpeg,*.bmp,*.gif)|*.jgp;*.png;*.jpeg;*.bmp;*.gif|All files(*.*)|*.*"
        # image_file, _ = FileDialog.getOpenFileName(self.ui.multiButton, 'open file', './',
        #                                            'Image files (*.jpg *.gif *.png *.jpeg)')

        files, ok1 = QFileDialog.getOpenFileNames(self.ui, "多文件选择", "/", "所有文件 (*);;文本文件 (*.jpg)")
        print(files)  # 打印所选文件全部路径（包括文件名和后缀名）和文件类型
        for i,name in enumerate(files):
            print(OCRcode.OCR(name,True))
        # print(image_file)



if __name__=="__main__":



    app=QApplication(sys.argv)
    window=MainWindow()
    window.ui.show()
    sys.exit(app.exec_())


