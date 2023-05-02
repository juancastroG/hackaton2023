from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import sys
import time
from main import Ui_MainWindow
import random
class app(QMainWindow):

    def __init__(self):# Contructor de la clase principal del programa
        QMainWindow.__init__(self) 
        self.ui = Ui_MainWindow() #Abrimos la ventana principal
        self.ui.setupUi(self) #Inicializamos la clase principal
        self.ui.pushButton.clicked.connect(self.monitorear) #Conectamos el boton de monitorear con la funcion monitorear
    
    def alertar(self, sensor,datos):
            if datos>40 and datos<80:
                sensor.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.ui.label_3.setStyleSheet("background-color: rgba(255, 255, 0,0.40);")
                self.ui.label_3.setText("Alerta amarilla")
            if datos>80:
                sensor.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.ui.label_3.setStyleSheet("background-color: rgba(255, 0, 0,0.40);")
                self.ui.label_3.setText("Alerta roja")
            if datos<40:
                sensor.setStyleSheet("background-color: rgb(0, 255, 0);")
                self.ui.label_3.setStyleSheet("background-color: rgba(0, 255, 0,0.40);")
                self.ui.label_3.setText("")

    def monitorear(self): #Funcion que se ejecuta al presionar el boton monitorear
        #verificamos que sensores estan seleccionados
        profundidad = random.randint(0, 100)
        if self.ui.checkBox.isChecked():
            self.ui.label_2.setText("Sensor 1:\n nivel de agua: {}% \nde la capacidad permitida \n precipitacion: 10%\n corriente: nn \n calidad del aire: nn".format(profundidad))
            self.ui.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")

            time.sleep(1)
        if self.ui.checkBox_2.isChecked():
            self.ui.label_2.setText("Sensor 2:\n nivel de agua:{}% \nde la capacidad permitida\n precipitacion: 10%\n corriente: nn \n calidad del aire: nn".format(profundidad))
            

            time.sleep(1)
        if self.ui.checkBox_3.isChecked():
            self.ui.label_2.setText("Sensor 3:\n nivel de agua: {}% \nde la capacidad permitida\n precipitacion: 10%\n corriente: nn\n calidad del aire: nn".format(profundidad))

            time.sleep(1)
        if self.ui.checkBox_4.isChecked():
            self.ui.label_2.setText("Sensor 4:\n nivel de agua: {}% \nde la capacidad permitida\n precipitacion: 10%\n corriente: nn\n calidad del aire: nn".format(profundidad))

        if self.ui.checkBox_5.isChecked():
            self.ui.label_2.setText("Sensor 5:\n nivel de agua: {}% \nde la capacidad permitida\n precipitacion: 10%\n corriente: nn\n calidad del aire: nn".format(profundidad))

            time.sleep(1)
        
        self.alertar(self.ui.label_2,profundidad)
            



if __name__ == "__main__":
    aplicacion = QApplication([])   
    main = app()
    main.show()
    sys.exit(aplicacion.exec_())    #Cierra el bucle que muestra la interfaz

