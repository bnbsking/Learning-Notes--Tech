import sys, sqlite3, os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, \
    QComboBox, QLineEdit
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

connect = sqlite3.connect('../data/data.db')
s = pd.read_sql('select sql from sqlite_master where name=="T"', connect)['sql'][0]
cols, state = str(len(list( filter(lambda x:'data' in x,s.split(',')) ))), '1'
data = { 'data'+str(i):[0]*100 for i in range(1,1+int(cols)) }
pred = { 'pred'+str(i):[1]*100 for i in range(1,1+int(cols)) }

class myWidget: # support QLabel, QPushButton, QComboBox, QLineEdit for fast creation
    def __init__(self, parent, widget, text, fontSize=24, fontColor='white', bgColor='', borderR=0,\
            connect=None, items=None, img=None, imgSize=None, fixedWidth=0, fixedHeight=0):
        self.obj = widget(parent)
        if widget==QLabel: self.obj.setAlignment(Qt.AlignCenter)
        if widget==QPushButton: self.obj.clicked.connect(connect)
        if widget==QComboBox:
            self.obj.addItems(items)
        else:
            self.obj.setText(text)
        if img: self.obj.setPixmap( QPixmap('greenLight.png').scaled(*imgSize) )
            
        q = "font-size:{}px; color:{}; font-family:Microsoft JhengHei;".format(fontSize, fontColor)
        if bgColor: q+=" background-color:{};".format(bgColor)
        if borderR: q+=" border-radius:{}px;".format(borderR)
        self.obj.setStyleSheet(q)
        if fixedWidth: self.obj.setFixedWidth(fixedWidth)
        if fixedHeight: self.obj.setFixedHeight(fixedHeight)
        
class myTimer(QTimer):
    def __init__(self, parent, connect, period):
        super().__init__(parent)
        self.timeout.connect(connect)
        self.start(period)

