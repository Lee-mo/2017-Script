from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import sys
import gui
import detailPopup
import datetime
from mail import *
from map import *
import search
from urllib import request
import urllib.parse
from xml.dom.minidom import *
from xml.etree import ElementTree

import folium
from urllib import request, parse
from xml.etree import ElementTree
import webbrowser
global x, y

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = "587"
pgNm = 1
url_home = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/'
serviceKey = 'serviceKey=OyfS4qqxnYyHXNdGgHg%2Bem2F%2FLAjaG4C0X2kgqycc%2B2G3%2F0flCjg9GIptnv23C3UXWRH3wjd3EuE31%2FGSX71ZA%3D%3D'
url_sido = url_home + "sido?" + serviceKey
url_dog = url_home + "kind?" + serviceKey + "&up_kind_cd=417000"

class DetailPopupDialog(QDialog, detailPopup.Ui_Dialog):
    def __init__(self,item):
        global first
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)
        self.InitDraw(item)

        self.MapPushButton.clicked.connect(self.pushAction)
        self.sendMailPushButton.clicked.connect(self.pushActionMail)



    def pushAction(self,item):
        global loc
        self.MapPushButton.clicked.connect(self.show_map(loc))

    def pushActionMail(self,item):
        global mailData
        self.sendMailPushButton.clicked.connect(self.sendMail(mailData))

    def sendMail(self, data):
        global host, port
        senderAddr = "eomdyeon@gmail.com"
        passwd = "qaz24534**google"  # 비밀번호

        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')

        recipientAddr = self.sendMailLineEdit.text()
        title = '[유기동물정보] ' + nowDate

        msg = MIMEMultipart('alternative')

        msg['Subject'] = title
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        msgPart = MIMEText(data, 'plain')
        msg.attach(msgPart)

        print("서버 연결중 ... ")
        s = smtplib.SMTP(host, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr, passwd)  # 로긴을 합니다.
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()

        print("메일 보내기 성공!")

    def InitDraw(self, item):
        global desertionNo, loc, mailData

        processState = item.find("processState")
        kindCd = item.find("kindCd")
        age = item.find("age")
        sexCd = item.find("sexCd")
        colorCd = item.find("colorCd")
        neuterYn = item.find("neuterYn")
        specialMark = item.find("specialMark")
        weight = item.find("weight")
        happenPlace = item.find("happenPlace")
        photo = item.find("popfile")
        happenDt = item.find("happenDt")
        careNm = item.find("careNm")
        careAddr = item.find("careAddr")
        careTel = item.find("careTel")
        chargeNm = item.find("chargeNm")
        officetel = item.find("officetel")
        orgNm = item.find("orgNm")
        noticeNo = item.find("noticeNo")
        dNo = item.find("desertionNo")

        self.noticeNoLabel.setText("공고번호: "+ noticeNo.text)
        self.desertionNoLabel.setText("유기번호: " + dNo.text)
        self.label_17.setText("접수일: " + happenDt.text)
        self.happenPlaceLabel.setText("발견장소: " + happenPlace.text)
        self.careNmLabel.setText("보호소 이름: " + careNm.text)
        self.careAddrLabel.setText("보호주소: " + careAddr.text)
        self.careTelLabel.setText("보호소 전화번호: " + careTel.text)
        self.chargeNameLabel.setText("담당자: " + chargeNm.text)
        self.officetelLabel.setText("담당자 연락처: " + officetel.text)
        self.orgNmLabel.setText("관할기관: " + orgNm.text)
        self.KindCdLabel.setText("품종: " + kindCd.text)
        self.neuterYnLabel.setText("중성화 여부: " + neuterYn.text)
        self.ageLabel.setText("나이 : " + age.text)
        self.sexCdLabel.setText("성별 : " + sexCd.text)
        self.colorCdLabel.setText("색상: " + colorCd.text)
        self.label_8.setText("체중: " + weight.text)
        self.specialMarkLabel.setText("특징: " + specialMark.text)
        self.webView.setUrl(QtCore.QUrl(photo.text))
        print(specialMark.text)

        mailData = "-----동물정보-----" + "\n상태: " + processState.text + "\n품종: " + kindCd.text + "\n나이: " + \
                   age.text + "\n성별: " + sexCd.text + "\n색상: " + colorCd.text + "\n중성화 여부: " + neuterYn.text + \
                   "\n특징: " + specialMark.text + "\n체중: " + weight.text + "\n발견장소: " + happenPlace.text \
                   + "\n사진: " + photo.text + "\n-----보호 정보-----" + "\n접수일: " + happenDt.text + "\n보호소 이름: " + \
                   careNm.text + "\n보호 주소: " + careAddr.text + "\n보호소 전화번호: " + careTel.text + "\n담당자: " + \
                   chargeNm.text + "\n담당자 연락처: " + officetel.text + "\n관할기관: " + orgNm.text + "\n공고번호: " + \
                   noticeNo.text + "\n유기번호: " + dNo.text

        loc = careAddr.text

    def show_map(self,loc):
        global x, y
        address = parse.quote(loc)
        url = "http://api.vworld.kr/req/address?service=address&version=2.0&request=getcoord&key=483E0418-2F46-3223-80A1-F66D16A24685&format=xml&type=road&address="+str(address)+"&refine=true&simple=false&crs=epsg:4326"
        res = request.urlopen(url).read()
        tree = ElementTree.fromstring(res)
        itemElements = tree.getiterator("point")
        for item in itemElements:
            x = item.find('x')
            y = item.find('y')

        # 위도 경도 지정
        map_osm = folium.Map(location=[y.text, x.text], zoom_start=13)
        # 마커 지정
        folium.Marker([y.text, x.text], popup='Mt. Hood Meadows').add_to(map_osm)
        # html 파일로 저장
        map_osm.save('osm.html')

        # 지도 열기
        webbrowser.open('osm.html')


