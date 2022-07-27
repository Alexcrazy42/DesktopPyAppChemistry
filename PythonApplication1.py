import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import  QCursor
import os 
from PIL import Image




# 3 кнопки отфотошопить: start_window + две на window 
# два видоса: занимательная химия + менделеев 
# сашин текст в Window_3


class MyDefs(QtWidgets.QWidget): 
    def make_nice_text(self, label, text, x, y, width, height): 
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(x, y, width, height))
        label.setStyleSheet("color: rgb(255, 0, 0);"
                                        "font-weight: bold;"
                                        "font-family: Segoe Print; "
                                        "font-size: 30px;"
                                        "text-align: center;")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText(text)
        label.setWordWrap(True)

    def make_pict(self, label, centralwidget, x, y, width, height, path_to_file): 
        label = QtWidgets.QLabel(centralwidget)
        label.setGeometry(QtCore.QRect(x, y, width, height))
        label.setPixmap(QtGui.QPixmap(path_to_file)) 

    def make_text(self, label, text, x, y, width, height): 
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(x, y, width, height))
        label.setStyleSheet("color: black; \n"
                            "font-family: Times New Roman; \n"
                            "font-size: 20px;")
        
        label.setText(text)
        label.setWordWrap(True)

    
        
    
    
       
class Start_Window(QtWidgets.QWidget): 
    def __init__(self, parent=None):
        
        super(Start_Window, self).__init__(parent, QtCore.Qt.Window)
        self.main()

    def main(self): 
        self.setObjectName("self")
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        

        # первая кнопка 
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 400, 270, 170))
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 21px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Дмитрий Менделеев")

        # вторая кнопка
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(363, 400, 270, 170))
        self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 21px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Принцип появления\n названий \n химических элементов")

        # третья кнопка
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(694, 400, 270, 170))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 21px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Карта химических \n элементов")

        #4 кнопка
        


        #5 кнопкка
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 30, 430, 350))
        self.pushButton_5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "background-image: url(C:/img/видос_1.jpg)")
        self.pushButton_5.setObjectName("pushButton_2")
        

        #6 кнопка
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 30, 430, 350))
        self.pushButton_6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "background-image: url(C:/img/видос_2.jpg)")
        self.pushButton_6.setObjectName("pushButton_2")
        


        self.setWindowTitle("Химия")
        self.pushButton.clicked.connect(self.btn_clk1)
        self.pushButton_2.clicked.connect(self.btn_clk2)
        self.pushButton_3.clicked.connect(self.btn_clk3)
        self.pushButton_5.clicked.connect(self.btn_clk_5)
        self.pushButton_5.clicked.connect(self.btn_clk_5)
        self.pushButton_6.clicked.connect(self.btn_clk_6)
        self.show()

        # 1 кнопка 
    def btn_clk1(self):
        self.newindow = Window_be4(self)
        self.newindow.setWindowTitle("Биография Дмитрия Ивановича Менделеева")
        
        Window2.main(self.newindow)
        
        self.newindow.show()

    # 2 кнопка
    def btn_clk2(self):
        self.newindow = Window3(self)
        self.newindow.setWindowTitle("Принцип появления названий химических элементов")
        
        Window3.main(self.newindow)
        self.newindow.show()

    # 3 кнопка
    def btn_clk3(self):
        self.newindow = Window4(self)
        self.newindow.setWindowTitle("География химических элементов")

        Window4.main(self.newindow)
        self.newindow.show()

    def btn_clk_5(self):
        os.startfile("C:/img/менделеев.mp4")

    def btn_clk_6(self):
        os.startfile("C:/img/видос_2.mp4")
        
#дать нормальные названия для кнопок


