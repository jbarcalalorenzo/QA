from enchant.checker import SpellChecker
import sys
import tkFileDialog
from Menu import *

class Primero(QtGui.QDialog):
    archivo = ""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui =Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.toolButton,QtCore.SIGNAL('clicked()'),self.Abrir)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.Errores)
        QtCore.QObject.connect(self.ui.checkBox,QtCore.SIGNAL('clicked()'),self.Ortografia)


    def Errores(self):
        texto = open(self.archivo)
        chkr = SpellChecker("es_ES")
        chkr.set_text(texto.readline())
        for err in chkr:
         tpalabras= tpalabras+1
        self.ui.palabras.setText(tpalabras)
    def Ortografia(self):
        marcado = True
    def Cuentapalabras(self):
        total = len(self.archivo.split(" "))
    def Abrir(self):
        archivo = tkFileDialog.askopenfilename()
        texto = open(archivo)

        self.ui.textBrowser.setText(texto.readline())
if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Primero()
    myapp.show()
    sys.exit(app.exec_())

