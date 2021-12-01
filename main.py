import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtGui
import traceback
import time

form_class = uic.loadUiType("Bombman.ui")[0]

class Form(QtWidgets.QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_SwRelease.clicked.connect(self.clickSwRelease)

        self.Monitor_1.setPixmap(QtGui.QPixmap("screenshot/1.png").scaledToWidth(380))
        self.Monitor_2.setPixmap(QtGui.QPixmap("screenshot/1.png").scaledToWidth(380))
        self.Monitor_3.setPixmap(QtGui.QPixmap("screenshot/1.png").scaledToWidth(380))
        self.Monitor_4.setPixmap(QtGui.QPixmap("screenshot/1.png").scaledToWidth(380))
        self.Monitor_5.setPixmap(QtGui.QPixmap("screenshot/1.png").scaledToWidth(380))
        self.Monitor_6.setPixmap(QtGui.QPixmap("screenshot/1.png").scaledToWidth(380))
        self.Monitor_7.setPixmap(QtGui.QPixmap("screenshot/1.png").scaledToWidth(380))
        self.Monitor_8.setPixmap(QtGui.QPixmap("screenshot/1.png").scaledToWidth(380))
        self.Monitor_9.setPixmap(QtGui.QPixmap("screenshot/1.png").scaledToWidth(380))

        '''
        index = 0
        self.relay0 = Relay_Channel(0, self, RC_Serial[0])
        self.relay1 = Relay_Channel(1, self, RC_Serial[0])
        self.relay2 = Relay_Channel(2, self, RC_Serial[0])
        self.relay3 = Relay_Channel(3, self, RC_Serial[0])
        index = index + 1;

        self.label_ch1_3.setStyleSheet("color: red")
        self.label_ch2_3.setStyleSheet("color: red")
        self.label_ch3_3.setStyleSheet("color: red")
        self.label_ch4_3.setStyleSheet("color: red")

        self.label_ch1_3.setText("Disconnected")
        self.label_ch2_3.setText("Disconnected")
        self.label_ch3_3.setText("Disconnected")
        self.label_ch4_3.setText("Disconnected")

        self.pushButton_ch1.setStyleSheet("background-color: red")
        self.pushButton_ch2.setStyleSheet("background-color: red")
        self.pushButton_ch3.setStyleSheet("background-color: red")
        self.pushButton_ch4.setStyleSheet("background-color: red")

        self.pushButton_ch1.clicked.connect(self.clickMethod1)
        self.pushButton_ch2.clicked.connect(self.clickMethod2)
        self.pushButton_ch3.clicked.connect(self.clickMethod3)
        self.pushButton_ch4.clicked.connect(self.clickMethod4)

        while (not (
                self.relay0.onDigitalOutput_Connect() and self.relay1.onDigitalOutput_Connect() and self.relay2.onDigitalOutput_Connect() and self.relay3.onDigitalOutput_Connect())):
            if index < len(RC_Serial):
                self.relay0 = Relay_Channel(0, self, RC_Serial[index])
                self.relay1 = Relay_Channel(1, self, RC_Serial[index])
                self.relay2 = Relay_Channel(2, self, RC_Serial[index])
                self.relay3 = Relay_Channel(3, self, RC_Serial[index])
                index = index + 1

            else:
                if QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.question(self, "Error",
                                                                               "Relay No Connection\nretry?",
                                                                               QtWidgets.QMessageBox.Yes,
                                                                               QtWidgets.QMessageBox.No):
                    index = 0
                    pass
                else:
                    sys.exit()
        '''
        self.show()

    def closeEvent(self, event):
        message = QtWidgets.QMessageBox.question(self, "Question", "Are you sure you want to quit?")
        if message == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def clickSwRelease(self):
        message = QtWidgets.QMessageBox.question(self, "Question", "Do you want to release Software?")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())