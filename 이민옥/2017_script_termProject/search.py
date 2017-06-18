from urllib import request
from xml.etree import ElementTree
from mail import *
from map import *

url_home = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/'
serviceKey = 'serviceKey=OyfS4qqxnYyHXNdGgHg%2Bem2F%2FLAjaG4C0X2kgqycc%2B2G3%2F0flCjg9GIptnv23C3UXWRH3wjd3EuE31%2FGSX71ZA%3D%3D'
url_sido = url_home + "sido?" + serviceKey
url_dog = url_home + "kind?" + serviceKey + "&up_kind_cd=417000"

def searchShelter():
    global sido_code, sigungu_code


    # 시/도 코드 찾기
    sido_name = input("시/도를 입력하세요: ")
    sido_code = getRegionCode(url_sido, sido_name)

    # 시/군/구 코드 찾기
    sigungu_name = input("시/군/구를 입력하세요: ")
    url_sigungu = url_home+'sigungu?'+serviceKey+'&upr_cd=' + sido_code
    sigungu_code = getRegionCode(url_sigungu, sigungu_name)

    #보호소 찾기
    url_shelter = url_home + 'shelter?' + serviceKey + '&upr_cd=' + sido_code + '&org_cd=' + sigungu_code
        #보호소 출력
    print('보호소 목록: ')
    printItem(url_shelter, "careNm")
    print("========================================")

def searchAnimal():
    global sido_code, sigungu_code, bgn_date, end_date, mailData
    menuStatus = True
    pgNm = 1
    i = 1
    print("============== 유기동물 검색 ==============")
    print("찾고싶은 기간(유기날짜)를 입력해주세요!")
    bgn_date = input("검색시작 날짜(YYYYMMDD): ")
    end_date = input("검색종료 날짜(YYYYMMDD): ")

    # 시/도 조건
    sido_name = input("시/도를 입력하세요: ")
    url_sido = url_home + "sido?" + serviceKey
    sido_code = getRegionCode(url_sido, sido_name)

    # 시/군/구 조건
    sigungu_name = input("시/군/구를 입력하세요: ")
    url_sigungu = url_home + 'sigungu?' + serviceKey + '&upr_cd=' + sido_code
    sigungu_code = getRegionCode(url_sigungu, sigungu_name)

    # 축종 조건
    animal_kind = input("동물 종류를 입력하세요(1.개/ 2.고양이/ 3.기타/ 4.상관없음: ")
    if animal_kind == '1': # 개 품종 조건
        animal_code = "&upkind=417000"
        kind_name = input("품종을 입력하세요(0.상관없음): ")
        if kind_name == '0': kind_code = ""
        else:
            kind_code = '&kind=' + getDogKindCode(kind_name)

    elif animal_kind == '2': #고양이
        animal_code = "&upkind=422400"
        kind_code = ""
    elif animal_kind == '3': #기타
        animal_code = "&upkind=429900"
        kind_code = ""
    elif animal_kind == '4': #상관없음
        animal_code = ""
        kind_code = ""

    while (menuStatus):
        url_searchAbandonment = \
            url_home+'abandonmentPublic?' + serviceKey + '&bgnde=' + bgn_date + '&endde=' + end_date \
            + animal_code + kind_code +'&org_cd=' + sigungu_code + \
            '&pageNo=' + str(pgNm) + '&numOfRows=1'
        response = request.urlopen(url_searchAbandonment).read()
        tree = ElementTree.fromstring(response)
        itemElements = tree.getiterator("item")
        for item in itemElements:
            print("=============== %d =================" % i)
            printAnimal(item)

        print("페이지번호. [%d]" % pgNm)
        menuSel = str(input("1. 메뉴로 / 2. 다음페이지 / 3. 이전페이지 / 4. 현재 페이지 메일로 보내기 / 5. 보호소 위치 지도 보기: "))
        if menuSel == '2':
            i += 1
            pgNm += 1
        elif menuSel == '3':
            if pgNm > 1:
                i -= 1
                pgNm -= 1
        elif menuSel == '4':
            sendMail(mailData)
        elif menuSel == '5':
            show_map(loc)
        else:
            menuStatus = False


def getRegionCode(url, search_name):
    response = request.urlopen(url).read()
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find('orgdownNm')
        name = name.text
        if name == search_name:
            result = item.find("orgCd")
            return result.text

def getDogKindCode(search_name):
    response = request.urlopen(url_dog).read()
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find('KNm')
        name = name.text
        if name == search_name:
            result = item.find("kindCd")
            return str(result.text)

def printItem(url, item_name):
    response = request.urlopen(url).read()
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find(item_name)
        print(name.text)

def printAnimal(item):
    global mailData, loc
    print("-----동물정보-----")
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
    print("상태: ", processState.text)
    print("품종: ", kindCd.text)
    print("나이: ", age.text)
    print("성별: ", sexCd.text)
    print("색상: ", colorCd.text)
    print("중성화 여부: ", neuterYn.text)
    print("특징: ", specialMark.text)
    print("체중: ", weight.text)
    print("발견장소: ", happenPlace.text)
    print("사진: ", photo.text)
    print("-----보호 정보-----")
    happenDt = item.find("happenDt")
    careNm = item.find("careNm")
    careAddr = item.find("careAddr")
    careTel = item.find("careTel")
    chargeNm = item.find("chargeNm")
    officetel = item.find("officetel")
    orgNm = item.find("orgNm")
    noticeNo = item.find("noticeNo")
    desertionNo = item.find("desertionNo")

    print("접수일: ", happenDt.text)
    print("보호소 이름: ", careNm.text)
    print("보호 주소: ", careAddr.text)
    print("보호소 전화번호: ", careTel.text)
    print("담당자: ", chargeNm.text)
    print("담당자 연락처: ", officetel.text)
    print("관할기관: ", orgNm.text)
    print("공고번호: ", noticeNo.text)
    print("유기번호: ", desertionNo.text)

    mailData = "-----동물정보-----" +"\n상태: "+processState.text +"\n품종: " + kindCd.text +"\n나이: "+ \
               age.text+"\n성별: "+ sexCd.text +"\n색상: "+ colorCd.text +"\n중성화 여부: "+ neuterYn.text +\
               "\n특징: "+ specialMark.text +"\n체중: "+ weight.text +"\n발견장소: "+ happenPlace.text \
               +"\n사진: "+ photo.text + "\n-----보호 정보-----"+"\n접수일: "+ happenDt.text + "\n보호소 이름: " + \
               careNm.text + "\n보호 주소: "+ careAddr.text + "\n보호소 전화번호: "+ careTel.text + "\n담당자: "+ \
               chargeNm.text + "\n담당자 연락처: " + officetel.text + "\n관할기관: "+ orgNm.text + "\n공고번호: "+ \
               noticeNo.text + "\n유기번호: "+ desertionNo.text

    loc = careAddr.text