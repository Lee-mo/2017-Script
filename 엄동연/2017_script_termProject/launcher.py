from search import *
loopFlag = True

def printMenu():
    print("=================== 메 뉴 ==================")
    print("1. 종료")
    print("2. 보호소 검색")
    print("3. 유기동물 검색")
    print("===========================================")

def launcherFunction(menu):
    if menu == '1':
        Quit()
    elif menu == '2':
        searchShelter()
    elif menu == '3':
        searchAnimal()
    else:
        print("Error: menu")

def Quit():
    global loopFlag
    loopFlag = False


def main():
    while(loopFlag == True):
        printMenu()
        menu = str(input('select menu: '))
        launcherFunction(menu)
        pass
    else:
        print("다음에 또 만나요.")

main()