import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)

window = QWidget()

window.setGeometry(50,50,320,200)
window.setWindowTitle("PyQT5 Example")

#Sean's Label
seanLabel = QLabel(window)
seanLabel.setText("Hi, Sean here!")
seanLabel.move(110,85)

#Alex
alexLabel = QLabel(window)
alexLabel.setText("Tony The Ant Means Anthony.")
alexLabel.move(100,80)

#Anthony
tonyLabel = QLabel(window)
tonyLabel.setText("Yeet")
tonyLabel.move(185, 70)

#Justin
justinLabel = QLabel(window)
justinLabel.setText("I like apples")
justinLabel.move(150, 75)

#Quingyun
qingyunLabel = QLabel(window)
qingyunLabel.setText("Heloo")
qingyunLabel.move(165,65)




window.show()

sys.exit(app.exec_())