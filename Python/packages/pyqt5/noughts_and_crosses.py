import sys
import numpy as np
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
class Window(QWidget):
    def __init__(self):
        super().__init__()       
        self.initUI()
        self.show()

    def initUI(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Input Test')
        
        self.hint = QLabel(self)
        self.hint.setText("GO GO !!")
        self.hint.move(420, -50)
        self.hint.resize(200,200)
        
        pixmap = QPixmap('9pix.png')
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.background = QLabel(self)
        self.background.setPixmap(pixmap)
        
        pixmap2 = QPixmap('now.png')
        pixmap2 = pixmap2.scaled(110, 110, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.block = QLabel(self)
        self.block.setPixmap(pixmap2)
        self.block.move(30, 25)
        
        self.L = []
        for i in range(9):
            pixmap = QPixmap('o.png') if i%2==0 else QPixmap('x.png')
            pixmap = pixmap.scaled(110, 110, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.L.append( QLabel(self) )
            self.L[i].setPixmap(pixmap)
            self.L[i].hide()
        self.step = 0
        self.N, self.x, self.y = np.zeros((3,3)), 0, 0
            
    def keyPressEvent(self, event): # cannot modify name
        if self.result()==0:
            if event.key()==16777234 and self.block.x()>30: # left
                self.block.move(self.block.x()-115, self.block.y())
                self.x-=1
            elif event.key()==16777235 and self.block.y()>25: # up
                self.block.move(self.block.x(), self.block.y()-100)
                self.y-=1
            elif event.key()==16777236 and self.block.x()<260: # right
                self.block.move(self.block.x()+115, self.block.y())
                self.x+=1
            elif event.key()==16777237 and self.block.y()<225: # down
                self.block.move(self.block.x(), self.block.y()+100)
                self.y+=1
            elif event.key()==16777220 and self.N[self.x, self.y]==0: # enter
                if self.step%2==0:
                    self.N[self.x, self.y] = 1
                else:
                    self.N[self.x, self.y] = -1
                self.L[self.step].move( self.block.x(), self.block.y() )
                self.L[self.step].show()
                self.step += 1
                if self.result()==1:
                    self.hint.setText("player O wins !")
                elif self.result()==-1:
                    self.hint.setText("player X wins !")
                elif self.result()==2:
                    self.hint.setText("draw !")
            
    def result(self):
        csum, rsum = self.N.sum(axis=0), self.N.sum(axis=1)
        dsum, osum = self.N.trace(), np.fliplr(self.N).trace()
        if 3 in csum or 3 in rsum or 3==dsum or 3==osum:
            return 1
        elif -3 in csum or -3 in rsum or -3==dsum or -3==osum:
            return -1
        elif self.step==9:
            return 2
        else:
            return 0
            
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print('You click left !')
        elif event.button() == Qt.RightButton:
            print('You click right !')
        elif event.button() == Qt.MidButton:
            print('You click middle !')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
