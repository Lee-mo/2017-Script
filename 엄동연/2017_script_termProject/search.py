from urllib import request
from xml.etree import ElementTree

url_home = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/'
serviceKey = 'serviceKey=OyfS4qqxnYyHXNdGgHg%2Bem2F%2FLAjaG4C0X2kgqycc%2B2G3%2F0flCjg9GIptnv23C3UXWRH3wjd3EuE31%2FGSX71ZA%3D%3D'
pgNm = 1

def searchShelter():
    global sido_code, sigungu_code

    print("============== 보호소 검색 ==============")

    # 시/도 코드 찾기
    sido_name = input("시/도를 입력하세요: ")
    url_sido = url_home + "sido?" + serviceKey
    response = request.urlopen(url_sido).read()
    sido_code = getRegionCode(response, sido_name)

    # 시/군/구 코드 찾기
    sigungu_name = input("시/군/구를 입력하세요: ")
    url_sigungu = url_home+'sigungu?'+serviceKey+'&upr_cd=' + sido_code
    response = request.urlopen(url_sigungu).read()
    sigungu_code = getRegionCode(response, sigungu_name)

    #보호소 찾기
    url_shelter = url_home + 'shelter?' + serviceKey + '&upr_cd=' + sido_code + '&org_cd=' + sigungu_code
    response = request.urlopen(url_shelter).read()

    #보호소 출력
    print('보호소 목록: ')
    printItem(response, "careNm")

def getRegionCode(response, search_name):
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find('orgdownNm')
        name = name.text
        if name == search_name:
            result = item.find("orgCd")
            return result.text

def printItem(response, item_name):
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find(item_name)
        print(name.text)

def searchAbandonment():
    global sido_code, sigungu_code, bgn_date, end_date
    menuStatus = True
    pgNm = 1
    print("============== 유기동물 검색 ==============")
    # 시/도 코드 찾기
    sido_name = input("시/도를 입력하세요: ")
    url_sido = url_home + "sido?" + serviceKey
    response = request.urlopen(url_sido).read()
    sido_code = getRegionCode(response, sido_name)

    # 시/군/구 코드 찾기
    sigungu_name = input("시/군/구를 입력하세요: ")
    url_sigungu = url_home+'sigungu?'+serviceKey+'&upr_cd=' + sido_code
    response = request.urlopen(url_sigungu).read()
    sigungu_code = getRegionCode(response, sigungu_name)

    print("찾고싶은 기간(유기날짜)를 입력해주세요!")
    bgn_date = input("검색시작 날짜(YYYYMMDD) : ")
    end_date = input("검색종료 날짜(YYYYMMDD) : ")

    while(menuStatus):
        url_searchAbandonment = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?'+serviceKey+'&bgnde='+bgn_date+'&endde='+end_date+'&org_cd='+sigungu_code+'&pageNo='+str(pgNm)+'&numOfRows=10'
        response = request.urlopen(url_searchAbandonment).read()
        tree = ElementTree.fromstring(response)
        itemElements = tree.getiterator("item")
        i = 1
        for item in itemElements:
            print("=============== %d =================" %i)
            age = item.find('age')
            careAddr = item.find('careAddr')
            careTel = item.find('careTel')
            chargeNm = item.find('chargeNm')
            colorCd = item.find('colorCd')
            happenPlace = item.find('happenPlace')
            kindCd = item.find('kindCd')
            processState = item.find('processState')
            specialMark = item.find('specialMark')
            weight = item.find('weight')
            print("품종: %s" %kindCd.text)
            print("털색: %s" %colorCd.text)
            print("나이: %s" %age.text)
            print("몸무게: %s" %weight.text)
            print("특이사항: %s" %specialMark.text)
            print("발견장소: %s" %happenPlace.text)
            print("보호중인 주소: %s" %careAddr.text)
            print("보호자 전화번호: %s" %careTel.text)
            print("보호자 이름: %s" %chargeNm.text)
            print("보호상태: %s" %processState.text)
            i+=1

        print("페이지번호. [%d]" % pgNm)
        menuSel = str(input("1. 메뉴로 / 2.다음페이지: "))
        if menuSel == '2':
            pgNm = pgNm + 1
        else:
            menuStatus = False







