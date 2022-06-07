# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import sys
from menu_u import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)

		#Eliminar barra y de titulo - opacidad
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		#SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		#Mover ventana
		self.ui.frame_superior.mouseMoveEvent = self.mover_ventana
		
		#Acceder a las paginas
		self.ui.bt_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))			
		self.ui.bt_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_uno))
		self.ui.bt_dos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_dos))	
		self.ui.bt_tres.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tres))			
		self.ui.bt_cinco.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cinco))

		#Acceder a los pdfs
		self.ui.bt_ter1.clicked.connect(self.abrir1)
		self.ui.bt_ter2.clicked.connect(self.abrir2)
		self.ui.bt_ter3.clicked.connect(self.abrir3)
		self.ui.bt_ter5.clicked.connect(self.abrir1)

		#Abrir los dockers
		self.ui.bt_prac1.clicked.connect(self.dock_elk)
		self.ui.bt_prac2.clicked.connect(self.dock_misp)
		self.ui.bt_prac3.clicked.connect(self.dock_ctz)
		self.ui.bt_prac5.clicked.connect(self.dock_php)

		#Acceder a las paginas
		self.ui.ELK.clicked.connect(self.ELK)
		self.ui.MISP.clicked.connect(self.MISP)
		self.ui.CTZ.clicked.connect(self.CTZ)
		self.ui.PHP.clicked.connect(self.PHP)

		#Acceder a los videos
		self.ui.vd1.clicked.connect(self.vd1)
		self.ui.vd2.clicked.connect(self.vd2)
		self.ui.vd3.clicked.connect(self.vd3)

		#Control barra de titulos
		self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
		self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
		self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.ui.bt_cerrar.clicked.connect(lambda: self.close())

		self.ui.bt_restaurar.hide()

		#Menu lateral
		self.ui.bt_menu.clicked.connect(self.mover_menu)

	#Funciones para abrir paginas de google

	def ELK(self):
		if os.name == "posix":
			os.system("firefox https://www.elastic.co/es/what-is/elk-stack")
		else:
			os.system("start chrome https://www.elastic.co/es/what-is/elk-stack")
	
	def MISP(self):
		if os.name == "posix":
			os.system("firefox https://www.misp-project.org")
		else:
			os.system("start chrome https://www.misp-project.org")

	def CTZ(self):
		if os.name == "posix":
			os.system("firefox https://cortezaproject.org")
		else:
			os.system("start chrome https://cortezaproject.org")

	def PHP(self):
		if os.name == "posix":
			os.system("firefox https://www.php.net")
		else:
			os.system("start chrome https://www.php.net")

	def vd1(self):
		if os.name == "posix":
			os.system("firefox https://www.youtube.com/watch?v=MhC3ZFY5dNI")
		else:
			os.system("start chrome https://www.youtube.com/watch?v=MhC3ZFY5dNI")

	def vd2(self):
		if os.name == "posix":
			os.system("firefox https://www.youtube.com/watch?v=lCN4n8CNkNM")
		else:
			os.system("start chrome https://www.youtube.com/watch?v=lCN4n8CNkNM")

	def vd3(self):
		if os.name == "posix":
			os.system("firefox https://www.youtube.com/watch?v=S-CfD_FW3Co")
		else:
			os.system("start chrome https://www.youtube.com/watch?v=S-CfD_FW3Co")
		
	def abrir1(self):
		if os.name == "posix":
			os.system("firefox https://github.com/ahmedhassank/documentacion/blob/main/Documentacion_ELK.pdf")
		else:
			os.system("start chrome https://github.com/ahmedhassank/documentacion/blob/main/Documentacion_ELK.pdf")

	def abrir2(self):
		if os.name == "posix":
			os.system("firefox https://github.com/ahmedhassank/documentacion/blob/main/MISP.pdf")
		else:
			os.system("start chrome https://github.com/ahmedhassank/documentacion/blob/main/MISP.pdf")
	
	def abrir3(self):
		if os.name == "posix":
			os.system("firefox https://github.com/ahmedhassank/documentacion/blob/main/Corteza.pdf")
		else:
			os.system("start chrome https://github.com/ahmedhassank/documentacion/blob/main/Corteza.pdf")

	#Funciones para abrir los contenedores de las herramientas

	def dock_elk(self):
		os.system("docker pull ahmedhassank/elk:latest")
		os.system("docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it --name elk ahmedhassank/elk")
		os.system("docker start elk")



	def dock_misp(self):
		os.chdir('docker-misp')
		os.system("docker-compose up")
		os.chdir('..')

		

	def dock_ctz(self):
		os.chdir('corteza')
		os.system("docker-compose up -d")
		os.chdir('..')



	
	def dock_php(self):
		os.system("docker pull ahmedhassank/php:latest")
		os.system("docker run -p 9000:9000 --name php ahmedhassank/php:latest")
		os.system("docker start php")

		

	#Funciones para poder ajustar y modificar las caracteristicas del programa

	def control_bt_minimizar(self):
		self.showMinimized()		

	def  control_bt_normal(self): 
		self.showNormal()		
		self.ui.bt_restaurar.hide()
		self.ui.bt_maximizar.show()

	def  control_bt_maximizar(self): 
		self.showMaximized()
		self.ui.bt_maximizar.hide()
		self.ui.bt_restaurar.show()

	def mover_menu(self):
		if True:			
			width = self.ui.frame_lateral.width()
			normal = 0
			if width==0:
				extender = 200
			else:
				extender = normal
			self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()

	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()

	def mover_ventana(self, event):
		if self.isMaximized() == False:			
			if event.buttons() == QtCore.Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()

		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()

#Para iniciar el programa

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	


