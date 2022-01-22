import sys
from PySide2.QtCore import Slot, Qt, QThread
from PySide2.QtGui import QPixmap, QMovie
from PySide2.QtWidgets import QApplication, QSplashScreen, QLabel


class Loading(QThread):
	def __init__(self):
		super(Loading, self).__init__()
		self.pixmap = QPixmap("loading.gif")
		self.splash = QSplashScreen(self.pixmap)
		self.splashlabel = QLabel(self.splash)
		self.splashgif = QMovie("loading.gif")
		self.splashlabel.setMovie(self.splashgif)
		self.splash.setWindowModality(Qt.ApplicationModal)
		self.splashgif.start()
		self.ishow = False

	def show(self):
		self.splash.show()

	def close(self):
		self.splash.close()

	def run(self):
		while self.ishow:
			self.show()

	@Slot()
	def getsignal(self, sig):
		print(sig)
		if sig:
			self.ishow = True
		else:
			self.ishow = False


if __name__ == "__main__":
	app = QApplication([])
	window = Loading()
	window.show()
	sys.exit(app.exec_())