class XDialog(QDialog, gui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)
        self.SearchPushButton.clicked.connect(self.seletMenu)
        self.detailPushButton.clicked.connect(self.InitDetailPopup)
        self.NextPagePushButton.clicked.connect(self.seletNext)

    def InitDetailPopup(self):
        global dlg2, desertionNo
        self.getDesertionNo(self.listWidget.currentItem())
        item = self.searchDesertionNo()
        dlg2 = DetailPopupDialog(item)
        dlg2.show()

    def seletMenu(self):
        sel = self.selectMenuComboBox.currentText()
        if(sel == "보호소 찾기"):
            self.searchShelter()
        else:
            self.searchAnimal()

    def seletNext(self):
        global pgNm
        sel = self.selectMenuComboBox.currentText()
        if(sel == "보호소 찾기"):
            pass
        else:
            pgNm += 1
            print(pgNm)
            self.searchAnimal()

    def printItem(self, url, item_name):
        response = request.urlopen(url).read()
        tree = ElementTree.fromstring(response)
        itemElements = tree.getiterator("item")
        for item in itemElements:
            name = item.find(item_name)
            self.listWidget.addItem(name.text)

    def getDesertionNo(self,item):
        global desertionNo
        value = item.text()
        desertionNo = value[6:21]

    def searchDesertionNo(self):
        global sido_code, sigungu_code, desertionNo, kind_code, animal_code, bgn_date, end_date

        url_searchAbandonment = \
            url_home + 'abandonmentPublic?' + serviceKey + '&bgnde=' + bgn_date + '&endde=' + end_date \
            + animal_code + kind_code + '&org_cd=' + sigungu_code+ '&pageNo=' +  str(pgNm) + '&numOfRows=50'
        response = request.urlopen(url_searchAbandonment).read()
        tree = ElementTree.fromstring(response)
        itemElements = tree.getiterator("item")

        print(desertionNo)

        for item in itemElements:
            num = item.find("desertionNo")
            if (num.text == desertionNo):
                print("찾음")
                print(num.text)
                return item


    def getRegionCode(self, url, search_name):
        response = request.urlopen(url).read()
        tree = ElementTree.fromstring(response)
        itemElements = tree.getiterator("item")
        for item in itemElements:
            name = item.find('orgdownNm')
            name = name.text
            if name == search_name:
                result = item.find("orgCd")
                return result.text

    def getDogKindCode(self, search_name):
        response = request.urlopen(url_dog).read()
        tree = ElementTree.fromstring(response)
        itemElements = tree.getiterator("item")
        for item in itemElements:
            name = item.find('KNm')
            name = name.text
            if name == search_name:
                result = item.find("kindCd")
                return str(result.text)

    def searchShelter(self):
        global sido_code, sigungu_code
        self.listWidget.clear()
        # 시/도 코드 찾기
        sido_name = self.sidoLineEdit.text()
        sido_code = self.getRegionCode(url_sido, sido_name)

        # 시/군/구 코드 찾기
        sigungu_name = self.sigunguLineEdit.text()
        url_sigungu = url_home + 'sigungu?' + serviceKey + '&upr_cd=' + sido_code
        sigungu_code = self.getRegionCode(url_sigungu, sigungu_name)

        # 보호소 찾기
        url_shelter = url_home + 'shelter?' + serviceKey + '&upr_cd=' + sido_code + '&org_cd=' + sigungu_code
        # 보호소 출력
        self.printItem(url_shelter, "careNm")

    def searchAnimal(self):
        global bgn_date, end_date, mailData, sido_code, sigungu_code, animal_kind, animal_code, kind_code
        self.listWidget.clear()

        # 시/도 조건
        sido_name = self.sidoLineEdit.text()
        sido_code = self.getRegionCode(url_sido, sido_name)

        # 시/군/구 조건
        sigungu_name = self.sigunguLineEdit.text()
        url_sigungu = url_home + 'sigungu?' + serviceKey + '&upr_cd=' + sido_code
        sigungu_code = self.getRegionCode(url_sigungu, sigungu_name)


        tmpS = self.startDateEdit.textFromDateTime (self.startDateEdit.dateTime())
        tmpE = self.startDateEdit.textFromDateTime(self.endDateEdit.dateTime())
        tmpS = tmpS.split('-')
        tmpE = tmpE.split('-')
        dateS = tmpS[0] + tmpS [1] + tmpS[2]
        dateE = tmpE[0] + tmpE[1] + tmpE[2]
        bgn_date = dateS
        end_date = dateE


        # 축종 조건
        if(self.radioButtonDog.isChecked() == True):
            animal_kind = '1'
        elif(self.radioButtonCat.isChecked() == True):
            animal_kind = '2'
        elif (self.radioButtonEtc.isChecked() == True):
            animal_kind = '3'
        else:
            animal_kind = '4'

        print(animal_kind)
        if animal_kind == '1':  # 개 품종 조건
            animal_code = "&upkind=417000"
            kind_code = ""
        elif animal_kind == '2':  # 고양이
            animal_code = "&upkind=422400"
            kind_code = ""
        elif animal_kind == '3':  # 기타
            animal_code = "&upkind=429900"
            kind_code = ""
        elif animal_kind == '4':  # 상관없음
            animal_code = ""
            kind_code = ""

      #  self.label_3.setText("변경")
        url_searchAbandonment = \
            url_home + 'abandonmentPublic?' + serviceKey + '&bgnde=' + bgn_date + '&endde=' + end_date \
            + animal_code + kind_code + '&org_cd=' + sigungu_code+ '&pageNo=' + str(pgNm) + '&numOfRows=50'
        response = request.urlopen(url_searchAbandonment).read()
        tree = ElementTree.fromstring(response)
        itemElements = tree.getiterator("item")

        for item in itemElements:
            self.printAnimal(item)



    def printAnimal(self,item):
        global mailData, loc
        processState = item.find("processState")
        kindCd = item.find("kindCd")
        age = item.find("age")
        sexCd = item.find("sexCd")
        colorCd = item.find("colorCd")
        neuterYn = item.find("neuterYn")
        specialMark = item.find("specialMark")
        weight = item.find("weight")
        happenPlace = item.find("happenPlace")
        photo = item.find("popfile")
        # -----보호 정보-----
        happenDt = item.find("happenDt")
        careNm = item.find("careNm")
        careAddr = item.find("careAddr")
        careTel = item.find("careTel")
        chargeNm = item.find("chargeNm")
        officetel = item.find("officetel")
        orgNm = item.find("orgNm")
        noticeNo = item.find("noticeNo")
        desertionNo = item.find("desertionNo")
        self.listWidget.addItem("유기번호 [" + desertionNo.text + "]\n" + "접수일: " + happenDt.text + "\n" + "상태: " + processState.text + "\n" + "품종: " + kindCd.text + "\n" +"발견장소: " + happenPlace.text + "\n" )



        mailData = "-----동물정보-----" + "\n상태: " + processState.text + "\n품종: " + kindCd.text + "\n나이: " + \
                   age.text + "\n성별: " + sexCd.text + "\n색상: " + colorCd.text + "\n중성화 여부: " + neuterYn.text + \
                   "\n특징: " + specialMark.text + "\n체중: " + weight.text + "\n발견장소: " + happenPlace.text \
                   + "\n사진: " + photo.text + "\n-----보호 정보-----" + "\n접수일: " + happenDt.text + "\n보호소 이름: " + \
                   careNm.text + "\n보호 주소: " + careAddr.text + "\n보호소 전화번호: " + careTel.text + "\n담당자: " + \
                   chargeNm.text + "\n담당자 연락처: " + officetel.text + "\n관할기관: " + orgNm.text + "\n공고번호: " + \
                   noticeNo.text + "\n유기번호: " + desertionNo.text

        loc = careAddr.text











app = QApplication(sys.argv)
dlg = XDialog()
dlg.show()


app.exec_()