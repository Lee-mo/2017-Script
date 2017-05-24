from search import *

loopFlag = True

def printMenu():
    print("사지 마세요, 입양하세요!")
    print("===========메뉴==========")
    print("q: 종료")
    print("ss: 보호소 검색")
    print("a: 임시")
    print("=========================")

def lancherFunction(menu):
    if menu == 'q':
        Quit()
    elif menu == 'ss':
        searchShelter()
    elif menu == 'a':
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