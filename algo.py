#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets  import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QRadioButton
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()

main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People')
main_win.move(100,100)
main_win.resize(400,200)
#создание виджетов главного окна
 
question = QLabel("Кто выйграл в турнире по CS:GO 'PGL Major Kraków 2017'")

btn_answer1 = QRadioButton('Astralis')
btn_answer2 = QRadioButton('Fnatic')
btn_answer3 = QRadioButton('Gambit')
btn_answer4 = QRadioButton('Navi')

layout_main = QVBoxLayout()

layout_main.addWidget(question, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer4, alignment = Qt.AlignCenter)

main_win.setLayout(layout_main)

def show_win():#правильный ответ
    victory_win = QMessageBox()
    victory_win.setText("Верно! Вы выиграли набор из ковра, мыши и клавиатуры")
    victory_win.exec_()
def show_lose(): #ошибка
    victory_win = QMessageBox()
    victory_win.setText("Нет, в этом году Major выйграла команда Gambit ")
    victory_win.exec_()


btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_win)
btn_answer4.clicked.connect(show_lose)

main_win.show()
app.exec_()

#расположение виджетов по лэйаутам

#обработка нажатий на переключатели
 
#отображение окна приложения b
