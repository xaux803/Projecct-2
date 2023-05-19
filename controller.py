from PyQt5.QtWidgets import *
from view import *

import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Submit.clicked.connect(lambda: self.submit())
        self.D3.clicked.connect(lambda: self.dice(3))
        self.D4.clicked.connect(lambda: self.dice(4))
        self.D5.clicked.connect(lambda: self.dice(5))
        self.D6.clicked.connect(lambda: self.dice(6))
        self.D7.clicked.connect(lambda: self.dice(7))
        self.D8.clicked.connect(lambda: self.dice(8))
        self.D9.clicked.connect(lambda: self.dice(9))
        self.D10.clicked.connect(lambda: self.dice(10))
        self.D11.clicked.connect(lambda: self.dice(11))
        self.D12.clicked.connect(lambda: self.dice(12))
        self.D13.clicked.connect(lambda: self.dice(13))
        self.D14.clicked.connect(lambda: self.dice(14))
        self.D15.clicked.connect(lambda: self.dice(15))
        self.D16.clicked.connect(lambda: self.dice(16))
        self.D17.clicked.connect(lambda: self.dice(17))
        self.D18.clicked.connect(lambda: self.dice(18))
        self.D19.clicked.connect(lambda: self.dice(19))
        self.D20.clicked.connect(lambda: self.dice(20))
            
            
            
    def submit(self):
        try:
            low = int(self.low.text())
            high = int(self.high.text())
            self.randintoutput.setText(f'{random.randint(low,high)}')
                
        except:
            self.randintoutput.setText('Please enter\ninterger values')
            
    def dice(self,choice):
        if choice == 3:
            out = random.randint(1,3)
        elif choice == 4:
            out = random.randint(1,4)
        elif choice == 5:
            out = random.randint(1,5)
        elif choice == 6:
            out = random.randint(1,6)
        elif choice == 7:
            out = random.randint(1,7)
        elif choice == 8:
            out = random.randint(1,8)
        elif choice == 9:
            out = random.randint(1,9)
        elif choice == 10:
            out = random.randint(1,10)
        elif choice == 11:
            out = random.randint(1,11)
        elif choice == 12:
            out = random.randint(1,12)
        elif choice == 13:
            out = random.randint(1,13)
        elif choice == 14:
            out = random.randint(1,14)
        elif choice == 15:
            out = random.randint(1,15)
        elif choice == 16:
            out = random.randint(1,16)
        elif choice == 17:
            out = random.randint(1,17)
        elif choice == 18:
            out = random.randint(1,18)
        elif choice == 19:
            out = random.randint(1,19)
        elif choice == 20:
            out = random.randint(1,20)
            
        self.Diceoutput.setText(f'{out}')
        
