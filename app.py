# main file of application

import sys
import PyQt5 as pq
import PyQt5.QtWidgets as pqwid
import controllers as controllers

app = pqwid.QApplication(sys.argv)
window = pqwid.QWidget()
window.setWindowTitle('App 07.03.2022')
window.setGeometry(600, 400, 600, 200) # topleft position to window popup then size x,y,width,heigth
window.move(400, 250)


button = pqwid.QPushButton('click',parent=window)
button.move(60,60)
button.clicked.connect(controllers.Test)

# loop

window.show()
sys.exit(app.exec_())