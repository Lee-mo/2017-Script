from PyQt4.QtGui import *
import sys
# MyDiag.py 모듈 import
import MyDiag_gmail
from urllib import request
import urllib.parse
from xml.dom.minidom import *
from xml.etree import ElementTree

#sendMail 모듈
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

ServiceKey = 'ServiceKey=1td22cJml3Qk4BuSNgwhWXUk2xtS8zrLx0n0OfwQHdcn5HvvOvAv9UOJ6qSztOTbtrI5ODfdxzXhgvC5NJWxvQ%3D%3D'
# MyDiag 모듈 안의 Ui_MyDialog 클래스로부터 파생

class XDialog(QDialog, MyDiag_gmail.Ui_Form):
    def __init__(self):
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.sendMail)
        self.pushButton_5.clicked.connect(self.editName)
        self.pushButton.clicked.connect(self.savePharmacy)
        self.pushButton_2.clicked.connect(self.searchNearby)


    def sendMail(self):

        # global
        host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
        port = "587"
        htmlFileName = "logo.html"

        senderAddr = self.lineEdit_3.text()  # 보내는 사람 email 주소.
        senderPw = self.lineEdit_4.text()
        recipientAddr = self.lineEdit_5.text()  # 받는 사람 email 주소.

        #선택된 약국 정보
        item = self.listWidget.currentItem()
        value = item.text()
        #msgtext = str(input('write message :'))

        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = "Test email(Pharmacy Manager) in Python 3.0"
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        # MIME 문서를 생성합니다.
        htmlFD = open(htmlFileName, 'rb')
        HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
        htmlFD.close()

        body = ("This is a test sending email through python")
        print(type(body))
        bodyPart = MIMEText(body.encode('utf-8'), 'plain', 'UTF-8')

        msgPharmacy = MIMEText(value.encode('utf-8'),_charset='UTF-8')
        #msgPart=MIMEText(msgtext,('plain'))

        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        #msg.attach(HtmlPart)

        #msg.attach(msgPart)
        msg.attach(bodyPart)
        msg.attach(msgPharmacy)

        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host, port)
        # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr, senderPw)
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()
        print("Mail sending complete!!!")

    def editName(self):
        self.listWidget.clear()
        global sidoName, sigunguName, day, order, pharmacyName
        sidoNameKor = self.lineEdit.text()
        sidoName = urllib.parse.quote(sidoNameKor)
        print(sidoNameKor)

        sigunguNameKor = self.lineEdit_2.text()
        sigunguName = urllib.parse.quote(sigunguNameKor)
        print(sigunguNameKor)

        dayKor = self.comboBox.currentText()
        if (dayKor == "월"):
            dayKor = "1"
        elif (dayKor == "화"):
            dayKor = "2"
        elif (dayKor == "수"):
            dayKor = "3"
        elif (dayKor == "목"):
            dayKor = "4"
        elif (dayKor == "금"):
            dayKor = "5"
        elif (dayKor == "토"):
            dayKor = "6"
        elif (dayKor == "일"):
            dayKor = "7"
        elif (dayKor == "공휴일"):
            dayKor = "8"
        day = urllib.parse.quote(dayKor)
        print(dayKor)

        response_body = request.urlopen(
            'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
            + ServiceKey +
            '&Q0=' + sidoName + '&Q1=' + sigunguName + '&QT=' + day + '&pageNo=1&numOfRows=20').read()
        tree = ElementTree.fromstring(response_body)
        itemElements = tree.getiterator("item")
        for item in itemElements:
            dutyName = item.find("dutyName")
            dutyAddr = item.find("dutyAddr")
            dutyTimeS = item.find("dutyTime" + day + "s")
            dutyTimeC = item.find("dutyTime" + day + "c")
            self.listWidget.addItem( dutyName.text +'\n'+
                                         dutyAddr.text)

    def savePharmacy(self):
        global value, line
        item = self.listWidget.currentItem()
        value = item.text()
        line = value.splitlines()


    def searchNearby(self):
        self.listWidget.clear()
        global line, sidoName, sigunguName, day, order, pharmacyName
        pharmacyName = line[0]
        pharmacyName1 = pharmacyName
        pharmacyName = urllib.parse.quote(pharmacyName)

        response_body = request.urlopen(
            'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
            + ServiceKey +
            '&Q0=' + sidoName + '&Q1=' + sigunguName + '&ORD=ADDR&numOfRows=500').read()
        tree = ElementTree.fromstring(response_body)
        itemElements = tree.getiterator("item")
        count = 0
        bool = False
        for item in itemElements:
            if (pharmacyName1 == item.findtext("dutyName")):
                bool = True
            if (bool == 1 and pharmacyName1 != item.findtext("dutyName")):
                for item in itemElements:
                    dutyName = item.find("dutyName")
                    dutyAddr = item.find("dutyAddr")
                    self.listWidget.addItem(dutyName.text + '\n' +
                                            dutyAddr.text)
                count += 1
            if (count > 10):
                bool = False
                break



app = QApplication(sys.argv)
dlg = XDialog()
dlg.show()
app.exec_()