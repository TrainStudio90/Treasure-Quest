# Библиотеки

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QRadioButton, QVBoxLayout,QHBoxLayout,QGroupBox
from PyQt5.QtCore import Qt
from random import randint, shuffle

# Объекты

class QuestionBox():
	def __init__ (self, my_question, win_word,wrong_word1,wrong_word2, wrong_word3):
		self.my_question = my_question
		self.win_word = win_word 
		self.wrong_word1 = wrong_word1
		self.wrong_word2 = wrong_word2
		self.wrong_word3 = wrong_word3


def action():
	global is_correct
	my_buttonLock = False
	is_correct = False
	if SendButton.text() == 'Отправить':
		for i in AnsButtonsList:
			if i.isChecked():
				my_buttonLock = True
		if my_buttonLock:
			if questionscount< 1 :
					
				SendButton.hide()
				TitleText.hide()
					
					
			else:
				SendButton.setText('Следующий вопрос')
			for i in AnsButtonsList:
				if i.isChecked():
					if i.text() == question_pack[num].win_word:
						is_correct = True
			if questionscount <1 :
				show_total()
			else:
				show_result()
	elif SendButton.text() == 'Следующий вопрос' :
		SendButton.setText('Отправить')
			
		hide_result()

def show_result():
	global is_correct, totalcount
	if is_correct:
		ResText.setText('Верно!')
		totalcount+=1
	else:
		ResText.setText('Неверно! Правильный ответ: '+question_pack[num].win_word)
	
	AnsGroup.hide()
	Results.show()

def show_total():
	global is_correct, totalcount
	if is_correct:
		totalcount+=1
	if totalcount>0:
		ResText.setText('Итог: '+str(totalcount)+' из 5!\nВы на '+str(int(totalcount/5*100))+'% знаток \"Острова сокровищ\"!')
	else:
		ResText.setText('Итог: 0 из 5...\nСоветуем пересмотреть \"Остров сокровищ\" с начала.')
	
	AnsGroup.hide()
	Results.show()

def start_the_game():
    Vline.show() 

def hide_result():
	global questionscount, num


	question_pack.remove(question_pack[num])
	questionscount-=1
	num = randint(0,questionscount+1)

	TitleText.setText(question_pack[num].my_question)
	AnsButton1.setText(question_pack[num].win_word)
	AnsButton2.setText(question_pack[num].wrong_word1)
	AnsButton3.setText(question_pack[num].wrong_word2)
	AnsButton4.setText(question_pack[num].wrong_word3)

	shuffle(AnsButtonsList)
	buttonsLine1.addWidget(AnsButtonsList[0],alignment = Qt.AlignCenter)
	buttonsLine1.addWidget(AnsButtonsList[1],alignment = Qt.AlignCenter)
	buttonsLine2.addWidget(AnsButtonsList[2],alignment = Qt.AlignCenter)
	buttonsLine2.addWidget(AnsButtonsList[3],alignment = Qt.AlignCenter)


	for i in AnsButtonsList:
		i.setAutoExclusive(False)
		i.setChecked(False)
	for i in AnsButtonsList:
		i.setAutoExclusive(True)



	AnsGroup.show()
	Results.hide()









# Подготовка данных

question_pack = list()

question_data = QuestionBox('Что не характеризует Билли Бонса?','Туп','Много пьёт','Всегда простужен','У него есть карта Флинта')
question_pack.append(question_data)
question_data = QuestionBox('Завершите цитату: \"Билли обрадуется мне как ... \"','Выпивке','Старому другу','Брату','Подарку')
question_pack.append(question_data)
question_data = QuestionBox('Как звали мальчика из песни, который любил деньги?','Бобби','Билли','Боря','Не было сказано')
question_pack.append(question_data)
question_data = QuestionBox('Как Трелони расправился с пиратами во время защиты наблюдательного пункта?','Загнал пиратов в ловушку','Поссорил пиратов','В ближнем бою','Расстрелял из ружья') # лучше заменить
question_pack.append(question_data)
question_data = QuestionBox('На что не делался акцент во вставочных песнях?','Повседневная жизнь пиратов','Употребление рома','Курение','Жадность')
question_pack.append(question_data)

#                                              Дополнение:
question_data = QuestionBox('Что не характеризует Джимми Гоккинса?','Слабый','Слушает маму','Не женат','Добрый')
question_pack.append(question_data)
question_data = QuestionBox('Флаг какой страны был поднят на наблюдательном пункте?','Флаг Великобритании','Флаг Америки','Флаг Франции','Флаг России')
question_pack.append(question_data)
question_data = QuestionBox('Были ли показаны мультяшные спецэффекты в моментах вставочных песнен?','Да','С появлением Билли','Только во втором фильме','Нет')
question_pack.append(question_data)
question_data = QuestionBox('Что означает \"Чёрная метка\"?','Шанс на исправление','Смерть близкого человека','Состояние пациента','Сигнал о помощи')
question_pack.append(question_data)
question_data = QuestionBox('Сражался ли Смоллет с пиратами во время защиты наблюдательного пункта?','Нет, он не мог','Да','Его не было на поле боя','Нет, он был ранен')
question_pack.append(question_data)

# Настройки окна

app = QApplication([])

screen = QWidget()
screen.setWindowTitle('Memory Card')
screen.resize(1000,800)
screen.show()

Vline =  QVBoxLayout()
screen.setLayout(Vline)

# Размещение кнопок
totalcount = 0
questionscount = 4
num = randint(0,4)

TitleText = QLabel(question_pack[num].my_question)
SendButton = QPushButton('Отправить')

SendButton.clicked.connect(action)

Vline.addWidget(TitleText,alignment = Qt.AlignCenter)


AnsGroup = QGroupBox('Варианты ответов:')
Vline.addWidget(AnsGroup,alignment = Qt.AlignCenter)

LineButtons = QVBoxLayout()
AnsGroup.setLayout(LineButtons)

buttonsLine1 = QHBoxLayout()
LineButtons.addLayout(buttonsLine1)
buttonsLine2 = QHBoxLayout()
LineButtons.addLayout(buttonsLine2)


AnsButton1 = QRadioButton(question_pack[num].win_word)

AnsButton2 = QRadioButton(question_pack[num].wrong_word1)

AnsButton3 = QRadioButton(question_pack[num].wrong_word2)

AnsButton4 =QRadioButton(question_pack[num].wrong_word3)

AnsButtonsList = [AnsButton1,AnsButton2,AnsButton3,AnsButton4]

shuffle(AnsButtonsList)



buttonsLine1.addWidget(AnsButtonsList[0],alignment = Qt.AlignCenter)
buttonsLine1.addWidget(AnsButtonsList[1],alignment = Qt.AlignCenter)
buttonsLine2.addWidget(AnsButtonsList[2],alignment = Qt.AlignCenter)
buttonsLine2.addWidget(AnsButtonsList[3],alignment = Qt.AlignCenter)

Results = QGroupBox('Ответ:')
Vline.addWidget(Results,alignment = Qt.AlignCenter)

Lineresults = QVBoxLayout()
Results.setLayout(Lineresults)

ResText = QLabel('')
Vline.addWidget(ResText,alignment = Qt.AlignCenter)
Lineresults.addWidget(ResText,alignment = Qt.AlignCenter)
Results.hide()

























Vline.addWidget(SendButton,alignment = Qt.AlignCenter)

# Hline1 =  QHBoxLayout()
# Vline.addLayout(Hline1)








































































































































app.exec_()
