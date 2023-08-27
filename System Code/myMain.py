from time import sleep

import pymysql

import openCV.OCRcode as OCRcode
from PySide2.QtCharts import QtCharts

from interface import *
# from temp import *
import sys
from PySide2.QtWidgets import QApplication,QMainWindow,QMessageBox,QFileDialog
# from PySide2 import QtCore
from Custom_Widgets.Widgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from threading import Thread
from multiprocessing import cpu_count
from math import ceil
from random import randrange
from functools import partial
import psutil
import PySide2extn

# from custom_qstacked_widgets
import mLineEdit

# from PySide2.QtWidgets import *
# from PySide2.QtUiTools import QUiLoader

platforms = {
'linux' : 'Linux',
'linux1' : 'Linux',
'linux2' : 'Linux',
'darwin' : 'OS X',
'win32' : 'Windows'
}


class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            pass
            # traceback.print_exc()
            # exctype, value = sys.exc_info()[:2]
            # self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class MySignals(QObject):
    progress_operate=Signal(int,str)
    ocr_start=Signal(str)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui=QUiLoader().load("test.ui")
        loadJsonStyle(self,self.ui)
        # 设置页面
        self.ui.stackedWidget.setCurrentIndex(0)
        #
        # self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        #

        self.ms = MySignals()
        self.ui.gpuOn = False
        self.num=[]
        self.timerJudge=0

        # 连接数据库
        self.con = pymysql.connect(host='127.0.0.1', port=3306, user="root", password="root", db='ocr')
        self.cur=self.con.cursor()
        self.selectNum()


        self.threadpool=QThreadPool()

        self.show()
        self.psutil_thread()

        # self.cpu_ram()

        # self.ms.ocr_start.connect(self.startOcr)
        # self.ui.dragEnter=False
    #     progressBar
        self.ui.progress.updateFormProgressIndicator(
            # Set font color
            color = "#000",
            # Set fill color
            fillColor = "white",
            # Set fill color for warnings
            successFillColor = "pink",
            # Set number of progress steps(default is 5)
            formProgressCount = 1,
            # Set progress animation duration
            formProgressAnimationDuration = 1000, #2seconds
            # Set progress container height
            height = 80,
            # Set progress container width
            width = 160,
            # Set default progress percentage
            startPercentage = 0 #half)
        )





        # 连接槽函数
        self.ui.GPUBtn.clicked.connect(self.gpuopen)
        self.ui.homeBtn.clicked.connect(self.homePage)
        self.ui.ocrBtn.clicked.connect(self.ocrPage)
        self.ui.percentBtn.clicked.connect(self.gotoPercentPage)
        self.ui.barBtn.clicked.connect(self.gotoBarPage)
        self.ui.pieBtn.clicked.connect(self.gotoPiePage)
        self.ui.openBtn.clicked.connect(self.loadFile)
        self.ui.files=None
        self.ui.processBtn.clicked.connect(self.startProcess)
        self.ms.progress_operate.connect(self.progressMov)
        self.ms.ocr_start.connect(self.startOcr)
        self.ui.clearBtn.clicked.connect(self.clearList)
        self.ui.delBtn.clicked.connect(self.delRow)
        self.ui.uploadBtn.clicked.connect(self.upLoad)


    def psutil_thread(self):
        worker = Worker(self.cpu_ram)

        # START WORKER
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def progress_fn(self, n):
        # n = progress value
        print("%d%% done" % n)

    def cpu_ram(self,progress_callback):
        while True:
            totalRam = 1.0
            totalRam = psutil.virtual_memory()[0] * totalRam
            totalRam = totalRam / (1024 * 1024 * 1024)
            self.ui.total_ram.setText(str("{:.4f}".format(totalRam) + ' GB'))

            availRam = 1.0
            availRam = psutil.virtual_memory()[1] * availRam
            availRam = availRam / (1024 * 1024 * 1024)
            self.ui.available_ram.setText(str("{:.4f}".format(availRam) + ' GB'))


            ramUsed = 1.0
            ramUsed = psutil.virtual_memory()[3] * ramUsed
            ramUsed = ramUsed / (1024 * 1024 * 1024)
            self.ui.used_ram.setText(str("{:.4f}".format(ramUsed) + ' GB'))

            ramFree = 1.0
            ramFree = psutil.virtual_memory()[4] * ramFree
            ramFree = ramFree / (1024 * 1024 * 1024)
            self.ui.free_ram.setText(str("{:.4f}".format(ramFree) + ' GB'))

            core = cpu_count()
            self.ui.cpu_count.setText(str(core))

            # ramUsages = str(psutil.virtual_memory()[2]) + '%'
            # self.ui.ram_usage.setText(str("{:.4f}".format(totalRam) + ' GB'))

            cpuPer = psutil.cpu_percent()
            self.ui.cpu_per.setText(str(cpuPer) + " %")

            cpuMainCore = psutil.cpu_count(logical=False)
            self.ui.cpu_main_core.setText(str(cpuMainCore))

            # CPU PERCENTAGE INDICATOR
            # SET PROGRESS BAR VALUE
            self.ui.cpu_percentage.rpb_setMaximum(100)
            # Set progress values
            self.ui.cpu_percentage.rpb_setValue(cpuPer)
            # SET PROGRESS BAR STYLE
            self.ui.cpu_percentage.rpb_setBarStyle('Hybrid1')
            # SET PROGRESS BAR LINE COLOR
            self.ui.cpu_percentage.rpb_setLineColor((255,100, 99))
            # SET PROGRESS BAR LINE COLOR
            self.ui.cpu_percentage.rpb_setCircleColor((255, 200, 175))
            # SET PROGRESS BAR LINE COLOR
            self.ui.cpu_percentage.rpb_setPieColor((45, 74, 83))
            #CHANGING THE PATH COLOR
            # self.ui.cpu_percentage.rpb_setPathColor((45, 74, 83))
            #SET PROGRESS BAR TEXT COLOR
            self.ui.cpu_percentage.rpb_setTextColor((255,128,0))

            # SET PROGRESS BAR STARTING POSITION
            # North, East, West, South
            self.ui.cpu_percentage.rpb_setInitialPos('West')
            #SET PROGRESS BAR TEXT TYPE : VALUE OR PERCENTAGE
            # Value, Percentage
            self.ui.cpu_percentage.rpb_setTextFormat('Percentage')

            #SET PROGRESS BAR FONT
            self.ui.cpu_percentage.rpb_setTextFont('Arial')
            #TEXT HIDDEN
            # self.ui.cpu_percentage.rpb_enableText(False)
            #SET PROGRESS BAR LINE WIDTH
            self.ui.cpu_percentage.rpb_setLineWidth(12)
            #PATH WIDTH
            self.ui.cpu_percentage.rpb_setPathWidth(12)
            #SET PROGRESS BAR LINE CAP
            # RoundCap, SquareCap
            self.ui.cpu_percentage.rpb_setLineCap('RoundCap')
            #LINE STYLE
            # DotLine, DashLine
            # self.ui.cpu_percentage.rpb_setLineStyle('DotLine')

            # RAM USAGE INDICATOR USING SPIRAL PROGRESSBAR
            # #######################################################################
            # #SETTING THE MINIMUM VALUE
            self.ui.ram_percantage.spb_setMinimum((0, 0, 0))
            # #######################################################################
            # #######################################################################
            # #SETTING THE MAXIMUM VALUE
            self.ui.ram_percantage.spb_setMaximum((totalRam, totalRam, totalRam))
            # #######################################################################
            # #######################################################################
            # # SET PROGRESS VALUE
            self.ui.ram_percantage.spb_setValue((availRam, ramUsed, ramFree))
            # #######################################################################
            # #######################################################################
            # #SET PROGRESS COLOR (R, G, B)
            self.ui.ram_percantage.spb_lineColor(((153,204,204), (255,204,153), (255, 204, 204)))
            # #######################################################################
            # #######################################################################
            # #SETING THE INITIAL POSITION OF THE PROGRESS BAR: FROM OUTER->INWARDS
            self.ui.ram_percantage.spb_setInitialPos(('West', 'West', 'West'))
            # #######################################################################
            # #######################################################################
            # #SETING THE DIRECTION OF PROGRESS OF THE PROGRESS BAR: FROM OUTER-INWARDS
            # self.ui.ram_percantage.spb_setDirection(('Clockwise', 'AntiClockwise', 'Clockwise'))
            # #######################################################################
            # #######################################################################
            # #SET LINE WIDTH: 15px
            self.ui.ram_percantage.spb_lineWidth(13)
            # #######################################################################
            # #######################################################################
            # #SET GAP WIDTH
            self.ui.ram_percantage.spb_setGap(15)
            # #######################################################################
            # #######################################################################
            # #SET LINE STYLE
            self.ui.ram_percantage.spb_lineStyle(('SolidLine', 'SolidLine', 'SolidLine'))
            # #######################################################################
            # #######################################################################
            # #SET LINE CAP
            self.ui.ram_percantage.spb_lineCap(('RoundCap', 'RoundCap', 'RoundCap'))
            # #######################################################################
            # #######################################################################
            # #HIDE THE PATH
            self.ui.ram_percantage.spb_setPathHidden(True)
            # #######################################################################
            # SLEEP FOR 1 SEC
            sleep(1)


    def selectNum(self):
        self.num=[]
        city=["重庆市","上海市","北京市","四川省成都市","湖南省长沙市"]
        for item in city:
            self.cur.execute("SELECT sum(DATE_FORMAT(日期,'%m')=1) as a1,"
                             "sum(DATE_FORMAT(日期,'%m')=2) as a2,sum(DATE_FORMAT(日期,'%m')=3) as a3,"
                             "sum(DATE_FORMAT(日期,'%m')=4) as a4,sum(DATE_FORMAT(日期,'%m')=5) as a5,"
                             "sum(DATE_FORMAT(日期,'%m')=6) as a6 "
                             "from (SELECT 日期 from info where 行程='{ci}')as tb".format(ci=item))
            row = self.cur.fetchone()
            temp=[]
            for i in range(0,6):
                temp.append(int(row[i]))
            self.num.append(temp)
        self.con.commit()
        print(self.num)


    def create_nested_donuts(self):
        self.setMinimumSize(800, 550)
        self.donuts = []
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart = self.chart_view.chart()


        self.chart.legend().setVisible(False)

        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        self.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)

        self.chart.setTitle("2022年途径城市纵向对比图")
        titleFont = QFont()
        titleFont.setBold(True)
        titleFont.setFamily("楷体")
        titleFont.setPixelSize(16)
        self.chart.setTitleFont(titleFont)



        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart_view.sizePolicy().hasHeightForWidth())
        self.chart_view.setSizePolicy(sizePolicy)
        self.chart_view.setMinimumSize(QSize(0, 300))
        self.ui.nested_donut_chart_cont.addWidget(self.chart_view, 0, 0, 9, 9)
        # self.ui.frame_7.setStyleSheet(u"background-color: transparent")

        self.min_size = 0.1
        self.max_size = 0.9
        self.donut_count = 5

        self.setup_donuts()
        if(self.timerJudge==1):
            self.update_timer.stop()
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_rotation)
        self.update_timer.start(1250)
        self.timerJudge=1

    def setup_donuts(self):
        for i in range(self.donut_count):
            donut = QtCharts.QPieSeries()
            slccount = 6
            for j in range(slccount):
                value = self.num[i][j]
                slc = QtCharts.QPieSlice(str(value), value)
                slc.setLabelVisible(True)
                slc.setLabelColor(Qt.white)
                slc.setLabelPosition(QtCharts.QPieSlice.LabelInsideTangential)

                # Connection using an extra parameter for the slot
                slc.hovered[bool].connect(partial(self.explode_slice, slc=slc))

                donut.append(slc)
                size = (self.max_size - self.min_size)/self.donut_count
                donut.setHoleSize(self.min_size + i * size)
                donut.setPieSize(self.min_size + (i + 1) * size)
                # print(i)

            self.donuts.append(donut)
            self.chart_view.chart().addSeries(donut)



    def update_rotation(self):
        for donut in self.donuts:
            phase_shift =  randrange(-50, 100)
            donut.setPieStartAngle(donut.pieStartAngle() + phase_shift)
            donut.setPieEndAngle(donut.pieEndAngle() + phase_shift)

    def explode_slice(self, exploded, slc):
        if exploded:
            self.update_timer.stop()
            slice_startangle = slc.startAngle()
            slice_endangle = slc.startAngle() + slc.angleSpan()

            donut = slc.series()
            idx = self.donuts.index(donut)
            for i in range(idx + 1, len(self.donuts)):
                self.donuts[i].setPieStartAngle(slice_endangle)
                self.donuts[i].setPieEndAngle(360 + slice_startangle)
        else:
            for donut in self.donuts:
                donut.setPieStartAngle(0)
                donut.setPieEndAngle(360)

            self.update_timer.start()

        slc.setExploded(exploded)



    def create_bar_graph(self):
        set0 = QtCharts.QBarSet("重庆市")
        set1 = QtCharts.QBarSet("上海市")
        set2 = QtCharts.QBarSet("北京市")
        set3 = QtCharts.QBarSet("四川省成都市")
        set4 = QtCharts.QBarSet("湖南省长沙市")

 
        maxVal=max(max(self.num[0]),max(self.num[1]),max(self.num[2]),max(self.num[3]),max(self.num[4]))
        set0.append(self.num[0])
        set1.append(self.num[1])
        set2.append(self.num[2])
        set3.append(self.num[3])
        set4.append(self.num[4])

        barSeries = QtCharts.QBarSeries()
        barSeries.append(set0)
        barSeries.append(set1)
        barSeries.append(set2)
        barSeries.append(set3)
        barSeries.append(set4)

        lineSeries = QtCharts.QLineSeries()
        lineSeries.setName("平均变化趋势")
        lineSeries.append(QPoint(0, (self.num[0][0]+self.num[1][0]+self.num[2][0]+self.num[3][0]+self.num[4][0])/5))
        lineSeries.append(QPoint(1, (self.num[0][1]+self.num[1][1]+self.num[2][1]+self.num[3][1]+self.num[4][1])/5))
        lineSeries.append(QPoint(2, (self.num[0][2]+self.num[1][2]+self.num[2][2]+self.num[3][2]+self.num[4][2])/5))
        lineSeries.append(QPoint(3, (self.num[0][3]+self.num[1][3]+self.num[2][3]+self.num[3][3]+self.num[4][3])/5))
        lineSeries.append(QPoint(4, (self.num[0][4]+self.num[1][4]+self.num[2][4]+self.num[3][4]+self.num[4][4])/5))
        lineSeries.append(QPoint(5, (self.num[0][5]+self.num[1][5]+self.num[2][5]+self.num[3][5]+self.num[4][5])/5))




        chart = QtCharts.QChart()
        chart.addSeries(barSeries)
        chart.addSeries(lineSeries)


        categories = ["1月", "2月", "3月", "4月", "5月", "6月"]
        axisX = QtCharts.QBarCategoryAxis()
        axisX.append(categories)
        chart.setAxisX(axisX, lineSeries)
        chart.setAxisX(axisX, barSeries)
        axisX.setRange("1月", "6月")

        axisY = QtCharts.QValueAxis()
        chart.setAxisY(axisY, lineSeries)
        chart.setAxisY(axisY, barSeries)
        axisY.setRange(0, ceil(maxVal*1.05))  # 设置Y的刻度

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QtCharts.QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        chartView.chart().setTheme(QtCharts.QChart.ChartThemeDark)
        #紧接着设置title
        chart.setTitle("2022年途径城市条形折线统计图")
        titleFont = QFont()
        titleFont.setBold(True)
        titleFont.setFamily("楷体")
        titleFont.setPixelSize(16)
        chart.setTitleFont(titleFont)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chartView.sizePolicy().hasHeightForWidth())
        chartView.setSizePolicy(sizePolicy)
        chartView.setMinimumSize(QSize(0, 300))
        self.ui.bar_charts_cont.addWidget(chartView, 0, 0, 9, 9)
        # self.ui.frame_18.setStyleSheet(u"background-color: transparent")


    def create_percentage_bar_chart(self):
        set0 = QtCharts.QBarSet("重庆市")
        set1 = QtCharts.QBarSet("上海市")
        set2 = QtCharts.QBarSet("北京市")
        set3 = QtCharts.QBarSet("四川省成都市")
        set4 = QtCharts.QBarSet("湖南省长沙市")

        set0.append(self.num[0])
        set1.append(self.num[1])
        set2.append(self.num[2])
        set3.append(self.num[3])
        set4.append(self.num[4])

        series = QtCharts.QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        categories = ["1月", "2月", "3月", "4月", "5月", "6月"]
        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.ui.chart_view = QtCharts.QChartView(chart)
        self.ui.chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)
        # #先设置theme再修改Title的样式，否则会被theme覆盖
        chart.setTitle("2022年途径城市百分比堆积柱形图")
        titleFont = QFont()
        titleFont.setBold(True)
        titleFont.setFamily("楷体")
        titleFont.setPixelSize(16)
        chart.setTitleFont(titleFont)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.chart_view.sizePolicy().hasHeightForWidth())
        self.ui.chart_view.setSizePolicy(sizePolicy)
        self.ui.chart_view.setMinimumSize(QSize(0, 300))
        self.ui.percentage_bar_chart_cont.addWidget(self.ui.chart_view, 0, 0, 9, 9)
        # self.ui.frame.setStyleSheet(u"background-color: transparent")





    def upLoad(self):
        lenth = self.ui.tableWidget.rowCount()
        for i in range(lenth):
            itemNow = []
            for j in range(5):
                tmp = self.ui.tableWidget.item(i, j).text()
                itemNow.append(tmp)
            self.cur.execute("insert into info values(%s,%s,%s,%s,%s)",
                        (itemNow[0], itemNow[1], itemNow[2], itemNow[3], itemNow[4]))

        self.con.commit()

        # msgBox=QMessageBox.information(self.ui.ocrPage,"消息通知","上传数据库成功！")
        msgBox=QMessageBox()
        msgBox.setText("上传数据库成功")
        msgBox.addButton(self.tr("好的"),QMessageBox.AcceptRole)
        # msgBox.standardIcon(icon("icons/title"))
        # msgBox.setTextFormat()
        msgBox.setWindowTitle("MySql返回通知")
        msgBox.setWindowIcon(QIcon("icons/title"))
        # msgBox.setButtonText(msgBox.button(),"好的")
        msgBox.exec_()





    def delRow(self):
        listItem=self.ui.tableWidget.selectedItems()
        #细节：对于选中的是行，会返回许多个item,这里进行去重操作
        # rowList=[]
        # # simpleList=[]
        # for element in range(listItem):
        #     rowList.append(element.row())
        # rowList=set(listItem)


        print(len(listItem))
        for index,itemNow in enumerate(listItem):
            # if(itemNow!=None):
            try:
                self.ui.tableWidget.removeRow(itemNow.row())
            except:
                pass
        # print(itemNow.row())
        # self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() - len(listItem))
        # self.ui.tableWidget.removeRow(rowNum)

    def clearList(self):
        cnt=self.ui.tableWidget.rowCount()
        for i in range(cnt):
            item=self.ui.tableWidget.removeRow(0)
        # self.ui.tableWidget.setRowCount(0)

    def gpuopen(self):
        if(self.ui.GPUBtn.isChecked()==True):
            self.ui.gpuOn=True
        else:
            self.ui.gpuOn = False

    def addData(self,data):

        self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount()+1)
        item=QTableWidgetItem(data["类型"])
        self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1,0,item)
        item = QTableWidgetItem(data["电话"])
        self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 1, item)
        item = QTableWidgetItem(data["日期"])
        self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 2, item)
        item = QTableWidgetItem(data["时间"])
        self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 3, item)
        item = QTableWidgetItem(data["行程"])
        self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 4, item)

    def startOcr(self,name):
        OCRcode.OCR(name)

    def progressMov(self,judge,name):
        if(judge==0):
            # print("开始")
            self.ui.progress.updateFormProgressIndicator(formProgressAnimationDuration=6000)
            self.ui.progress.animateFormProgress(50)
            self.ui.loadLabel.setScaledContents(True)
            self.ui.loadLabel.setPixmap(QPixmap(name))
        if(judge==1):
            # print("第二次开始")
            self.ui.progress.updateFormProgressIndicator(formProgressAnimationDuration=200)
            self.ui.progress.animateFormProgress(100)
            # self.ui.progress.setStepStatus(status="suc1cess")
        # if(judge==2):
        #     self.ui.labelName.setText(name)


    def startProcess(self):
        def innerFunc():
            if(self.ui.files==[]):
                self.ui.files.append(self.ui.lineEdit.text())

            self.ui.progress.removeRight()
            self.ui.progress.updateFormProgressIndicator(startPercentage=0)
            # self.ui.progress.animateFormProgress(1)
            for i, name in enumerate(self.ui.files):
                self.ms.progress_operate.emit(0,name)  #在主线程中执行
                # self.ms.ocr_start.emit(name)
                data=OCRcode.OCR(name,self.ui.gpuOn)
                self.addData(data)
                # print("结束")
            self.ms.progress_operate.emit(1, name)
        task=Thread(target=innerFunc)
        task.start()




    def loadFile(self):
        # dialog = QFileDialog(self)
        # dialog.setFileMode(QFileDialog.ExistingFiles)
        # dialog.filter("png")
        # fileName=dialog.getOpenFileUrl(self,str("Open File"),'./',str("Images(*.png *.jpg)"))
        # print(fileName)
        self.ui.files, ok1 = QFileDialog.getOpenFileNames(self, "行程码图片选择", "Z:/Desktop/testSet", "图片文件(*.PNG;*.JPG;*.JPEG;*.BMP)")
        if(len(self.ui.files)>1):
            self.ui.lineEdit.setText(self.ui.files[0]+" 等"+str(len(self.ui.files))+"个文件")
        else:
            self.ui.lineEdit.setText(self.ui.files[0])
        print(self.ui.files)  # 打印所选文件全部路径（包括文件名和后缀名）和文件类型
        # self.ui.loadLabel.setPixmap(files)

    def btnColor(self, str):
        self.ui.leftMenu.setStyleSheet(u"#%s\n{"
                                       "	background-color: #fefeff;\n"
                                       "	padding: 10px 5px;\n"
                                       "	text-align: left;\n"
                                       "	border-top-left-radius: 22px ;\n}" % str)
    def homePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        self.btnColor("homeBtn")



    def ocrPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ocrPage)
        self.btnColor("ocrBtn")

    def gotoPercentPage(self):
        self.selectNum()
        self.create_percentage_bar_chart()
        self.ui.stackedWidget.setCurrentWidget(self.ui.percentPage)
        self.btnColor("percentBtn")

    def gotoBarPage(self):
        self.selectNum()
        self.create_bar_graph()
        self.ui.stackedWidget.setCurrentWidget(self.ui.barPage)
        self.btnColor("barBtn")

    def gotoPiePage(self):
        # self.selectNum()
        self.create_nested_donuts()
        self.ui.stackedWidget.setCurrentWidget(self.ui.piePage)
        self.btnColor("pieBtn")






if __name__=="__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QApplication(sys.argv)
    window=MainWindow()
    window.setWindowTitle("基于OCR的防疫行程卡识别实验室")
    Icon=QIcon("icons/title.png")
    window.setWindowIcon(Icon)
    window.show()
    sys.exit(app.exec_())
