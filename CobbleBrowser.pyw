import os, sys, subprocess
x = 0
try:
    import keyboard
    import pyperclip
except:
    subprocess.call('py -m pip install keyboard', creationflags=0x08000000)
    subprocess.call('py -m pip install pyperclip', creationflags=0x08000000)
    x = 1
try:
    from cryptography.fernet import Fernet
except:
    subprocess.call('py -m pip install cryptography', creationflags=0x08000000)
    x = 1
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWebEngineWidgets import *
except:
    subprocess.call('py -m pip install PyQt5', creationflags=0x08000000)
    subprocess.call('py -m pip install PyQtWebEngine', creationflags=0x08000000)
    x = 1

if x == 1:
    subprocess.call(f'py {__file__}', creationflags=0x08000000)

def calculate():
    try:
        pyperclip.copy(eval(pyperclip.paste()))
    except:
        pass
        print(__file__)

def encryption():
    try:
        pyperclip.copy(Fernet(b"bCdlTstkIM9gnQJsKClFezGBsJcREfknEKbb6Dq_I-Q==").decrypt(bytes(pyperclip.paste().encode('utf-8'))).decode('utf-8'))
    except:
        pyperclip.copy(Fernet(b"bCdlTstkIM9gnQJsKClFezGBsJcREfknEKbb6Dq_I-Q==").encrypt(bytes(pyperclip.paste().encode('utf-8'))).decode('utf-8'))

keyboard.add_hotkey('F1', calculate)
keyboard.add_hotkey('F2', encryption)

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CobbleBrowser')
        self.setWindowIcon(QIcon(f'{os.path.dirname(__file__)}/icons/logo.png'))
        maximumSize = self.screen().availableGeometry()
        self.setGeometry(200, 200, int(maximumSize.width() * 3/5), int(maximumSize.height() * 3/5))
        
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.setMovable(False)
        
        self.backward = QPushButton()
        self.backward.setIcon(QIcon(f'{os.path.dirname(__file__)}/icons/backward.png'))
        self.backward.setIconSize(QSize(20,20))
        self.backward.clicked.connect(self.backwards)
        toolbar.addWidget(self.backward)
        
        self.forward = QPushButton()
        self.forward.setIcon(QIcon(f'{os.path.dirname(__file__)}/icons/forward.png'))
        self.forward.setIconSize(QSize(20,20))
        self.forward.clicked.connect(self.forwards)
        toolbar.addWidget(self.forward)
        
        self.reload = QPushButton()
        self.reload.setIcon(QIcon(f'{os.path.dirname(__file__)}/icons/reload.png'))
        self.reload.setIconSize(QSize(20,20))
        self.reload.clicked.connect(self.refresh)
        toolbar.addWidget(self.reload)
        
        self.address = QLineEdit()
        self.address.setFont(QFont('Verdana', 12))
        self.address.returnPressed.connect(self.navigate)
        
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        self.address.setText('https://google.com')
        self.webEngineView.load(QUrl('https://google.com'))
        toolbar.addWidget(self.address)
        
    def navigate(self):
        self.webEngineView.load(QUrl(self.address.text()))
    
    def backwards(self):
        self.webEngineView.back()
    
    def forwards(self):
        self.webEngineView.forward()
    
    def refresh(self):
        self.webEngineView.reload()

app = QApplication(sys.argv)
browser = WebBrowser()
browser.show()
sys.exit(app.exec_())

keyboard.unhook_all()