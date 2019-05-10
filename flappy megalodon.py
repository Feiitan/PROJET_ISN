import datetime
import math
import signal
import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets

signal.signal(signal.SIGINT, signal.SIG_DFL)

class Obstacle() :
    
    def __init__(self, x, y, w, h, t) :
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.t = t
        
class Animated_window(QtWidgets.QWidget) :

    def __init__(self) :
        super().__init__()
        self.create_contents()
        self.show()
        framerate = 60
        self.animation_start = datetime.datetime.now()
        self.animation_timer = QtCore.QTimer()
        self.animation_timer.timeout.connect(self.animation_step)
        self.animation_timer.start(1000 / framerate)
        self.obstacles = [ ]
        self.obstacles.append(Obstacle(300, 0, 40, random.randint(100, 500), 125))
        self.obstacles.append(Obstacle(500, 0, 40, random.randint(100, 500), 125))
        self.obstacles.append(Obstacle(700, 0, 40, random.randint(100, 500), 125))
        self.obstacles.append(Obstacle(900, 0, 40, random.randint(100, 500), 125))
        self.obstacles.append(Obstacle(1100, 0, 40, random.randint(100, 500), 125))
        

    def create_new_obstacle(self, i) :
        self.obstacles[i] = Obstacle(950 ,0 ,40 ,random.randint(100, 500), 125)

    def create_contents(self) :
        self.time = 0
        self.gravity = 1
        self.speed = 1
        self.setWindowTitle("Flappy Megalodon")
        self.resize(800, 600)
        #box = QtWidgets.QVBoxLayout(self)
        #box.setContentsMargins(0, 0, 0, 0)
        #self.button = QtWidgets.QPushButton()
        #box.addWidget(self.draw)

    def animation_step(self) :
        time = datetime.datetime.now() - self.animation_start
        self.time = time.total_seconds()
        self.update()

    def paintEvent(self, event) :
        try :
            size = self.size()
            w = size.width()
            h = size.height()
            t = 125
            x = 200
            self.velocity += self.gravity
            y = self.gravity + 300
            if y > h:
                y = h
            if y < 0 :
                y = 0
            qp = QtGui.QPainter()
            qp.begin(self)
            qp.setRenderHints(QtGui.QPainter.Antialiasing, 1)
            #pen = QtGui.QPen(QtGui.QColor(255, 128, 0))
            #qp.setPen(pen)
            path = QtGui.QPainterPath()
            path.moveTo(x + 25, y)
            path.lineTo(x, y + 25)
            path.lineTo(x - 25, y)
            path.lineTo(x, y - 25)
            path.closeSubpath()
            qp.fillPath(path, QtGui.QColor(0, 0, 255))
            #qp.drawPath(path)
            qp.end()
            
            qp.begin(self)
            qp.setRenderHints(QtGui.QPainter.Antialiasing, 1)
            #pen = QtGui.QPen(QtGui.QColor(255, 128, 0))
            #qp.setPen(pen)
            for i in range(0,len(self.obstacles)):
                path = QtGui.QPainterPath()
                path.addRect(self.obstacles[i].x, 0, self.obstacles[i].w, self.obstacles[i].h)
                path.addRect(self.obstacles[i].x, h, self.obstacles[i].w, -(h - self.obstacles[i].h - t))
                qp.fillPath(path, QtGui.QColor(0, 0, 255))
                #qp.drawPath(path)
            qp.end()
            for i in range(0,len(self.obstacles)):
                self.obstacles[i].x -= self.speed
                if self.obstacles[i].x < -40 :
                    self.create_new_obstacle(i)
        except Exception as e :
            print("Erreur:", e)
        
            
        
    def keyPressEvent(self, event):
        key = event.key()
        #print(key)
        if key == QtCore.Qt.Key_Escape  :
            self.close()
        elif key == QtCore.Qt.Key_Space :
            self.velocity -= 25
            
        

    def keyReleaseEvent(self, event):
        return


def main() :
    app = QtWidgets.QApplication(sys.argv)
    clock = Animated_window()
    sys.exit(app.exec_())

main()
