import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import ctypes

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("MainWindow.ui", self)
        # Acomodo ventana al medio de la pantalla
        res = ctypes.windll.user32
        _ancho = res.GetSystemMetrics(0)
        _alto = res.GetSystemMetrics(1)
        left = (_ancho/2) - (self.frameSize().width()/2)
        top = (_alto/2) - (self.frameSize().height()/2)
        self.move(left, top)
        #<>

    def main(self):
        pass

if __name__ =='__main__':
    app = QApplication(sys.argv)
    _ventana = Ventana()
    _ventana.main()
    _ventana.show()
    app.exec_()