class Window_be4(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_be4, self).__init__(parent, QtCore.Qt.Window)


    
    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        

        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        
        self.text = "Оксид этого элемента был впервые получен в 1798 году французским химиком Луи Никола Вокленом (1763–1829) при анализе минерала берилла Be3Al2Si6O18. Такой же состав имеют изумруд и аквамарин (цвет возникает из? за примесей различных элементов). Название минерала (по гречески beryllos) восходит к названию города Белур (Велур) в Южной Индии, недалеко от Мадраса; с древних времен в Индии были известны месторождения изумрудов. Соли бериллия оказались сладкими (тогда не знали об их ядовитости), поэтому новый элемент называли также глицинием, от греч. Glykys – «сладкий». А в «Основах химии» Д. И. Менделеева бериллий называется глицием. Для бериллия характерны две степени окисления — 0 и +2. Гидроксид бериллия(II) амфотерен, причём как основные, так и кислотные свойства выражены слабо. "
        self.text_2 = "Степень окисления +1 у бериллия была получена при исследовании процессов испарения бериллия в вакууме в тиглях из оксида бериллия ВеО с образованием летучего оксида Ве2O в результате сопропорционирования ВеО + Be = Ве2O. По многим химическим свойствам бериллий больше похож на алюминий, чем на находящийся непосредственно под ним в таблице Менделеева магний  (проявление «диагонального сходства»). Металлический бериллий относительно мало реакционноспособен при комнатной температуре. В компактном виде он не реагирует с водой и водяным паром даже при температуре красного каления и не окисляется воздухом до 600 °C. Порошок бериллия при поджигании горит ярким пламенем, при этом образуются оксид и нитрид. Галогены реагируют с бериллием при температуре выше 600 °C, а халькогены требуют ещё более высокой температуры. Аммиак взаимодействует с бериллием мпри температуре выше 1200 °C с образованием нитрида Be3N2, а углерод даёт карбид Ве2С при 1700 °C. С водородом бериллий не реагирует. "

        MyDefs.make_nice_text(self, self.label, "Бериллий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 52, 186, 207, "C:/img/be4.jpg")
        MyDefs.make_text(self, self.label_3, self.text, 207, 40, 790, 236)
        MyDefs.make_pict(self, self.label_4, self.centralwidget, 795, 305, 200, 295, "C:/img/be4_2.jpg")
        MyDefs.make_text(self, self.label_5, self.text_2, 16, 279, 777, 292)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_sc21(QtWidgets.QWidget): 
    def __init__(self, parent=None):
        super(Window_sc21, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        

        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        
        self.text = "Скандий — элемент побочной подгруппы третьей группы, четвёртого периода периодической системы химических элементов Д. И. Менделеева, с атомным номером 21. Обозначается символом Sc (лат. Scandium). Простое вещество скандий (CAS-номер: 7440-20-2) — лёгкий металл серебристого цвета с характерным жёлтым отливом. Существует в двух кристаллических модификациях: альфа-Sc с гексагональной решёткой типа магния, бета-Sc с кубической объёмноцентрированной решёткой, температура перехода - 1336 °C.  Элемент был предсказан Д. И. Менделеевым (как эка-бор) и открыт в 1879 году шведским химиком Ларсом Нильсоном. Л. Нильсон назвал элемент в честь Скандинавии."
        self.text_2 = "Скандий — лёгкий металл серебристого цвета с характерным жёлтым отливом. Существует в двух кристаллических модификациях: альфа-Sc с гексагональной решёткой типа магния, бета-Sc с кубической объёмноцентрированной решёткой, температура перехода 1336 °C. Температура плавления 1541 °C, температура кипения 2837 °C. Скандий — мягкий металл, с чистотой 99,5% и выше легко поддается механической обработке. Главным по объёму применением скандия является его применение в алюминиево-скандиевых сплавах, применяемых в спортивной экипировке — везде, где требуется высокопрочные материалы. В сплаве с алюминием скандий обеспечивает дополнительную прочность и ковкость. Применение скандиевых сплавов в авиации и ракетостроении позволит значительно снизить стоимость перевозок и резко повысить надёжность эксплуатируемых систем."
        
        MyDefs.make_nice_text(self, self.label, "Скандий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 52, 186, 207, "C:/img/sc21.jpg")
        MyDefs.make_text(self, self.label_3, self.text, 207, 40, 790, 236)
        MyDefs.make_nice_text(self, self.label, "Свойства и применение", 0, 276, 1000, 40)
        MyDefs.make_text(self, self.label_3, self.text_2, 0, 316, 738, 600 - 316)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 739, 319, 259, 600 - 319, "C:/img/sc21_2.jpg")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made        

class Window_ga31(QtWidgets.QWidget): 
    def __init__(self, parent=None):
        super(Window_ga31, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
        
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0

        self.text = "Галлий — элемент главной подгруппы третьей группы четвёртого периода периодической системы химических элементов Д. И. Менделеева, атомный номер 31. Обозначается символом Ga (лат. Gallium). Относится к группе лёгких металлов. Простое вещество галлий (CAS-номер: 7440-55-3) — мягкий пластичный металл серебристо-белого (по другим данным светло-серого) цвета с синеватым оттенком. Д. И. Менделеев в соответствии с открытым им в марте 1869 года периодическим законом предсказал существование этого элемента, назвав его эка-алюминием. Поль Эмиль Лекок де Буабодран назвал его в честь своей родины Франции, по её латинскому названию — Галлия (Gallia). Примечательно так же, что символ Франции — петух (по-французски — le coq), так что в названии элемента его первооткрыватель неявно увековечил и свою фамилию. Кроме того на латыни «петух» — gallus. Открытие галлия — первое подтверждение справедливости выявленных Д. И. Менделеевым закономерностей."
        self.text_1 = """   Галлий образует полимерные гидриды:
    4LiH + GaCl3 = Li[GaH4] + 3LiCl
    Устойчивость ионов падает в ряду BH4- → AlH4- → GaH4-. Ион BH4- устойчив в водном растворе, AlH4- и     GaH4- быстро гидролизуются:
    GaH4— + 4H2O = Ga(OH)3 + OH- + 4H2-
    При нагревании под давлением галлий реагирует с водой:
    2Ga + 4H2O = 2GaOOH + 3H2-
    С минеральными кислотами Ga медленно реагирует с выделением водорода:
    2Ga + 6HCl = 2GaCl3 + 3H2↑
                        """

        MyDefs.make_nice_text(self, self.label, "Галлий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 810, 42, 186, 280, "C:/img/ga31.jpg")
        MyDefs.make_text(self, self.label, self.text, 0, 40, 809, 280)
        MyDefs.make_nice_text(self, self.label, "Химические свойства", 0, 320, 1000, 40)
        MyDefs.make_text(self, self.label, self.text_1, 0, 360, 1000, 200)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

    
class Window_sr38(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_sr38, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0

        self.text = "Cтронций - элемент II группы периодической системы; атомный номер 38, атомная масса 88. Открыт А. Крофордом (Шотландия) в 1790 г, выделен Деви в 1808 г. Назван в честь лат. Strontian (Шотландия). Стронций - мягкий металл серебристо-белого цвета, относится к щелочноземельным металлам. Химически очень активен. Реагирует с водой, горит на воздухе. Применяется при производстве кинескопов телевизионной аппаратуры. При взрыве ядерного заряда образуются радиоактивные изотопы стронция, опасные для жизни человека. Стронций используется в металлургии, производстве аккумуляторов и пиротехнических средств. В медицине радиоактивные изотопы 89Sr и 90Sr применяют в лучевой терапии костных опухолей. Как уже отмечалось, изотоп стронция (90Sr) может образовываться при ядерных взрывах и авариях на объектах атомной энергетики и приводить к поражению костного мозга, способствовать развитию лейкемии и рака костей."
        self.text_1 = """
    Стронций в своих соединениях всегда проявляет валентность +2. По свойствам стронций близок к кальцию и барию, занимая промежуточное положение между ними.
    В электрохимическом ряду напряжений стронций находится среди наиболее активных металлов (его нормальный электродный потенциал равен −2,89 В. Энергично реагирует с водой, образуя гидроксид:
    Sr + 2H2O = Sr(OH)2 + H2↑
    Взаимодействует с кислотами, вытесняет тяжелые металлы из их солей. С концентрированными кислотами (H2SO4, HNO3) реагирует слабо.
        """

        MyDefs.make_nice_text(self, self.label, "Стронций", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 42, 186, 207, "C:/img/sr38.jpg")
        MyDefs.make_text(self, self.label, self.text, 207, 40, 791, 249)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 997 - 242, 300, 242, 300, "C:/img/sr38_2.jpg")
        MyDefs.make_text(self, self.label, self.text_1, 0, 300, 997-243, 249)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made


class Window_y39(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_y39, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0

        self.text = "Минерал иттербит, который дал имя иттрию, назван в честь деревни Иттербю (Ytterby) расположенной на острове Руслаген в Швеции. В дальнейшем, минерал иттербит изменил свое название на гадолинит в честь своего первого исследователя (и первооткрывателя иттрия) Юхана Гадолина, финского ученого. Иттрий — элемент побочной подгруппы третьей группы пятого периода периодической системы химических элементов, атомный номер 39. Обозначается символом Y (Yttrium). Простое вещество иттрий (CAS-номер: 7440-65-5) — металл светло-серого цвета. Существует в двух кристаллических модификациях: альфа-Y с гексагональной решёткой типа магния, бета-Y с кубической объёмноцентрированной решёткой типа альфа-Fe, температура перехода - 1482 °C."
        self.text_1 = """Тетраборид иттрия находит применение в качестве материала для управления атомным реактором (имеет малое газовыделение по гелию и водороду).
Ортотанталат иттрия синтезируется и используется для производства рентгеноконтрастных покрытий.
Синтезированны иттрий-алюминиевые гранаты («сиграны»)(ИАГ), имеющие ценные физико-химические свойства, могут применяться и в ювелирном деле, и уже довольно давно применяемые в качестве технологичных и относительно дешёвых твердотельных лазеров. Важным лазерным материалом является ИСГГ — иттрий-скандий-галлиевый гранат.
Феррит иттрия применяется для производства супер-ЭВМ, и хотя он уступает ферриту скандия в несколько раз, он дешевле.
    """

        MyDefs.make_nice_text(self, self.label, "Иттрий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 42, 186, 207, "C:/img/y39.jpg")
        MyDefs.make_text(self, self.label, self.text, 207, 40, 791, 240)
        MyDefs.make_nice_text(self, self.label, "Применение", 0, 280, 1000, 40)
        MyDefs.make_text(self, self.label, self.text_1, 0, 320, 1000, 240)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made


class Window_ru44(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_ru44, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        self.label_6 = 0
        
        self.text = "Элемент назван в честь России, по её латинскому названию — Рутения (Ruthenia). Рутений – один из аналогов платины. Он самый легкий и, если можно так выразиться, самый «неблагородный» из платиновых металлов. Рутений – первый элемент, который позволял связать азот воздуха в химическое соединение (комплексное соединение рутения), подобно тому как это делают некоторые бактерии. Рутений образуется при работе ядерных реакторов и при взрыве атомных бомб. Это один из наиболее неприятных осколочных элементов. Рутений в зависимости от способа его получения является матово-серым или серебристо-белым блестящим металлом, обладающим чрезвычайно большой твердостью; при этом он настолько хрупок, что его можно легко растереть в порошок. Он очень тугоплавок и плавится при значительно более высокой температуре, чем платина."
        self.text_2 = "В электрической дуге при плавлении Ru одновременно испаряется. Он переходит в газовую фазу также при сильном прокаливании на воздухе, но в этом случае летит не металл, а четыреокись, устойчивая при очень высоких температурах."

        MyDefs.make_nice_text(self, self.label, "Рутений", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 52, 186, 207, "C:/img/ru44_1.jpg")
        MyDefs.make_text(self, self.label_3, self.text, 207, 40, 790, 236)
        MyDefs.make_text(self, self.label_4, self.text_2, 5, 276, 997, 60)
        MyDefs.make_pict(self, self.label_5, self.centralwidget, 86, 350, 186, 207, "C:/img/ru44.jpg")
        MyDefs.make_pict(self, self.label_6, self.centralwidget, 46 + 490, 350, 520, 252, "C:/img/ru44_2.jpg")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made  

class Window_hf72(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_hf72, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        self.label_6 = 0

        self.text = "Химический элемент IV группы периодической системы, атомный номер 72, атомная масса 178,49. Долгое время химики подозревали, что в циркониевых минералах содержится примесь какого-то неизвестного элемента. Еще в 1845 г. шведский химик Сванберг сообщил об открытии им в цирконе элемента, который он назвал норием (Norium). После этого многие исследователи сообщали об открытии этого элемента, но каждый раз это было ошибкой. В 1895 г. Томсен на основании периодического закона показал, что между редкими землями и танталом должен существовать элемент, отличающийся от редких земель, но близкий к цирконию. В 1911 г. Урбэн, занимаясь выделением иттриевой земли из гадолинита, обнаружил, что одна фракция последнего маточного рассола дает несколько неизвестных спектральных линий. Он пришел к выводу о существовании нового элемента, принадлежащего к группе редких земель, и назвал его кельтием (Celtium)."
        self.text_1 = "После того как Мозели открыл рентгеновские спектры элементов и были установлены их порядковые номера (1913 -1914), оказалось, что новый элемент должен иметь атомный номер 72. Однако линии этого элемента Мозели не обнаружил в кельтии Урбэна. Предполагая, что в этом виновата несовершенная техника определения рентгеновских спектров, Урбэн попросил физика Довилье повторить опыт. Довилье удалось обнаружить две слабые линии, характерные для элемента 72, в связи с чем элементу оставили название кельтий. Но уже в следующем году Костер и Хевеши нашли эти линии и несколько похожих в различных цирконах. Это послужило доказательством, что элемент 72 не принадлежит к редким землям, а является аналогом циркония. Выделенный Хевеши вскоре после этого элемент 72 оба исследователя, будучи датчанами, решили назвать гафнием (Hafnium) от старинного имени г. Копенгагена (Hafnia, или Kjobn- hafn), так как их открытие было сделано в этом городе."

        MyDefs.make_nice_text(self, self.label, "Гафний", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 800, 42, 186, 207, "C:/img/hf_72.jpg")
        MyDefs.make_text(self, self.label_3, self.text, 10, 40, 790, 250)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 10, 295, 200, 265, "C:/img/hf_72_1.jpg")
        MyDefs.make_text(self, self.label_4, self.text_1, 10 + 205, 295, 780, 270)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_re75(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_re75, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        self.label_6 = 0
        
        self.text = "Химический элемент VII группы периодической системы, атомный номер 75, атомная масса 186,207. Поиски предсказанных Менделевым элементов 43 и 76 (эка-марганца и дви-марганца) начались в конце XIX в., но были безуспешными до 20-х годов нашего столетия, когда Ноддаку и Такке удалось определить главные свойства этих недостающих в периодической таблице элементов. Эти ученые систематически изучали руды и минералы, в которых присутствие искомых элементов казалось вероятным. Первым объектом исследований, начатых в 1922 г., была платиновая руда, но из-за ее дороговизны вскоре пришлось переключиться на другие объекты, в частности редкоземельные минералы - колумбит, гадолинит и т. д. "
        self.text_1 = "Результатом трехлетних напряженных трудов Ноддака и Такке, а также Берга по концентрированию отдельных фракций растворов, выделенных из минералов, явилось обнаружение в рентгеновском спектре одной из фракций серии из пяти новых линий. Как оказалось, эти линии принадлежали элементу 75. Исследователи назвали его рением (Rhenium) в честь Рейнской провинции - родины Такке, ставшей к тому времени супругой Ноддака. Вскоре последовало сообщение о том, что супругам Ноддак удалось наблюдать новые линии рентгеновского спектра, принадлежащие элементу 43, названному мазурием (Masurium) в честь Мазурской провинции - родины Ноддака. Впрочем, некоторые историки химии считают, что оба названия содержат большую дозу национализма: рейнская область и мазурские болота оказались во время первой мировой войны местами крупных удачных для германских войск сражений. Открытие мазурия не было подтверждено. Что же касается рения, то в 1926 г. супруги Ноддак выделили его в количестве 2 мг; годом позже в их распоряжении имелось уже около 120 мг рения."

        MyDefs.make_nice_text(self, self.label, "Рений", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 42, 186, 207, "C:/img/re75.jpg")
        MyDefs.make_text(self, self.label_3, self.text, 207, 40, 790, 210)
        MyDefs.make_pict(self, self.label_4, self.centralwidget, 740, 260, 251, 400, "C:/img/re75_1.jpg")
        MyDefs.make_text(self, self.label_5, self.text_1, 10, 253, 725, 330)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_fr87(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_fr87, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        self.label_6 = 0

        self.text = "Этот элемент открыла (по его радиоактивности) в 1939 году Маргарита Катрин Перей (1909–1975), сотрудница Института радия в Париже, а название ему в честь своей родины она дала в 1946 году. Химический элемент - франций (символ Fr, атомный номер 87), выделяется среди своих собратьев по Таблице Менделеева двумя особенностями. Это самый тяжёлый и самый активный щелочной металл. Это самый неустойчивый элемент из обнаруженных в природе – период полураспада самого долгоживущего изотопа 223Fr составляет 22 минуты. Несмотря на то, что Франций был предсказан Менделеевым в 1871 году как эка-цезий, открыт он был лишь в 1939 году Маргаритой Перей в Институте радия в Париже. Изучая продукты распада актиния-227, Перей обнаружила нуклид нового элемента с периодом полураспада около 22 минут. Позже она установила соответствие нового элемента эка-цезию, который предсказал Менделеев. Первым рабочим названием элемента было «актиний К»."
        self.text_1 = "В 1946 году он получил окончательное наименование «франций» - в честь родины первооткрывателя элемента, по аналогии с полонием, который Мария Склодовская-Кюри в 1898 году назвала в честь своей родины — Польши. Такие долгие поиски 87 элемента объясняются редчайшим сочетанием двух факторов: его высокой химической активностью и низкой ядерной устойчивостью. Франций — один из редчайших элементов. Среди элементов, постоянно существующих в земной коре, только астат имеет меньшее содержание. Весь природный франций является радиогенным, его радиоактивный распад компенсируется одновременным возникновением новых атомов франция в качестве промежуточных продуктов распада урана-235 и тория-232. Общее содержание франция в земной коре оценивается в 340 граммов."

        MyDefs.make_nice_text(self, self.label, "Франций", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 810, 42, 186, 207, "C:/img/fr_87.jpg")
        MyDefs.make_text(self, self.label_3, self.text, 10, 41, 796, 270)
        MyDefs.make_pict(self, self.label_4, self.centralwidget, 10, 320, 320, 257, "C:/img/fr_87_1.jpg")
        MyDefs.make_text(self, self.label_5, self.text_1, 345, 297, 650, 270)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 569, 150, 26))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_lu71(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_lu71, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        self.label_6 = 0

        self.text = "Химический элемент III группы периодической системы, атомный номер 71, атомная масса 174,967, относится к лантаноидам. Открытие лютеция (англ. Lutecium, франц. Lutecium, нем. Lutetium) связано с исследованием земли иттербии. История открытия сложна и длительна. Мозандер выделил из иттриевой земли эрбиевую землю (эрбию), а спустя 25 лет, в 1878 г., Мариньяк показал, что в гадолините наряду с эрбией существует еще одна земля, названная им иттербией. В следующем году Нильсон выделил из иттербии землю скандию, содержащую элемент скандий. Затем исследованиями иттербии не занимались до 1905 г., когда Урбэн, а немного спустя, Ауэр фон Вельсбах сообщили, что в иттербии Мариньяка есть еще две новые земли, одна из которых содержит элемент лютеций (Lutetium), а другая - элемент неоиттербий (Neoytterbium). "
        self.text_1 = "Ауэр фон Вельсбах назвал эти же элементы соответственно кассиопеем (Cassiopeium) и альдебаранием (Aldebaranium). Ряд лет в химической литературе употреблялись и те, и другие названия. В 1914 г. Международная комиссия по атомным весам вынесла решение принять для элемента 71 название лютеций, а для элемента 70 - иттербий. Слово лютеций Урбэн произвел от лютеция (Lutetia) - древнее латинское название Парижа (Lutetia Parisorum). В русской литературе до 1940 г. иногда вместо лютеций писали лутеций. Лютеций — металл серебристо-белого цвета, легко поддаётся механической обработке. Он является самым тяжёлым элементом среди лантаноидов как по атомному весу, так и по плотности. Температура плавления лютеция (1663 °C) максимальна среди всех редкоземельных элементов. Благодаря эффекту лантаноидного сжатия среди всех лантаноидов лютеций имеет наименьшие атомный и ионный радиусы. Не радиоактивен. Является проводником."

        MyDefs.make_nice_text(self, self.label, "Лютеций", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 42, 186, 207, "C:/img/lu_71.jpg")
        MyDefs.make_text(self, self.label_3, self.text, 207, 40, 792, 240)
        MyDefs.make_pict(self, self.label_4, self.centralwidget, 765, 285, 225, 325, "C:/img/lu_71_1.jpg")
        MyDefs.make_text(self, self.label_5, self.text_1, 4, 280, 760, 310)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_yb70(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_yb70, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        self.label_6 = 0

        self.text = "Наряду ещё с тремя химическими элементами (иттрий, тербий, эрбий) получил название в честь села Иттербю Первый концентрат иттербия был получен в 1878 году швейцарским химиком. Жан-Шарль Галиссар де Мариньяк. Французский химик Жорж Урбен и австрийский химик Карл Ауэр фон Вельсбах независимо продемонстрировал в 1907–08 годах, что земля Мариньяка состоит из двух оксидов, которые Урбен назвал neoytterbia и lutetia. Эти элементы теперь известны как иттербий и лютеций. Иттербий относится к менее распространенным редкоземельным элементам. В незначительных количествах он встречается во многих редкоземельных минералах, таких как латеритные глины, ксенотим и эвксенит, а также в продуктах ядерного деления. Этот элемент имеет мало практического применения, кроме исследований. Иттербий, как и европий, является двухвалентным металлом. Иттербий — это вязкий и ковкий редкоземельный металл. Не радиоактивен. Является проводником. Основные методы получения иттербия — это восстановление оксида иттербия (III) в вакууме углеродом или лантаном, а также электролизом расплава хлорида YbCl3."
        

        MyDefs.make_nice_text(self, self.label, "Иттербий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 76, 42, 186, 207, "C:/img/yb_70.jpg")
        MyDefs.make_text(self, self.label, self.text , 309, 40, 684, 460)
        
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 6, 290, 300, 300, "C:/img/yb_70_1.jpg")
        MyDefs.make_pict(self, self.label_4, self.centralwidget, 1000, 599, 1, 1, "C:/img/yb_70_1.jpg")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made 

class Window_er68(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_er68, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        
        self.text = "Название дано в честь села Иттербю. Элемент был открыт в 1842 году как оксид. Карл Густав Мосандер, первоначально назвавший его тербия; в путанице, возникшей из-за сходства свойств редкоземельных элементов, названия двух - тербия и эрбия - поменялись местами (около 1860 г.). Эрбий — это мягкий пластичный редкоземельный металл серебристого цвета. Не радиоактивен. Является парамагнетиком. Металлический эрбий получают электролизом расплава хлорида (фторида) эрбия ErCl3 (ErF3), а также кальцийтермическим восстановлением этих солей. Этот элемент встречается во многих редкоземельных минералах; среди наиболее важных - латеритные ионные глины, ксенотим и эвксенит. Эрбий также присутствует в продуктах ядерного деления."
        self.text_1 = "В земной коре эрбий так же богат, как тантал и вольфрам. Чистый эрбий - серебристо-белый металл, относительно устойчивый на воздухе. Он медленно реагирует с водой и быстро растворяется в разбавленных кислотах, за исключением плавиковой кислоты (HF), из-за образования защитного фторидного слоя (ErF 3 ) на поверхности металла. Эрбий используется в дополнение к другим редкоземельным элементам, таким как неодим или гольмий, для легирования лазерных кристаллов в твердотельных лазерах (лазер Er: YAG, см. Также лазер Nd: YAG). Er: YAG лазер в основном используется в медицине. Он также используется при лечении твердых тканей, таких как кости, эмаль и дентин (здоровые и кариозные)."

        MyDefs.make_nice_text(self, self.label, "Эрбий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 42, 186, 207, "C:/img/er_68.jpg")
        MyDefs.make_text(self, self.label, self.text, 207, 40, 791, 209)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 775, 252, 220, 359, "C:/img/er_68_1.jpg")
        MyDefs.make_text(self, self.label, self.text_1, 0, 250, 775, 309)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_ho67(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_ho67, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0

        self.text = "Химический элемент III группы периодической системы, атомный номер 67, атомная масса 164,9304, относится к лантаноидам. Элемент открыт в 1878 - 1879 гг. швейцарским химиком Сорэ, который, исследуя старую эрбиевую землю (эрбию), обнаружил раздвоение спектральных линий. Сорэ обозначил новый элемент индексом Х. Вскоре (1879) шведский химик Клеве выделил из прежней эрбиевой земли некоторое количество солей элемента, окрашенных в оранжевый цвет; они оказались солями элемента Х. Несмотря на то, что Клеве не смог охарактеризовать новый элемент более подробно, чем это сделал Сорэ, он предложил назвать новую землю гольмией (holmia), а элемент - гольмием (Holmium) в честь столицы Швеции Стокгольма, носившего в старину латинское название Гольмия (Holmia); около Стокгольма были найдены редкоземельные минералы, которые исследовал Клеве."

        MyDefs.make_nice_text(self, self.label, "Гольмий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 810, 42, 186, 207, "C:/img/ho_67.jpg")
        MyDefs.make_text(self, self.label, self.text, 0, 40, 809, 247)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_tb65(QtWidgets.QWidget): 
    def __init__(self, parent=None):
        super(Window_tb65, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        self.label_6 = 0

        self.text = "Элемент назван в честь села Иттербю, находящегося на острове Ресарё, входящем в Стокгольмский архипелаг. Тербий (лат. Terbium), Tb, химический элемент III группы периодической системы, атомный номер 65, атомная масса 158,925 4, относится к лантаноидам В 1843 году шведский химик К. Г. Мосандер обнаружил примеси в концентрате Y2O3 и выделил из него три фракции: иттриевую, розовую terbia (которая содержала современный элемент эрбий) и бесцветную erbia (содержала элемент тербий, нерастворимый оксид тербия имеет коричневый оттенок). Из-за бесцветности erbia существование этого соединения долгое время подвергалось сомнению, также были перепутаны названия фракций. Тербий в исходном концентрате составлял около 1%, однако этого было достаточно, чтобы придать ему желтоватый оттенок."
        self.text_1 = "Чистый тербий начале XX века первым получил французский химик Жорж Урбэн, использовавший технологию ионного обмена. Элемент 65. В природе существует в виде одного-единственного стабильного изотопа тербий-159. Элемент редкий, дорогой и используемый пока главным образом для изучения его же собственных свойств. Весьма ограниченно соединения тербия используют в люминофорах, лазерных материалах и ферритах. Своеобразны магнитные свойства тербия: при обычных условиях он – парамагнетик, но при охлаждении до –54°C и ниже приобретает ферромагнитные свойства. В остальном же этот металл достаточно зауряден: серебристо-белого цвета, при нагревании покрывается окисной пленкой... Тербий — это пластичный, мягкий (тербий настолько мягок, что его можно резать ножом) редкоземельный металл серебристо-белого цвета. Не радиоактивен. Является парамагнетиком."

        MyDefs.make_nice_text(self, self.label, "Тербий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 42, 186, 207, "C:/img/tb_65.jpg")
        MyDefs.make_text(self, self.label, self.text, 207, 40, 791, 227)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 695, 270, 300, 315, "C:/img/tb_65_1.jpg")
        MyDefs.make_text(self, self.label, self.text_1, 1, 267, 693, 327)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_eu63(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_eu63, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        self.label_6 = 0

        self.text = "Химический элемент III группы периодической системы, атомный номер 63, атомная масса 151,96, относится к лантаноидам. Открытие европия связано с ранними спектроскопическими работами Крукса и Лекока де Буабодрана. В 1886 г. Крукс, исследуя спектр фосфоресценции минерала самарскита, обнаружил полосу в области длины волн 609 А. Эту же полосу он наблюдал при анализе смеси иттербиевой и самариевой земель. Крукс не дал названия подозревавшемуся элементу и временно обозначил его индексом Я. В 1892 г. Лекок де Буабодран получил от Клеве 3 г очищенной самариевой земли и произвел ее дробную кристаллизацию. Спектроскопировав полученные фракции, он обнаружил ряд новых линий и обозначил предполагаемый новый элемент индексами Z(эпсилон), и Z(дзетта). Четыре года спустя Демарсэ в результате длительной кропотливой работы по выделению из самариевой земли искомого элемента отчетливо увидел спектроскопическую полосу неизвестной земли; он дал ей индекс E." 
        self.text_1 = "Позднее было доказано, что Z(эпсилон), и Z(дзетта) Лекок де Буабодрана, E Демарсэ и аномальные полосы спектра, наблюдавшиеся Круксом, относятся к одному и тому же элементу, названному Демарсэ в 1901 г. европием (Europium) в честь континента Европы. Европий быстро реагирует с водой и разбавленными кислотами, за исключением плавиковой кислоты (HF), в котором он защищен слоем EuF . Европий является очень сильным парамагнетиком при температуре выше 90 К, ниже этой температуры металл упорядочивается антиферромагнитно, образуя спиральную структуру. Как мы уже знаем, в соединениях европий бывает двух- и трехвалентным. Большинство его соединений – белого цвета обычно с кремовым, розоватым или светло-оранжевым оттенком. Соединения европия с хлором и бромом светочувствительны."

        MyDefs.make_nice_text(self, self.label, "Европий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 72, 186, 207, "C:/img/eu_63.jpg")
        MyDefs.make_text(self, self.label, self.text, 207, 40, 791, 270)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 810, 320, 176, 300, "C:/img/eu_63_1.jpg")
        MyDefs.make_text(self, self.label, self.text_1, 1, 310, 808, 270)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_am95(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_am95, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0

        self.text = "Был получен искусственно в 1944 году в Металлургической лаборатории Чикагского университета Гленном Сиборгом с сотрудниками. Внешняя электронная оболочка нового элемента (5f) оказалась аналогичной европию (4f). Поэтому элемент назвали в честь Америки, как европий — в честь Европы. Америций — это радиоактивный ковкий и тягучий металл серебристо-белого цвета. Светится в темноте за счёт собственного α-излучения. Пожалуй, наиболее распространенной сферой применения америция являются бытовые детекторы дыма. Внутри детектора находится немного оксида америция, полученного с помощью изотопа америций-241. Америций-241 вырабатывает альфа-частицы, которые сталкиваются с молекулами воздуха, что приводит к их распаду и образованию электрически заряженных ионов."
        self.text_1 = "Такие заряженные ионы наделяют воздух внутри детектора дыма электропроводностью, а ток проходит от одной стороны детектора к другой.  Когда дым оказывается между передающим и получающим элементами, электропроводность воздуха меняется, что активирует сигнал детектора дыма. Хотя америций достаточно редкий и дорогостоящий в производстве элемент, в каждом детекторе дыма используется совсем небольшое его количество (0,29 микрограмм). Это меньше веса зернышка пыльцы. \n Чем хорош америций? Хорош не всякий америций, а изотоп америций-241. Его период полураспада велик — 433 года, тем не менее его радиоактивность велика: такой америций светится в темноте. При этом америций-241 испускает и альфа-частицы, и гамма-кванты. У этих гамма-квантов энергия невелика, и от них можно защититься свинцовой оболочкой небольшой толщины. Это делает америций неплохим источником альфа-частиц, с которым удобно работать. А учитывая то обстоятельство, что в атомном реакторе его образуется относительно много, такой изотоп удается использовать, выделив его из отработанного топлива АЭС. "

        MyDefs.make_nice_text(self, self.label, "Америций", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 42, 124, 138, "C:/img/am_95.jpg")
        MyDefs.make_text(self, self.label, self.text, 145, 40, 850, 207)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 770, 252, 220, 600 - 252, "C:/img/am_95_1.jpg")
        MyDefs.make_text(self, self.label, self.text_1, 0, 250, 770, 350)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_bk97(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_bk97, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0

        self.text = "Получил свое название от города Беркли, именно там в 1949 году был получен это радиоактивный элемент. Берклий является химическим аналогом тербия, получившего название от небольшого селения Иттербю в Швеции, рядом с которым был обнаружен минерал, содержащий среди прочих редкоземельных металлов и тербий. Поэтому было решено назвать 97-й элемент по названию города Беркли, в котором он был впервые получен. Простое вещество берклий — радиоактивный металл серебристо-белого цвета. "
        self.text_1 = "Установлено, что берклий очень реакционноспособен. В своих многочисленных соединениях он имеет степени окисления + 3 (преимущественно) и + 4. Существование четырехвалентного берклия позволяет отделять этот элемент от других актиноидов и лантаноидов (продуктов деления), которые либо не имеют такой валентной формы, либо труднее в нее переводятся. Взаимодействует с кислородом (оксид и диоксид), галогенами и серой. Известны двойные соли и металлоорганические соединения берклия. Образует комплексные соединения с минеральными и органическими кислотами. Наиболее устойчивы соединения берклия в растворе при степени окисления +3. При рН, близких к щелочной среде, Bk3+ образует нерастворимый основной гидроксид. Оксиды, фториды, фосфаты и карбонаты берклия нерастворимы в воде. В четырехвалентном состоянии берклий является сильным окислителем. \n При введении крысам нитрата 249Вк радионуклид распределяется между скелетом (40 %) и печенью (18 %). Небольшие количества 249Вк определяются в мышцах (9 %), надпочечниках (7,3 %), коже (4,5 %), селезенке (1,3 %) и почках (1,1 %). Тб из костной ткани составляет 500—600 сут. Выведение из организма крыс происходит в основном с мочой 18,2 % и калом 10 %. Максимальные дозы в костной ткани, не влияющие на сокращение продолжительности жизни крыс, составляют 6,3 Гр (β-излучение) при введении 37-108 кБк/кр массы тела крыс. В отдаленные сроки у крыс развиваются остеосаркомы."

        MyDefs.make_nice_text(self, self.label, "Берклий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 42, 124, 138, "C:/img/bk_97.jpg")
        MyDefs.make_text(self, self.label, self.text, 143, 40, 1000 - 144, 140)
        MyDefs.make_text(self, self.label, self.text_1, 0, 180, 1000, 380)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_cf98(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_cf98, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0

        self.text = "Элемент назван в честь Калифорнийского университета в Беркли, где и был получен. Как писали авторы, этим названием они хотели указать, что открыть новый элемент им было так же трудно, как век назад пионерам Америки достичь Калифорнии. Калифорний – чрезвычайно летучий металл. Калифорний представляет собой серебристо-белый металл. Чистый металл податлив и легко режется лезвием. Металлический калифорний начинает испаряться при температуре выше 300 °C под вакуумом. Образует сплавы с лантаноидными металлами, но о них мало что известно Этот химический элемент считается одним из самых дорогих металлов в мире. По оценкам специалистов, его стоимость от 6,5 миллионов долларов за грамм. Главное применение калифорния – в изготовлении мощных и чрезвычайно компактных источников нейтронов. Он также широко используется в медицине и различного рода детекторах."
        self.text_1 = "Благодаря испусканию мощного потока нейтронов его применяют в нейтронно-активационном анализе и в нейтронной радиографии; в геологоразведке и при добыче полезных ископаемых; в сталелитейной, химической, нефтеперерабатывающей, угледобывающей промышленности; в ядерной энергетике и авиационно-космической технике."

        MyDefs.make_nice_text(self, self.label, "Калифорний", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 810, 42, 186, 207, "C:/img/cf_98.jpg")
        MyDefs.make_text(self, self.label, self.text, 0, 40, 808, 250)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 290, 200, 200, "C:/img/cf_98_1.jpg")
        MyDefs.make_text(self, self.label_3, self.text_1, 220, 310, 778, 120)
        MyDefs.make_pict(self, self.label_4, self.centralwidget, 1000, 600, 1, 1, "C:/img/cf_98_1.jpg")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())

#made

class Window_db105(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_db105, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0

        self.text = "Элемент 105 впервые получен на ускорителе Объединенного института ядерных исследований в Дубне в 1970 году группой академика Георгия Николаевича Флерова (1913–1990) и независимо в Беркли (США). Советские исследователи предложили назвать его нильсборием (Ns), в честь датского физика Нильса Хенрика Давида Бора (1885–1962); американцы – ганием (На), в честь Отто Гана (1879–1968), одного из авторов открытия спонтанного деления урана; Комиссия по номенклатуре Международного союза теоретической и прикладной химии (ИЮПАК) предложила назвать элемент жолиотием (Jl), в честь французского физика и радиохимика Фредерика Жолио-Кюри (1897–1956), либо (чтобы никому не было обидно) числительным «уннилпентиум» (Unp), то есть просто 105м."
        self.text_1 = "Символы Ns, Ha, Jl можно было видеть в таблицах элементов, изданных в разные годы. Городок этот упомянут в песне Александра Галича: «И живет-то он не в Дубне атомной, а в НИИ каком-то под Каширою…». Дубний является сверхтяжелым как и все элементы с такими высокими атомными номерами, он очень нестабилен. Самый долгоживущий изотоп дубния, Db, имеет период полураспада около суток. Стабильных изотопов не обнаружено, и расчет ОИЯИ 2012 г. показал, что период полураспада всех изотопов дубния не будет изменено суток. Дубний может быть получен только путем искусственного производства. Согласно периодическому закону, дубний должен принадлежать к группе 5, с ванадием, ниобием и тантал. Изучали свойства элемента исследований, что они в целом согласуются с предсказаниями периодического закона. Тем не менее, могут возникнуть сильные отклонения из-за релятивистских эффектов, которые резко изменяют физические свойства как в атомном, так и в макроскопическом масштабе. Эти свойства по-прежнему сложно измерить по нескольким причинам: трудности производства сверхтяжелых элементов, низкие производства допускают только микроскопические испытания, требования к радиохимической лаборатории для проверки элементов, короткие периоды полураспада этих элементов, и наличие многих нежелательных действий, помимо сверхтяжелых элементов."

        MyDefs.make_nice_text(self, self.label, "Дубний", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 42, 186, 207, "C:/img/db_105.jpg")
        MyDefs.make_text(self, self.label, self.text, 207, 40, 791, 222)
        MyDefs.make_text(self, self.label, self.text_1, 0, 262, 1000, 600-300)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_hs108(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_hs108, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0

        self.text = "Первые надежные данные об элементе 108 получены в 1984 году в Дубне и независимо и одновременно на ускорителе Лаборатории по исследованию тяжелых ионов вблизи Дармштадта – города в федеральной земле Гессен. Латинское название этого старинного немецкого княжества, а затем великого герцогства Гессен-Дармштадт – Hassia, отсюда и название элемента. И с этим элементом была путаница в названиях (раньше его называли ганием). Впервые сообщения об открытии элемента 108 появились в начале 1970 года и были совершенно неожиданными для экстремально короткоживущих и трудноуловимых сверхтяжёлых химических элементов. По результатам экспедиции в пустынном районе вблизи полуострова Челекен у Каспийского моря группой учёных СССР под руководством В. В. Чердынцева на основании фиксирования треков (следов ядер) на образцах минерала молибденита был сделан смелый вывод об обнаружении элемента 108 с атомной массой 267 в природе."
        self.text_1 = "Сообщения об этом «открытии» попала в журнал «Наука и жизнь» (02/1970) и другие СМИ и в апреле 1970 года были обсуждены на заседаниях институтов АН СССР (геохимического, физических проблем). Впоследствии научная достоверность заключения была оспорена как недостаточно доказанная. Физики давно ожидали, что более тяжелый изотоп хассия с массовым числом 270 (108 протонов и 162 нейтрона) окажется гораздо стабильнее. Этот вывод покоится на общепринятых теориях ядерной материи, из которых вытекает, что ядро обладает слоистой структурой. Согласно этой модели, внутри ядер существуют протонные и нейтронные оболочки, каждая из которых может вмещать определенное максимальное число нуклонов. Ядра с полностью заполненными оболочками особенно устойчивы по отношению к распадам. Числа нейтронов и протонов, соответствующих таким оболочкам, называются магическими. Некоторые из магических чисел надежно определены в экспериментах — это, например, 2, 8 и 20."

        MyDefs.make_nice_text(self, self.label, "Хассий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 810, 42, 186, 267, "C:/img/hs_108.jpg")
        MyDefs.make_text(self, self.label, self.text, 0, 40, 810, 270)
        MyDefs.make_text(self, self.label, self.text_1, 0, 310, 1000, 250)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide()) 
#made   

class Window_ds110(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_ds110, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        self.label_6 = 0

        self.text = "Происходит от немецкого «наукограда» Дармштадт, в котором в 1994 году был синтезирован этот элемент. Элемент получил название по месту открытия. Впервые синтезирован 9 ноября 1994 в Центре исследований тяжёлых ионов (нем. Gesellschaft für Schwerionenforschung, GSI), Дармштадт, С. Хофманном, В. Ниновым, Ф. П. Хессбергером, П. Армбрустером, Х. Фолгером, Г. Мюнценбергом, Х. Шоттом и другими. Обнаруженный изотоп имел атомную массу 269. Новый элемент был получен в реакции слияния атомов никеля и свинца в результате бомбардировки свинцовой мишени ионами никеля в ускорителе ионов UNILAC в GSI. Дармштадтий был четвёртым элементом, обнаруженным в GSI. Между 1981 и 1984 гг. там были получены и выделены элементы 107 (борий), 108 (хассий), 109 (мейтнерий)."
        self.text_1 = "После открытия дармштадтия там же были синтезированы элементы 111 (рентгений) и 112. Учёные ОИЯИ из российского наукограда Дубна предлагали назвать этот элемент беккерелием (Bl) в честь открывателя радиоактивности Анри Беккереля (позже это же название стало предлагаться для 113-го элемента, который сейчас называется нихонием). Американская команда в 1997 году предложила название ганиум в честь Отто Гана (ранее это имя использовалось для 105 элемента). Рабочая группа Международного совета по теоретической и прикладной химии (IUPAC) в 2001 году подтвердила открытие нового химического элемента и признала приоритет GSI в этом открытии. В августе 2003 года IUPAC на своей 42-й Генеральной ассамблее в Оттаве официально ввёл в периодическую систему новый химический элемент под номером 110 под названием дармштадтий РадиоактивенОднозначно определить химические характеристики дармштадия тяжело из-за коротких периодов полураспада изотопов дармштадия и ограниченного числа вероятных летучих соединений, которые могут быть изучены в очень небольших масштабах. Дармштадтий должен быть очень тяжелым металлом с плотностью около 34,8 г/см кубический. Для сравнения, самый плотный известный элемент, для которого измерена его плотность, осмий, имеет плотность всего 22,61 г/см кубический."

        MyDefs.make_nice_text(self, self.label, "Дармштадий", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 16, 42, 186, 207, "C:/img/ds_110.jpg")
        MyDefs.make_text(self, self.label, self.text, 207, 40, 791, 227)
        MyDefs.make_text(self, self.label, self.text_1, 0, 267, 1000, 300)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 569, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

class Window_lv116(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window_lv116, self).__init__(parent, QtCore.Qt.Window)

    def main(self): 
       
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_2 = 0
        self.label_3 = 0
        self.label_4 = 0
        self.label_5 = 0
        self.label_6 = 0

        self.text = "Элемент 116 назван в честь знаменитой Ливерморской национальной лаборатории имени Эрнеста Лоуренса, в которой производился синтез элементов. Лаборатория расположена недалеко от города Ливермора в штате Калифорния, а город, в свою очередь, был назван по имени основавшего его фермера Роберта Ливермора, эмигрировавшего в Калифорнию из Англии в 1816 году. Так что в названии этого элемента фактически увековечен никому не известный фермер. Заявление об открытии элементов 116 и 118 в 1999 году в Беркли (США) оказалось ошибочным и даже фальсифицированным Синтез по объявленной методике не был подтверждён в российском, немецком и японском центрах ядерных исследований, а затем и в самих США. Элемент имеет высокую радиоактивность, ведь его изотопы неустойчивы и быстро подвергаются альфа-распаду, что делает его радиотоксичным. Но общебиологического влияния на организм элемент не оказывает, ведь в естественной среде он не находится, а искусственно синтезируется в малых количествах."
        self.text_1 = "Наиболее свойственная ему степень окисления в реакциях и соединениях — +2. Но в соединении с фтором будет проявлять степень окисления +4, что является максимально возможной степенью. А с щелочными металлами или другими достаточно сильными восстановителями ливерморий будет приобретать степень окисления -2. Но такие соединения не обладают большой устойчивостью из-за специфики электронов основной оболочки.Учитывая химические свойства ливермория, можно сделать вывод, что для данного соединения приоритетом является образование катионов, а не анионов. Элемент был также искусственно синтезирован в 2000 году в городе Дубне, России. А точнее в Объединенном институте ядерных исследований расположенном в этом городе."

        MyDefs.make_nice_text(self, self.label, "Ливермоний", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label_2, self.centralwidget, 695, 42, 300, 300, "C:/img/lv_116.jpg")
        MyDefs.make_text(self, self.label, self.text, 3, 40, 691, 340)
        MyDefs.make_text(self, self.label, self.text_1, 1, 380, 997, 180)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

# окно про менделеева
class Window2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent, QtCore.Qt.Window)
        
    def main(self): 
        #self.setStyleSheet("background-image: url(C:/img/для_химии.jpg)")
        self.setObjectName("self")
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg); \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.upper_label = QtWidgets.QLabel(self)
        self.upper_label.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.upper_label.setStyleSheet("color: rgb(255, 0, 0);"
                                        "font-weight: bold;"
                                        "font-family: Segoe Print; "
                                        "font-size: 30px;"
                                        "text-align: center;")
        self.upper_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop) 
        self.upper_label.setWordWrap(True)
        self.upper_label.setObjectName("upper_label")
        self.upper_label.setText("Биография Дмитрия Менделеева")
        self.upper_label.setAlignment(QtCore.Qt.AlignCenter)

        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(310, 70, 681, 300))
        self.label.setStyleSheet("color: black; \n"
                                "font-family: Times New Roman; \n"
                                "font-size: 18px;\n"
                                "font-style: bold;")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(12, 70, 284, 284))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/img/менделеев.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 370, 981, 171))
        self.label_3.setStyleSheet("color: black; \n"
                                "font-family: Times New Roman; \n"
                                "font-size: 18px;\n"
                                "font-style: bold;")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
  
        self.label.setText("<html><head/><body><p>Менделеев Дмитрий Иванович (1834— 1907) - химик, создатель периодической системы химических элементов. Родился 8 февраля 1834 г. в Тобольске в семье директора гимназии. Учился в этой гимназии, затем был принят на отделение естественных наук физико-математического факультета Главного педагогического института в Петербурге. Курс окончил с золотой медалью, однако за годы напряжённых занятий подорвал здоровье. В 1855 г. уехал в Одессу, где преподавал в гимназии при Ришельевском лицее. Благодатный южный климат позволил Менделееву уже в следующем году вернуться в Петербург. Он защитил магистерскую диссертацию и приступил к чтению лекций по органической химии в Петербургском университете. В 1859—1861 гг. посетил Германию «для усовершенствования в науках», а по возвращении на родину издал первый в России учебник по органической химии, который был удостоен Демидовской премии. В 1865 г. Менделеев защитил докторскую диссертацию, заложившую основы учения о растворах. В 1869 г. учёный совершил одно из величайших открытий в истории химии — вывел периодический закон</p><p><br/></p></body></html>")
        self.label_3.setText("<html><head/><body><p>химических элементов. В 1871 г. вышел его классический труд «Основы химии», где обобщались представления о любимой науке. Дмитрий Иванович отдавал много сил преподавательской деятельности — был профессором Петербургского университета, вёл курсы в других учебных заведениях. На склоне лет он отмечал: «Из тысяч моих учеников много теперь повсюду видных деятелей, профессоров, администраторов, и, встречая их, всегда слышал, что доброе в них семя полагал, а не простую отбывал повинность». В 1890 г. Менделеев покинул университет в знак протеста против притеснения студенчества. Несколько лет учёный был консультантом научно-технической лаборатории Морского министерства; в 1892 г. он организовал производство изобретённого им бездымного пороха. С 1892 г. и до конца своей жизни Дмитрий Иванович возглавлял Главную палату мер и весов. Скончался 2 февраля 1907 г. в Петербурге.</p></body></html>")        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 572, 150, 25))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
#made

# окно про экскурс по элементам
class Window3(QtWidgets.QWidget):
    def __init__(self, parent=None): 
        super(Window3, self).__init__(parent, QtCore.Qt.Window)
        
    def main(self): 
        
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg)")
        self.setObjectName("self")
        self.resize(1000, 600)
        self.setFixedSize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        
        
        self.label = 0
        self.label_1 = 0

        self.text = "Каждый химический элемент имеет свое латинское название. В качестве символов по предложению шведского химика Берцелиуса были приняты в большинстве случаев начальные буквы латинских названий химических элементов. В названиях одних элементов отражены важнейшие свойства элементов, например, — водород H - рождающий воду. Бром Br — с древне греческого переводится как «вонючий», его простое вещество представляет собой жидкость с сильным неприятным запахом. Азот N - с древне греческого переводится как «безжизненный»; не поддерживает ни горение, ни дыхание, хотя впоследствии выяснилось, что азот наоборот, крайне необходим для всех живых существ. \n"
        self.text_1 = "Другие элементы названы в честь небесных тел или планет Солнечной системы — селен Se и теллур Te - от греческого Селена — Луна, Теллурис — Земля; уран U; нептуний Np; плутоний Pu. Отдельные названия заимствованы из мифологии. В честь героя древнего мифа Прометея, подарившего людям огонь и обреченного за это на страшные муки, назван химический элемент 61 прометий Pm. Титан Ti- в честь титанов, персонажей древнегреческой"
        self.text_2 = "мифологии, детей Геи (богини земли). Ванадий V - в честь богини любви и красоты Фрейи (древнескандинавский Vanadis — дочь Ванов). В названиях некоторых элементов увековечены имена великих ученых: кюрий (Cm), фермий (Fm), эйнштейний (Es), менделевий(Md), лоуренсий (Lr). Некоторые элементы были названы в честь различных государств или частей света. Эти элементы мы рассмотрим более подробно."


        MyDefs.make_nice_text(self, self.label, "Принцип появления названий химических элементов", 0, 0, 1000, 40)
        MyDefs.make_pict(self, self.label, self.centralwidget, 10, 43, 398, 398, "C:/img/хим_эл.jpg")
        MyDefs.make_text(self, self.label, self.text + self.text_1, 408, 40, 592, 420)
        MyDefs.make_text(self, self.label, self.text_2, 10, 460, 990, 95)


        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 565, 150, 30))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())
   
        

# окно с картой хим элементов
class Window4(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window4, self).__init__(parent, QtCore.Qt.Window) 
    
    def main(self): 
       
        self.resize(1000, 585)
        self.setFixedSize(1000, 585)

        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        self.setStyleSheet("background-image: url(C:/img/карта_мира.jpg)") 
        self.centralwidget = QtWidgets.QWidget(self)

        self.label = 0 
        MyDefs.make_nice_text(self, self.label, "География химических элементов", 0, 0, 1000, 30)


        

        self.button_be4 = 0
        self.button_sc21 = 0    
        self.button_ga31 = 0
        self.button_sr38 = 0
        self.button_y39 = 0
        self.button_ru44 = 0
        self.button_hf72 = 0
        self.button_re75 = 0
        self.button_fr87 = 0
        self.button_db105 = 0
        self.button_hs108 = 0
        self.button_ds110 = 0
        self.button_lv116 = 0
        self.button_eu63 = 0
        self.button_tb65 = 0
        self.button_ho67 = 0
        self.button_er68 = 0
        self.button_yb70 = 0
        self.button_lu71 = 0
        self.button_am95 = 0
        self.button_bk97 = 0
        self.button_cf98 = 0

          
        
        self.button_be4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_be4.setGeometry(QtCore.QRect(123, 114, 48, 48))
        self.button_be4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_be4.setStyleSheet("background-image: url(C:/img/w4_be4.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_be4.clicked.connect(lambda: Window4.fnc_be4(self))

        self.button_sc21 = QtWidgets.QPushButton(self.centralwidget)
        self.button_sc21.setGeometry(QtCore.QRect(174, 214, 48, 48))
        self.button_sc21.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_sc21.setStyleSheet("background-image: url(C:/img/w4_sc21.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_sc21.clicked.connect(lambda: Window4.fnc_sc21(self))

        self.button_ga31 = QtWidgets.QPushButton(self.centralwidget)
        self.button_ga31.setGeometry(QtCore.QRect(679, 214, 48, 48))
        self.button_ga31.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_ga31.setStyleSheet("background-image: url(C:/img/w4_ga31.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_ga31.clicked.connect(lambda: Window4.fnc_ga31(self))

        self.button_sr38 = QtWidgets.QPushButton(self.centralwidget)
        self.button_sr38.setGeometry(QtCore.QRect(123, 266, 48, 48))
        self.button_sr38.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_sr38.setStyleSheet("background-image: url(C:/img/w4_sr38.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_sr38.clicked.connect(lambda: Window4.fnc_sr38(self))

        self.button_y39 = QtWidgets.QPushButton(self.centralwidget)
        self.button_y39.setGeometry(QtCore.QRect(173, 266, 48, 48))
        self.button_y39.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_y39.setStyleSheet("background-image: url(C:/img/w4_y39.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_y39.clicked.connect(lambda: Window4.fnc_y39(self))

        self.button_ru44 = QtWidgets.QPushButton(self.centralwidget)
        self.button_ru44.setGeometry(QtCore.QRect(426, 266, 48, 48))
        self.button_ru44.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_ru44.setStyleSheet("background-image: url(C:/img/w4_ru44.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_ru44.clicked.connect(lambda: Window4.fnc_ru44(self))

        self.button_hf72 = QtWidgets.QPushButton(self.centralwidget)
        self.button_hf72.setGeometry(QtCore.QRect(225, 315, 48, 48))
        self.button_hf72.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_hf72.setStyleSheet("background-image: url(C:/img/w4_hf72.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_hf72.clicked.connect(lambda: Window4.fnc_hf72(self))

        self.button_re75 = QtWidgets.QPushButton(self.centralwidget)
        self.button_re75.setGeometry(QtCore.QRect(375, 315, 48, 48))
        self.button_re75.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_re75.setStyleSheet("background-image: url(C:/img/w4_re75.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_re75.clicked.connect(lambda: Window4.fnc_re75(self))

        self.button_fr87 = QtWidgets.QPushButton(self.centralwidget)
        self.button_fr87.setGeometry(QtCore.QRect(73, 367, 48, 48))
        self.button_fr87.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_fr87.setStyleSheet("background-image: url(C:/img/w4_fr87.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_fr87.clicked.connect(lambda: Window4.fnc_fr87(self))
        
        self.button_lu71 = QtWidgets.QPushButton(self.centralwidget)
        self.button_lu71.setGeometry(QtCore.QRect(933, 440, 48, 48))
        self.button_lu71.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_lu71.setStyleSheet("background-image: url(C:/img/w4_lu71.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_lu71.clicked.connect(lambda: Window4.fnc_lu71(self))

        self.button_yb70 = QtWidgets.QPushButton(self.centralwidget)
        self.button_yb70.setGeometry(QtCore.QRect(883, 440, 48, 48))
        self.button_yb70.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_yb70.setStyleSheet("background-image: url(C:/img/w4_yb70.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_yb70.clicked.connect(lambda: Window4.fnc_yb70(self))

        self.button_er68 = QtWidgets.QPushButton(self.centralwidget)
        self.button_er68.setGeometry(QtCore.QRect(783, 440, 48, 48))
        self.button_er68.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_er68.setStyleSheet("background-image: url(C:/img/w4_er68.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_er68.clicked.connect(lambda: Window4.fnc_er68(self))
        
        self.button_ho67 = QtWidgets.QPushButton(self.centralwidget)
        self.button_ho67.setGeometry(QtCore.QRect(732, 440, 48, 48))
        self.button_ho67.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_ho67.setStyleSheet("background-image: url(C:/img/w4_ho67.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_ho67.clicked.connect(lambda: Window4.fnc_ho67(self))

        self.button_tb65 = QtWidgets.QPushButton(self.centralwidget)
        self.button_tb65.setGeometry(QtCore.QRect(630, 440, 48, 48))
        self.button_tb65.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_tb65.setStyleSheet("background-image: url(C:/img/w4_tb65.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_tb65.clicked.connect(lambda: Window4.fnc_tb65(self))

        self.button_eu63 = QtWidgets.QPushButton(self.centralwidget)
        self.button_eu63.setGeometry(QtCore.QRect(529, 440, 48, 48))
        self.button_eu63.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_eu63.setStyleSheet("background-image: url(C:/img/w4_eu63.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_eu63.clicked.connect(lambda: Window4.fnc_eu63(self))

        self.button_am95 = QtWidgets.QPushButton(self.centralwidget)
        self.button_am95.setGeometry(QtCore.QRect(529, 490, 48, 48))
        self.button_am95.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_am95.setStyleSheet("background-image: url(C:/img/w4_am95.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_am95.clicked.connect(lambda: Window4.fnc_am95(self))

        self.button_bk97 = QtWidgets.QPushButton(self.centralwidget)
        self.button_bk97.setGeometry(QtCore.QRect(630, 490, 48, 48))
        self.button_bk97.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_bk97.setStyleSheet("background-image: url(C:/img/w4_bk97.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_bk97.clicked.connect(lambda: Window4.fnc_bk97(self))

        self.button_cf98 = QtWidgets.QPushButton(self.centralwidget)
        self.button_cf98.setGeometry(QtCore.QRect(680, 490, 48, 48))
        self.button_cf98.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_cf98.setStyleSheet("background-image: url(C:/img/w4_cf98.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_cf98.clicked.connect(lambda: Window4.fnc_cf98(self))
        
        self.button_db105 = QtWidgets.QPushButton(self.centralwidget)
        self.button_db105.setGeometry(QtCore.QRect(275, 365, 48, 48))
        self.button_db105.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_db105.setStyleSheet("background-image: url(C:/img/w4_db105.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_db105.clicked.connect(lambda: Window4.fnc_db105(self))

        self.button_hs108 = QtWidgets.QPushButton(self.centralwidget)
        self.button_hs108.setGeometry(QtCore.QRect(425, 365, 48, 48))
        self.button_hs108.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_hs108.setStyleSheet("background-image: url(C:/img/w4_hs108.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_hs108.clicked.connect(lambda: Window4.fnc_hs108(self))

        self.button_ds110 = QtWidgets.QPushButton(self.centralwidget)
        self.button_ds110.setGeometry(QtCore.QRect(527, 365, 48, 48))
        self.button_ds110.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_ds110.setStyleSheet("background-image: url(C:/img/w4_ds110.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_ds110.clicked.connect(lambda: Window4.fnc_ds110(self))

        self.button_lv116 = QtWidgets.QPushButton(self.centralwidget)
        self.button_lv116.setGeometry(QtCore.QRect(833, 365, 48, 48))
        self.button_lv116.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_lv116.setStyleSheet("background-image: url(C:/img/w4_lv116.jpg);"
                                      "background-color: rgb(255, 0, 0)")
        self.button_lv116.clicked.connect(lambda: Window4.fnc_lv116(self))

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(845, 555, 150, 25))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Выйти")
        self.pushButton_3.clicked.connect(lambda: self.hide())

    
    def fnc_be4(self):
        self.newindow = Window_be4(self)
        self.newindow.setWindowTitle("Бериллий")
        Window_be4.main(self.newindow)
        self.newindow.show()
    def fnc_sc21(self):
        self.newindow = Window_sc21(self)
        self.newindow.setWindowTitle("Скандий")
        Window_sc21.main(self.newindow)
        self.newindow.show()
    def fnc_ga31(self):
        self.newindow = Window_ga31(self)
        self.newindow.setWindowTitle("Галлий")
        Window_ga31.main(self.newindow)
        self.newindow.show()
    def fnc_sr38(self):
        self.newindow = Window_sr38(self)
        self.newindow.setWindowTitle("Стронций")
        Window_sr38.main(self.newindow)
        self.newindow.show()
    def fnc_y39(self):
        self.newindow = Window_y39(self)
        self.newindow.setWindowTitle("Иттрий")
        Window_y39.main(self.newindow)
        self.newindow.show()
    def fnc_ru44(self):
        self.newindow = Window_ru44(self)
        self.newindow.setWindowTitle("Рутений")
        Window_ru44.main(self.newindow)
        self.newindow.show()
    def fnc_hf72(self):
        self.newindow = Window_hf72(self)
        self.newindow.setWindowTitle("Гафний")
        Window_hf72.main(self.newindow)
        self.newindow.show()
    def fnc_re75(self):
        self.newindow = Window_re75(self)
        self.newindow.setWindowTitle("Рений")
        Window_re75.main(self.newindow)
        self.newindow.show()
    def fnc_fr87(self):
        self.newindow = Window_fr87(self)
        self.newindow.setWindowTitle("Франций")
        Window_fr87.main(self.newindow)
        self.newindow.show()
    def fnc_lu71(self):
        self.newindow = Window_lu71(self)
        self.newindow.setWindowTitle("Лютеций")
        Window_lu71.main(self.newindow)
        self.newindow.show()
    def fnc_yb70(self):
        self.newindow = Window_yb70(self)
        self.newindow.setWindowTitle("Иттербий")
        Window_yb70.main(self.newindow)
        self.newindow.show()
    def fnc_er68(self):
        self.newindow = Window_er68(self)
        self.newindow.setWindowTitle("Эрбий")
        Window_er68.main(self.newindow)
        self.newindow.show()
    def fnc_ho67(self):
        self.newindow = Window_ho67(self)
        self.newindow.setWindowTitle("Гольмий")
        Window_ho67.main(self.newindow)
        self.newindow.show()
    def fnc_tb65(self):
        self.newindow = Window_tb65(self)
        self.newindow.setWindowTitle("Тербий")
        Window_tb65.main(self.newindow)
        self.newindow.show()
    def fnc_eu63(self):
        self.newindow = Window_eu63(self)
        self.newindow.setWindowTitle("Европий")
        Window_eu63.main(self.newindow)
        self.newindow.show()
    def fnc_am95(self):
        self.newindow = Window_am95(self)
        self.newindow.setWindowTitle("Америций")
        Window_am95.main(self.newindow)
        self.newindow.show()
    def fnc_bk97(self):
        self.newindow = Window_bk97(self)
        self.newindow.setWindowTitle("Берклий")
        Window_bk97.main(self.newindow)
        self.newindow.show()
    def fnc_cf98(self):
        self.newindow = Window_cf98(self)
        self.newindow.setWindowTitle("Калифорний")
        Window_cf98.main(self.newindow)
        self.newindow.show()
    def fnc_db105(self):
        self.newindow = Window_db105(self)
        self.newindow.setWindowTitle("Дубний")
        Window_db105.main(self.newindow)
        self.newindow.show()
    def fnc_hs108(self):
        self.newindow = Window_hs108(self)
        self.newindow.setWindowTitle("Хассий")
        Window_hs108.main(self.newindow)
        self.newindow.show()
    def fnc_ds110(self):
        self.newindow = Window_ds110(self)
        self.newindow.setWindowTitle("Дармштадий")
        Window_ds110.main(self.newindow)
        self.newindow.show()
    def fnc_lv116(self):
        self.newindow = Window_lv116(self)
        self.newindow.setWindowTitle("Ливермоний")
        Window_lv116.main(self.newindow)
        self.newindow.show()
#made
        

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.resize(1000, 600)
        self.setWindowTitle("Химия")  
        self.setFixedSize(1000, 600)
        self.setObjectName("self")
        self.setStyleSheet("background-image: url(C:/img/для_химии.jpg) \n")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = 0
        self.label_1 = 0
        
        self.setWindowIcon(QtGui.QIcon("C:/img/лого_школы.png"))
        
        
        
        
        self.image = Image.open("C:/img/лого_слева.png")
        width, height = self.image.size
        w = int(width/4)
        h = int(height/4)
        self.resized_image = self.image.resize((w, h))       
        self.resized_image.save("C:/img/лого_школы_resized.png")      
        MyDefs.make_pict(self, self.label, self.centralwidget, int((1000 - w)/2), 0, w, h,  "C:/img/лого_школы_resized.png")


        MyDefs.make_nice_text(self, self.label_1, "Добро пожаловать, дорогие ученики!", 0, 115+10, 1000, 40)
        MyDefs.make_nice_text(self, self.label_1, 'Проект на тему: "География химических элементов"', 0, 100 + 115, 1000, 40)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 330, 400, 200))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-image: url(C:/img/1_okno_knopka.jpg);"
                                        "background-color: rgb(255, 0, 0)")  
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_3.clicked.connect(self.btn_clk1)   
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(795, 550, 200, 50))
        self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0); \n"
                                        "color: rgb(255, 0, 0); \n"
                                        "font-weight: bold; \n"
                                        "font-family: Segoe Print;"
                                        "font-size: 14px")
        self.pushButton_2.setObjectName("pushButton_3")
        self.pushButton_2.setText("Пропустить")
        self.pushButton_2.clicked.connect(self.btn_clk3)

        
        

 
         
    def btn_clk3(self):
        self.newindow = Start_Window(self)
        self.newindow.setWindowTitle("Биография Дмитрия Ивановича Менделеева")
        Start_Window.main(self.newindow)
        self.hide()
        self.newindow.show() 
       
    def btn_clk1(self): 
        os.startfile("C:/img/Trees - 111973.mp4")
# вставить видео с варей         
       
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a_window = Window()
    a_window.show()
    sys.exit(app.exec_())
  