
Title = 0
Version = 1
TitleText = "Testing"
info = [TitleText, "V0.0.0.1"]
def ScaleTextSides(Text, spaceChar, width, side):
   #print(Text)
    #//print(spaceChar)
   # //print(width)
   sides = ""
   t = 0
   if(side):
       sides = '|'
       t = -2
   done = sides + Text + spaceChar*(width-(len(Text)-1) + t) + sides
    #  //print(done)
  #  print(width-(len(Text)-1))
   return (done)
    
def header():
    print("|")
    print(ScaleTextSides('', '-', 20, False))
 #   print("2222********************")
    print(ScaleTextSides(info[Title], ' ', 20, True))
    

def displayMenu(menu):
    header()    
running = True
menuActive = 0
subMenuActive = 0;

while running:


    menu = ['Cards', 'test']

    card1 = ["Title", "Body"]
    card2 = ["Title", "Body"]
    cardsSubMenu = [card1, card2]

    testSubMenu = ['1', '2']
    menuListActive = [menu, cardsSubMenu, testSubMenu]

    displayMenu(menu)
    print(ScaleTextSides("", ' ', 20, True))
    for e in range(0, len(menuListActive[int(menuActive)])):
        print("Test1: i: " + str(e))
        if(menuActive != 0):
            for i in range(0, len(((menuListActive[int(menuActive)])[int(subMenuActive)] ))):
                print("Test1: i: " + i)
                print("Yeet")
                print(ScaleTextSides(str(i+1)+ ": " + ((menuListActive[int(menuActive)])[int(subMenuActive)] )[i], ' ', 20, True))
        else:
            print(ScaleTextSides(str(e+1)+ ": " + (menuListActive[int(menuActive)])[e], ' ', 20, True))
        
    if(menuActive == 0):
        menuActive = input(": ")
        
    if(subMenuActive == 0):
        subMenuActive = input(menuListActive[int(menuActive)])
        
