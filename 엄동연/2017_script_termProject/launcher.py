from search import *

loopFlag = True


def printMenu():
    print("사지 마세요, 입양하세요!")
    print("=================== 메 뉴 ==================")
    print("1. 종료")
    print("2. 보호소 검색")
    print("3. 지역별 유기동물 검색")
    print("===========================================")

def lancherFunction(menu):
    if menu == '1':
        Quit()
    elif menu == '2':
        searchShelter()
    elif menu == '3':
        searchAbandonment()
    else:
        print("Error: menu")

def Quit():
    global loopFlag
    loopFlag = False

while(loopFlag == True):
    printMenu()
    menu = str(input('select menu: '))
    lancherFunction(menu)
else:
    print("다음에 또 만나요.")