class MainWindow(QMainWindow):
    def __init__(self):
        global state, cols
        super().__init__()
        self.setWindowTitle("Real time edge device status")
        self.setGeometry(150, 175, 1500, 800)
        self.setWindowIcon(QIcon("icon.png"))
        self.setStyleSheet("QMainWindow{background:qlineargradient(spread:\
            pad,x1:0,y1:0,x2:0,y2:1, stop:0 #003377, stop:1 #0000AA)}")
        
        title = myWidget(self, QLabel, 'MiAION-SeeR 異常檢測', 48).obj
        dataFig = PlotCanvas(self, width=7, height=3, title='data', color='#ff0000')
        lightText = myWidget(self, QLabel, 'Abnormal\nstate\nwarning', 24).obj
        self.light = myWidget(self, QLabel, '', img='greenLight.png', imgSize=(100,100)).obj
        predFig = PlotCanvas(self, width=7, height=3, title='pred', color='#00ff00')
        prevButton = myWidget(self, QPushButton, 'prev', 24, 'black', connect=\
            lambda:self.pageAction('prev')).obj
        self.page = myWidget(self, QLabel, 'Page: '+state+'/'+cols, 24).obj
        nextButton = myWidget(self, QPushButton, 'next', 24, 'black', connect=\
            lambda:self.pageAction('next')).obj
        self.CPU = myWidget(self, QLabel, 'CPU: -1', 24, 'black', 'orange', 12).obj
        self.memory = myWidget(self, QLabel, 'memory: -1', 24, 'black', 'green', 12).obj
        self.temperature = myWidget(self, QLabel, 'temperature: -1', 24, 'black', '#00ffff', 12).obj
        self.log = myWidget(self, QLabel, 'This is system log', 24, 'black', 'white', fixedWidth=200,\
            fixedHeight=100).obj        
        retrainParameter = myWidget(self, QLabel, 'Parameter: ', 24).obj
        self.retrainComboBox = myWidget(self, QComboBox, '', 24, 'black',\
            items=['data'+str(i) for i in range(1,int(cols)+1)], fixedWidth=150).obj
        retrainNumber = myWidget(self, QLabel, 'Number: ', 24).obj
        self.retrainLineEdit = myWidget(self, QLineEdit, '30000', 24, 'black', fixedWidth=150).obj
        self.retrainButton = myWidget(self, QPushButton, 'Start\nRetrain', 24, 'black', \
            connect=self.retrain).obj
        
        self.dataFigThread = myTimer(dataFig, dataFig.plotc, 1000)
        self.lightThread = myTimer(self, self.trafficLight, 1000)
        self.predFigThread = myTimer(predFig, predFig.plotc, 1000)
        self.accessDBThread = myTimer(self, self.accessDB, 1000)
                
        layout = QGridLayout()
        layout.addWidget(title, 0, 0, 1, 7, Qt.AlignCenter) # merge table from 0,0 thick1 width4
        layout.addWidget(dataFig, 1, 0, 3, 3, Qt.AlignCenter)
        layout.addWidget(lightText, 1, 3)
        layout.addWidget(self.light, 2, 3, 2, 1, Qt.AlignCenter)
        layout.addWidget(predFig, 1, 4, 3, 3, Qt.AlignCenter)
        layout.addWidget(prevButton, 4, 0)
        layout.addWidget(self.page, 4, 1)
        layout.addWidget(nextButton, 4, 2)
        layout.addWidget(self.CPU, 5, 0)
        layout.addWidget(self.memory, 5, 1)
        layout.addWidget(self.temperature, 5, 2)
        layout.addWidget(self.log, 4, 3, 2, 1, Qt.AlignCenter)
        layout.addWidget(retrainParameter, 4, 4)
        layout.addWidget(self.retrainComboBox, 4, 5)
        layout.addWidget(retrainNumber, 5, 4)
        layout.addWidget(self.retrainLineEdit, 5, 5)
        layout.addWidget(self.retrainButton, 4, 6, 2, 1, Qt.AlignCenter)
        
        widget = QWidget() # available resize and move
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def pageAction(self, action):
        global state, cols
        if action=='prev' and state!='1':
            state = str(int(state)-1)
        elif action=='next' and state!=cols:
            state = str(int(state)+1)
        self.page.setText('Page: '+state+'/'+cols)
    
    def accessDB(self):
        global data, pred, hardware, cols, connect
        df = pd.read_sql('select* from T order by time desc limit 1', connect)
        for i in range(1,int(cols)+1):
            data['data'+str(i)] = data['data'+str(i)][1:] + [df['data'+str(i)][0]]
            pred['pred'+str(i)] = pred['pred'+str(i)][1:] + [df['pred'+str(i)][0]]
        self.CPU.setText('CPU: '+str(df['CPU'][0]))
        self.memory.setText('memory: '+str(df['memory'][0]))
        self.temperature.setText('temperature: '+str(df['temperature'][0]))
    
    def trafficLight(self):
        global pred, state
        light = QPixmap('redLight.png') if pred['pred'+state][-1] else QPixmap('greenLight.png')
        light = light.scaled(100, 100)
        self.light.setPixmap(light)
        
    def retrain(self):
        self.retrainButton.hide()
        self.log.setText('Training...')
        os.system('python ../train/abnormal_detection/retrain.py {} {}'.format(\
            self.retrainComboBox.currentText(), self.retrainLineEdit.text()))
        self.log.setText('Training complete')
        self.retrainButton.show()
        
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=3, title='?', color='b'):
        super().__init__(Figure(figsize=(width, height), dpi=100, tight_layout={"pad":0.4,\
            "w_pad":0.5, "h_pad":1.0})) # self.figure is the object that plt.figure() returns
        self.title, self.color = title, color
        self.setParent(parent)
        self.plotc()

    def plotc(self):
        global state, data, pred
        self.figure.patch.set_facecolor('black')   # border
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.axes.set_facecolor('black')             # inner
        ax.set_title(self.title+state, color='white', fontsize=16)
        ax.spines['bottom'].set_color('white')     # spines
        ax.tick_params(axis='x', colors='white')   # ticks
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='y', colors='white')
        ax.plot(data['data'+state] if self.title[:4]=='data' else pred['pred'+state], self.color)
        self.draw()
    
app = QApplication(sys.argv)
MainWindow = MainWindow()
MainWindow.show()
sys.exit(app.exec_())
