listDict = {}
listtes = ['satu', 'dua', 'tiga']
def mainmenu():
    menu = int(input('Main Menu\n1. Lihat full Dictionary\n2. Isi Dictionary\n3. Searching Dictionary\n4. Keluar\nMasukkan pilihan : '))
    index = menu-1
    menuList = [showFullDict, dictContent, searchDict, exit]
    menuList[index]()
    
def showFullDict():
    i=0
    print('________________________________________')
    print('|       Key       |         Value       |')
    print('----------------------------------------')
    if(len(listDict) == 0):
        print('|     Kosong      |astaghfirullahaladzim|')
    for item in listDict:
        print('|'+str(i+1)+'. ' + '   {}        |    {}             |'.format(item,listDict[item]))
        i+=1
    mainmenu()

def dictContent():
    listPil = ['String','Number']
    check = False
    
    while(check == False):
        pilihan = input('Berapa kali masukkan dictionary? : ')
        if(str.isdigit(pilihan) == True):
            check = True
            pilihan = int(pilihan)
            for item in range(pilihan):
                for item1 in range(len(listPil)):
                    print(str(item1+1)+'. {}'.format(listPil[item1]))
                check1 = False
                while(check1 == False):
                    
                    inputpil = int(input('Masukkan Pilihan : '))
                    if(inputpil > 0 and inputpil < 3):  
                        check1 = True
                        inputstringornum(inputpil)
                    else:
                        print('Salah input!')
        else:
            print('Inputan salah!')
    mainmenu()

def inputstringornum(x):
    
    if(x == 1):
        keytodict = input('Masukkan key : ')
        check = False
        while(check == False):
            valuetodict = input('Masukkan value : ')
            if(str.isalpha(valuetodict) == True or str.isdigit(valuetodict) == False):
                check = True
            else:
                print('Data Harus berbentuk string!')
        listDict[keytodict] = valuetodict

    elif(x == 2):
        keytodict = input('Masukkan key : ')
        check = False
        while(check == False):
            valuetodict = input('Masukkan value : ')
            if(str.isdigit(valuetodict) == True):
                check = True
            else:
                print('Data Harus berbentuk number!')
        listDict[keytodict] = valuetodict

def searchDict():
    searchword =input('Search Key : ')
    print('________________________________________')
    print('|       Key       |         Value       |')
    print('----------------------------------------')
    i=0
    for item in listDict:
        if str.lower(searchword) in str.lower(item):
            print('|'+str(i+1) + '.  {}      |       {}     | '.format(item,listDict[item]))
     
    mainmenu()

mainmenu()