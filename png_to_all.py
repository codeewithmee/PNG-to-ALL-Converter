from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
import sys
import os


class Png_to_All(QtWidgets.QWidget):
 	"""docstring for Png_to_All"""
 	def __init__(self):
 		QMainWindow.__init__(self)
 		self.file_path = ""
 		self.convert_list = ["jpg","webp"]
 		self.setWindowTitle("Png Converter")
 		self.ui()
 		self.show()


 	def ui(self):
 		self.label_1 = QLabel("Select the Png file ")
 		self.label_2 = QLabel("Convert the file")
 		self.option = QComboBox(self)
 		self.option.addItems(self.convert_list)
 		self.option.activated[str].connect(self.onChanged)
 		self.select_btn = QPushButton('Browse..',self)
 		self.type_space = QLineEdit('')
 		self.download_btn = QPushButton('Convert',self)

 		hbox = QHBoxLayout()
 		hbox.addWidget(self.type_space)
 		hbox.addWidget(self.select_btn)
 		hbox.addWidget(self.option)
 		hbox.addWidget(self.download_btn)

 		vbox = QVBoxLayout()
 		vbox.addWidget(self.label_1)
 		vbox.addWidget(self.label_2)
 		vbox.addLayout(hbox)

 		self.setLayout(vbox)
 		self.select_btn.clicked.connect(lambda x : self.select_path() )
 		self.download_btn.clicked.connect(lambda x : self.converter())
 		

 	def onChanged(self, text):
 		self.label_2.setText(f"Convert png to {text}")
 		self.label_2.adjustSize()

 	def select_path(self):
 		options = QFileDialog.Options()
 		options |= QFileDialog.DontUseNativeDialog
 		self.file_path, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "", options=options)
 		self.type_space.setText(self.file_path)

 	def converter(self):
 		try:
 			im = Image.open(self.file_path)
 			rgb_im = im.convert("RGB")
 			text = self.option.currentText()
 			if text  == "jpg":
 				save_path = self.download_path("jpg")
 				rgb_im.save(save_path)
 				
 			elif text == "webp":
 				save_path = self.download_path("webp")
 				rgb_im.save(save_path)
 				
 		except Exception as e:
 			raise e


 	def download_path(self,format):
 		path, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",f"Untitled.{format}","All Files (*);;Text Files (*.txt)")
 		return path

 	


if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = Png_to_All()
	sys.exit(App.exec())
 		

