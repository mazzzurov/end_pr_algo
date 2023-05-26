import sys
 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


 
 
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.ans = 0
        self.ans2 = 0
        self.t = ""
        
 
    def initUI(self):
        self.setGeometry(300, 300, 450, 380)
        self.setWindowTitle('Simple Calculator')
 
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.resize(225, 95)
        self.label.move(10, 0)
        
        # первая строчка в калькуляторе
        self.num_1 = QPushButton('1', self)
        self.num_1.resize(90, 50)
        self.num_1.move(5, 100)
        self.num_1.clicked.connect(self.res)
        
        
        self.num_2 = QPushButton('2', self)
        self.num_2.resize(90, 50)
        self.num_2.move(100, 100)
        self.num_2.clicked.connect(self.res)
 
        self.num_3 = QPushButton('3', self)
        self.num_3.resize(90, 50)
        self.num_3.move(200, 100)
        self.num_3.clicked.connect(self.res)
        
        self.num_div = QPushButton('/', self)
        self.num_div.resize(90, 50)
        self.num_div.move(300, 100)
        self.num_div.clicked.connect(self.div)
 
         # вторая строчка в калькуляторе
        self.num_4 = QPushButton('4', self)
        self.num_4.resize(90, 50)
        self.num_4.move(5, 155)
        self.num_4.clicked.connect(self.res)
        
        self.num_5 = QPushButton('5', self)
        self.num_5.resize(90, 50)
        self.num_5.move(100, 155)
        self.num_5.clicked.connect(self.res)
 
        self.num_6 = QPushButton('6', self)
        self.num_6.resize(90, 50)
        self.num_6.move(200, 155)
        self.num_6.clicked.connect(self.res)
        
        self.num_mul = QPushButton('*', self)
        self.num_mul.resize(90, 50)
        self.num_mul.move(300, 155)
        self.num_mul.clicked.connect(self.mul)
 
        # третья строчка в калькуляторе
        self.num_7 = QPushButton('7', self)
        self.num_7.resize(90, 50)
        self.num_7.move(5, 210)
        self.num_7.clicked.connect(self.res)
        
        self.num_8 = QPushButton('8', self)
        self.num_8.resize(90, 50)
        self.num_8.move(100, 210)
        self.num_8.clicked.connect(self.res)
 
        self.num_9 = QPushButton('9', self)
        self.num_9.resize(90, 50)
        self.num_9.move(200, 210)
        self.num_9.clicked.connect(self.res)
        
        self.num_plus = QPushButton('+', self)
        self.num_plus.resize(90, 50)
        self.num_plus.move(300, 210)
        self.num_plus.clicked.connect(self.add)
 
        # четвёртая строчка в калькуляторе
        self.num_C = QPushButton('C', self)
        self.num_C.resize(90, 50)
        self.num_C.move(5, 265)
        self.num_C.clicked.connect(self.C)
        
        self.num_0 = QPushButton('0', self)
        self.num_0.resize(90, 50)
        self.num_0.move(100, 265)
        self.num_0.clicked.connect(self.res)
 
        self.num_CE = QPushButton('CE', self)
        self.num_CE.resize(90, 50)
        self.num_CE.move(200, 265)
        self.num_CE.clicked.connect(self.C)
        
        self.num_minus = QPushButton('-', self)
        self.num_minus.resize(90, 50)
        self.num_minus.move(300, 265)
        self.num_minus.clicked.connect(self.minus)
 
        # пятая строчка в калькуляторе
        #self.num_dot = QPushButton('.', self)
        #self.num_dot.resize(50, 50)
        #self.num_dot.move(5, 320)
        #self.num_dot.clicked.connect(self.dot)
        
        self.num_p_m = QPushButton('±', self)
        self.num_p_m.resize(190, 50)
        self.num_p_m.move(5, 320)
        self.num_p_m.clicked.connect(self.p_m)
 
        self.num_eq = QPushButton('=', self)
        self.num_eq.resize(190, 50)
        self.num_eq.move(205, 320)
        self.num_eq.clicked.connect(self.eq)

        self.stepen = QPushButton('^', self)
        self.stepen.resize(40, 270)
        self.stepen.move(405, 100)
        self.stepen.clicked.connect(self.step)
        
    def eq(self):
        if self.t == "+":
            self.label.setText(str(self.ans + self.ans2))
            self.ans = 0
            self.ans2 = 0
        elif self.t == "-":
            self.label.setText(str(self.ans - self.ans2))
            self.ans = 0
            self.ans2 = 0
        elif self.t == "*":
            self.label.setText(str(self.ans * self.ans2))
            self.ans = 0
            self.ans2 = 0
        elif self.t == "/":
            self.label.setText(str(self.ans / self.ans2))
            self.ans = 0
            self.ans2 = 0
        elif self.t == '^':
            self.label.setText(str(self.ans ** self.ans2))
            self.ans = 0
            self.ans2 = 0
        else:
            self.label.setText(str(self.ans))
        
    def p_m(self):
        if self.t != "":
            self.ans2 *= -1
            self.label.setText(str(self.ans2))
        else:
            self.ans *= -1
            self.label.setText(str(self.ans))

    def step(self):
        self.t = "^"
        self.label.setText(str(self.ans))
        
    def C(self):
        self.t = ''
        self.ans = 0
        self.ans2 = 0
        self.label.setText(str(0))
    
    def res(self, v):
        num = int(self.sender().text())
        if self.t != "":
            self.ans2 = self.ans2 * 10 + num
            self.label.setText(str(self.ans2))
        else:
            self.ans = self.ans * 10 + num
            self.label.setText(str(self.ans))


    def add(self):
        self.t = "+"
        self.label.setText(str(self.ans))

    def minus(self):
        self.t = "-"
        self.label.setText(str(self.ans))

    def mul(self):
        self.t = "*"
        self.label.setText(str(self.ans))

    def div(self):
        self.t = "/"
        self.label.setText(str(self.ans))
 

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    
    pal = ex.palette()
    pal.setColor(QPalette.Normal, QPalette.Window, QColor("#FF6600"))
    pal.setColor(QPalette.Inactive, QPalette.Window, QColor("#ff0000"))
    ex.setPalette(pal)
    


    ex.show()
    sys.exit(app.exec())
