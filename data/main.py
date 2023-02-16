from PyQt6.QtWidgets import QMainWindow,QLabel,QPushButton,QApplication
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon,QPixmap,QFont
from data import get_weather
class MainWeather(QMainWindow):
    def __init__(self, width = 500, height = 500, title = "Wather APP") -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(500,250,width,height)
        icon_title = QIcon("image//asosiy.png")
        far_icon = QIcon("image//far.png")
        tosh_icon = QIcon("image//tosh.png")
        and_icon = QIcon("image//and.png")
        nam_icon = QIcon("image//nam.png")
        calc_icon = QPixmap("image//therm.png").scaled(QtCore.QSize(35,35))
        update_icon = QIcon("image//update.png")
        send_icon = QIcon("image//share.png")
        quit_icon = QIcon("image//shutdown.png")
        self.setWindowIcon(icon_title)
        
        self.fbutton = QPushButton(far_icon, " Farg'ona",self)
        self.fbutton.setGeometry(20, 20, 150, 40)
        self.fbutton.adjustSize()
        self.fbutton.setStyleSheet('background-color:#B79D3A;color:black;border-radius:10px;')

        self.tbutton = QPushButton(tosh_icon, " Toshkent",self)
        self.tbutton.setGeometry(130, 20, 150, 40)
        self.tbutton.adjustSize()
        self.tbutton.setStyleSheet('background-color:#B79D3A;color:black;border-radius:10px;')

        self.abutton = QPushButton(and_icon, " Andijon",self)
        self.abutton.setGeometry(250, 20, 150, 40)
        self.abutton.adjustSize()
        self.abutton.setStyleSheet('background-color:#B79D3A;color:black;border-radius:10px;')

        self.nbutton = QPushButton(nam_icon, " Namangan",self)
        self.nbutton.setGeometry(370, 20, 150, 40)
        self.nbutton.adjustSize()
        self.nbutton.setStyleSheet('background-color:#B79D3A;color:black;border-radius:10px;')

        self.temp_img=QLabel(self)
        self.temp_img.setPixmap(calc_icon)
        self.temp_img.setGeometry(185,200,35,35)

        self.update_weath = QPushButton(update_icon, "Update", self)
        self.update_weath.setGeometry(20,400,150,40)
        self.update_weath.adjustSize()
        self.update_weath.setStyleSheet("background-color:#B79D3A;color:black;border-radius:10px;")
        #self.update_weath.clicked.connect(self,)

        self.send_bot = QPushButton(send_icon, "Send", self)
        self.send_bot.setGeometry(140,400,150,40)
        self.send_bot.adjustSize()
        self.send_bot.setStyleSheet("background-color:#B79D3A;color:black;border-radius:10px;")

        self.quit = QPushButton(quit_icon, "Quit", self)
        self.quit.setGeometry(260, 400, 150, 40)
        self.quit.adjustSize()
        self.quit.setStyleSheet("background-color:#B79D3A;color:black;border-radius:10px;")
        self.quit.clicked.connect(QApplication.quit)


        self.temp = QLabel("Harorat: ",self)
        self.temp.setFont(QFont('Arial', 16))
        self.temp.setGeometry(25,200,150,50)

        self.holat = QLabel("Ob Havo Holati: ",self)
        self.holat.setFont(QFont("Arial",16))
        self.holat.setGeometry(25,140,150,50)
        
        self.shamol = QLabel("Shamol: ",self)
        self.shamol.setFont(QFont("Arial",16))
        self.shamol.setGeometry(25,260,150,50)

        self.fbutton.clicked.connect(self.far_temp)
        self.tbutton.clicked.connect(self.tosh_temp)
        self.abutton.clicked.connect(self.and_temp)
        self.nbutton.clicked.connect(self.nam_temp)
        
        
        # style = """
        # background: no-repeat center url('image/wea_im.jpg');
        # """
        # self.setStyleSheet(style)
    def far_temp(self):
        temp = get_weather.get_weather(city="фергана")
        self.temp.setText("Harorat "+ temp)
    def tosh_temp(self):
        temp = get_weather.get_weather(city="ташкент")
        self.temp.setText("Harorat "+ temp)
    def and_temp(self):
        temp = get_weather.get_weather(city="андижан")
        self.temp.setText("Harorat "+ temp)
    def nam_temp(self):
        temp = get_weather.get_weather(city="наманган")
        self.temp.setText("Harorat "+ temp)
    # def far_holat(self):
    #     holat = get_weather.get_holat(city="фергана")
    #     self.holat.setText("Ob Havo Holati: "+holat)
