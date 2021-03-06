import sys

# sys.path.append("D:\source\CloudStation\AAT")

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import datetime
from kiwoom import *
import os
import requests
from bs4 import BeautifulSoup
from trading import *
from start_point import *
from log import *

form_class = uic.loadUiType("main.ui")[0]
# form_c.loadUiType("start.ui")[0]
SECU_BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),"security_file")

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.start = Start(self)
        self.log = Log(self)
        # start.move(885, 520)
        # start.resize(650, 450)

        self.tabWidget.addTab(self.start, "start")
        self.tabWidget.addTab(self.log, "log")

        self.start.pushButton_2.clicked.connect(self.button_clicked)

        self.start.pushButton_4.clicked.connect(self.button2)
        # self.menu_log.triggered.connect(self.log)

        if self.start.login_state == True:
            pass
        # 탭 컨트롤 성공 / 탭을 가져옴
        # self.table_widget = Start(self)
        # self.setCentralWidget(self.table_widget)


    def button2(self):
        try:
            self.trading.lineEdit.setText("01")
            print("button")
        except:
            pass

    def button_clicked(self):
        self.trading = Trading(self, self.start.kiwoom)
        self.tabWidget.addTab(self.trading, "수동 매매")

        # trading.checkBox_2.setEnabled(True)

    # def log(self):

# class Start(QWidget, form_class1):
#     def __init__(self, parent):
#         super(QWidget, self).__init__(parent)
#         self.setupUi(self)
#         self.non_login_state = True
#         self.kiwoom = Kiwoom()
#
#         self.holidays = self.open_api_holiday()
#
#         self.timer = QTimer(self)
#         self.timer.start(1000)
#         self.timer.timeout.connect(self.display_time)
#
#         self.pushButton_2.clicked.connect(self.button_clicked)
#
#         # self.auto_trading_action.triggered.connect(lambda: self.show_sub_windows(self.auto_trading_action.text()))
#         # self.manual_trading_action.triggered.connect(lambda: self.show_sub_windows(self.manual_trading_action.text()))
#
#
#     def show_sub_windows(self, action):
#         if action == self.auto_trading_action.text():
#             pass
#             # self.auto_trading = AutoTrading()
#             # self.auto_trading.show()
#         elif action == self.manual_trading_action.text():
#             # self.manual_trading = ManualTrading(self.state)
#             self.manual_trading = ManualTrading(self.kiwoom, self.state)
#             self.manual_trading.show()
#
#         # if self.action.isCheckable():
#         #     print("A")
#         # elif self.action_2.isChecked():
#         #     print("B")
#         # print(self.action.isEnabled())
#         # print(self.action_2.isEnabled())
#
#     def display_time(self):
#         today_time = datetime.datetime.today().strftime('%Y-%m-%d / %p.%H:%M:%S')
#
#         self.label.setText(today_time)
#
#         week = int(datetime.datetime.today().strftime('%w'))
#         day = int(datetime.datetime.today().strftime('%d'))
#         hour = datetime.datetime.today().strftime('%H')
#         min = datetime.datetime.today().strftime('%M')
#
#         hour_P_min = hour + min
#
#         if week == 6 or week == 0:
#             self.label_2.setText("주말 입니다.")
#             self._open_close(False)
#         elif int(hour) < 9 or (int(hour_P_min) > 1530):    # 9 - 15:30 # 일단 이렇게 보류 / 더 나은 방법 찾아보기
#             self.label_2.setText("개장 시간이 아닙니다.")
#             self._open_close(False)
#         elif day in self.holidays:
#             self.label_2.setText("휴무일 입니다.")
#             self._open_close(False)
#         else:
#             self.label_2.setText("장 오픈 !")
#             self._open_close(True)
#
#         self.connect_state()
#
#         if int(hour) == 8 and int(min) == 50 and self.non_login_state:
#             self.button_clicked()
#             self.non_login_state = False
#
#     """
#     공공 데이터로 공휴일 처리
#     개장 폐장은 하루 한번만 확인해도 됨
#     프로그램 실행 때 딱 한번만 확인
#     """
#     def open_api_holiday(self):
#         holi_api = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/"
#         operation = "getHoliDeInfo"
#         year = "?solYear=" + datetime.datetime.today().strftime('%Y')
#         month = "&solMonth=" + datetime.datetime.today().strftime('%m')
#         # month = "&solMonth=04"
#         service_key = self.open_file()
#         service_key = "&ServiceKey="+service_key
#
#         url = holi_api+operation+year+month+service_key
#
#         holiday_req = requests.get(url=url)
#         holiday_xml = holiday_req.text
#
#         soup = BeautifulSoup(holiday_xml, "xml")
#         holidays = soup.find_all("locdate")
#
#         holiday_day = []
#
#         for holiday in holidays:
#             holiday_slice = holiday.text
#             holiday_slice = holiday_slice[6:8]
#             holiday_day.append(holiday_slice)
#         print("open_api_hoilday")
#         return holiday_day
#
#     def open_file(self):
#         with open(os.path.join(SECU_BASE_DIR, "key.txt"),'r+', encoding='utf-8') as f_read:
#             service_key = f_read.readline()
#         return service_key
#
#     def _open_close(self, door):
#         if door == True:
#             self.radioButton.setChecked(True)
#             self.radioButton.setStyleSheet("Color : Blue")
#             self.label.setStyleSheet("Color : Blue")
#
#             self.radioButton_2.setStyleSheet("Color : Black")
#         elif door == False:
#             self.radioButton_2.setChecked(True)
#             self.radioButton_2.setStyleSheet("Color : Red")
#
#             self.radioButton.setStyleSheet("Color : Black")
#             self.label.setStyleSheet("Color : Black")
#         else:
#             pass
#
#     def connect_state(self):
#         self.state = self.kiwoom.get_connect_state()
#
#         if self.state == 1:
#             self.label_3.setText("서버 연결 상태 😁")
#             self.label_3.setStyleSheet("Color : Blue")
#         elif self.state == 0:
#             self.label_3.setText("서버 미연결 상태 😅")
#             self.label_3.setStyleSheet("Color : Black")
#
#     def button_clicked(self):
#         self.kiwoom.comm_connect()
#         self.manual_trading_action.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
    app = None