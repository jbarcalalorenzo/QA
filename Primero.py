from enchant.checker import SpellChecker
import sys
import tkFileDialog
from Menu import *

class Primero(QtGui.QDialog):
    archivo = None
    marcado = None
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui =Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.toolButton,QtCore.SIGNAL('clicked()'),self.Abrir)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.Validar)

    def Errores(self):
        terrores = 0
        texto = open(self.archivo, 'r')
        chkr = SpellChecker("es_ES")
        chkr.set_text(texto.readline())
        for err in chkr:
         terrores+=1
        terrores=str(terrores)
        self.ui.errores.setText(terrores)

    def Cuentapalabras(self):
        tpalabras=None
        total=0
        texto = open(self.archivo, 'r')
        text= texto.readline()
        total = len(text.split(" "))
        tpalabras=total
        tpalabras=str(tpalabras)
        self.ui.palabras.setText(tpalabras)

    def Abrir(self):
        self.archivo = tkFileDialog.askopenfilename()
        ruta=str(self.archivo)
        self.ui.lineEdit.setText(ruta)
        texto = open(self.archivo, 'r')
        self.ui.textBrowser.setText(texto.readline())

    def Validar(self):
        self.Errores()
        self.Cuentapalabras()
if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Primero()
    myapp.show()
    sys.exit(app.exec_())

