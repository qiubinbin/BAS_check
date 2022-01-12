import json
import sys

from PySide2.QtCore import Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QCheckBox, QListWidgetItem


class Setting:
	def __init__(self):
		self.ui = QUiLoader().load('setting.ui')
		self.initUI()
		self.ui.checkBox.setTristate(True)
		self.ui.checkBox.stateChanged.connect(self.select)
		self.ui.checkBox.setCheckState(Qt.Checked)
		self.checkedlist = []
	
	def initUI(self):
		with open('configure.json', encoding='utf-8', mode='r') as f:
			json_data = json.load(f)
			for i in json_data['category'].keys():
				box = QCheckBox(i + ' ' + json_data['category'][i])
				box.setToolTip(i)
				box.setCheckState(Qt.Checked)
				box.stateChanged.connect(self.partialselect)
				item = QListWidgetItem()
				self.ui.listWidget.addItem(item)
				self.ui.listWidget.setItemWidget(item, box)
	
	def partialselect(self):
		items = self.ui.listWidget.findChildren(QCheckBox)
		check = 0
		uncheck = 0
		for i in items:
			if i.checkState() == Qt.Checked:
				check += 1
			elif i.checkState() == Qt.Unchecked:
				uncheck += 1
		if check == len(items):
			self.ui.checkBox.setCheckState(Qt.Checked)
		elif uncheck == len(items):
			self.ui.checkBox.setCheckState(Qt.Unchecked)
		else:
			self.ui.checkBox.setCheckState(Qt.PartiallyChecked)
	
	def select(self):
		if self.ui.checkBox.checkState() == Qt.Checked:
			for i in self.ui.listWidget.findChildren(QCheckBox):
				i.setCheckState(Qt.Checked)
		elif self.ui.checkBox.checkState() == Qt.Unchecked:
			for i in self.ui.listWidget.findChildren(QCheckBox):
				i.setCheckState(Qt.Unchecked)
	
	def getchecked(self):
		self.checkedlist.clear()
		
		for i in self.ui.listWidget.findChildren(QCheckBox):
			if i.checkState() == Qt.Checked:
				self.checkedlist.append(i.toolTip())
		return self.checkedlist
	
	def show(self):
		self.ui.show()


if __name__ == "__main__":
	app = QApplication([])
	window = Setting()
	window.show()
	sys.exit(app.exec_())
