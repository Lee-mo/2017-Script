from urllib import request
from xml.dom.minidom import *
from xml.etree import ElementTree

serviceKey = 'serviceKey=OyfS4qqxnYyHXNdGgHg%2Bem2F%2FLAjaG4C0X2kgqycc%2B2G3%2F0flCjg9GIptnv23C3UXWRH3wjd3EuE31%2FGSX71ZA%3D%3D'

def print10():
    response = request.urlopen('http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?'
                                    'serviceKey=OyfS4qqxnYyHXNdGgHg%2Bem2F%2FLAjaG4C0X2kgqycc%2B2G3%2F0flCjg9GIptnv23C3UXWRH3wjd3EuE31%2FGSX71ZA%3D%3D&'
                                    'bgnde=20140601&endde=20170521&upkind=417000&numOfRows=10&pageSize=10').read()
    tree = ElementTree.fromstring(response)
    #print(response)
    itemElements = tree.getiterator("item")
    #print(itemElements)
    for item in itemElements:
        age = item.find("age")
        print(age.text)


def searchShelter():
    global sido_num, sigungu_num

    print("==========보호소 검색==========")
    sido = input("시/도를 입력하세요: ")

    url_sido = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido?' + serviceKey
    response = request.urlopen(url_sido).read()
    #print(response)

    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find('orgdownNm')
        sido_name = name.text
        if sido_name == sido:
            ret = item.find("orgCd")
            sido_num = ret.text
            #print(sido_num)

    sigungu = input("시/군/구를 입력하세요: ")
    url_sigungu = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sigungu?'+serviceKey+'&upr_cd=' + sido_num
    response = request.urlopen(url_sigungu).read()
    #print(response)
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find('orgdownNm')
        sigungu_name = name.text
        if sigungu_name == sigungu:
            ret = item.find("orgCd")
            sigungu_num = ret.text
            #print(sido_num)

    url_shelter = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/shelter?'+serviceKey+'&upr_cd='+sido_num+'&org_cd='+sigungu_num
    response = request.urlopen(url_shelter).read()
    #print(response)
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    print('보호소 목록: ')
    for item in itemElements:
        name = item.find('careNm')
        print(name.text)


def searchAbandonment():
    global sido_num, sigungu_num, bgn_date, end_date
    print("==========유기동물 검색==========")
    sido = input("시/도를 입력하세요: ")

    url_sido = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido?' + serviceKey
    response = request.urlopen(url_sido).read()
    # print(response)

    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find('orgdownNm')
        sido_name = name.text
        if sido_name == sido:
            ret = item.find("orgCd")
            sido_num = ret.text
            # print(sido_num)

    sigungu = input("시/군/구를 입력하세요: ")
    url_sigungu = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sigungu?' + serviceKey + '&upr_cd=' + sido_num
    response = request.urlopen(url_sigungu).read()
    # print(response)
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
        name = item.find('orgdownNm')
        sigungu_name = name.text
        if sigungu_name == sigungu:
            ret = item.find("orgCd")
            sigungu_num = ret.text

    print("찾고싶은 기간(유기날짜)를 입력해주세요!")
    bgn_date = input("검색시작 날짜(YYYYMMDD) : ")
    end_date = input("검색종료 날짜(YYYYMMDD) : ")

    url_searchAbandonment = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?'+serviceKey+'&bgnde='+bgn_date+'&endde='+end_date+'&org_cd='+sigungu_num+'&pageNo=1&numOfRows=10'
    response = request.urlopen(url_searchAbandonment).read()
    tree = ElementTree.fromstring(response)
    itemElements = tree.getiterator("item")
    for item in itemElements:
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
        print(age.text)
        print(careAddr.text)
        print(careTel.text)
        print(chargeNm.text)
        print(colorCd.text)
        print(happenPlace.text)
        print(kindCd.text)
        print(processState.text)
        print(specialMark.text)
        print(weight.text)




