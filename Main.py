false = False
true = True
debug = false

#Offset values
Title = 0
Version = 1
BuildType_Offset = 2
#-------------

#Config values
TitleText = "Testing"
VersionText = "V0.4.2.5"
BuildType_Text = "Dev"
#-------------

info = [TitleText, VersionText, BuildType_Text]


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

    
def DisplayMenu(oldSubMenuActive, oldMenuActive, data):
    print(ScaleTextSides(data[1], ' ', 20, True))


def displayMenu(menu):
    header()    
      
running = True
menuActive = -1
subMenuActive = -1;

def menu(Title, Body, Date):
   print(Title + Body + Date)
   return "w";

while running:


    MainMenu = ['Cards', 'test']
    menu = [MainMenu]

    card1Option1 = ["Title", "body", "date"]
    card1Option2 = ["Title2", "body2", "date2"]

    card1Loc = ["O"] + card1Option1
    card2Loc = ["O"] + card1Option2 #menu(card1Option1[0], card1Option1[1], card1Option1[2])]
    card1 = ["Card 1 Menu", "Body", card1Loc]#, card1Loc[0]]
    
    card2 = ["Card 2 Menu", "Body", card2Loc]
    cardsSubMenu = [card1, card2]

    testSubMenu = ['1', '2']
    menuListActive = [menu, cardsSubMenu, testSubMenu]

    displayMenu(menu)
    print(ScaleTextSides("", ' ', 20, True))
    subOptionCount = len(menuListActive[ int(menuActive) ][int(subMenuActive)] )
    if(menuListActive[ int(menuActive) ][int(subMenuActive)]):
       for e in range(0, int( subOptionCount)    ):
          # print("Test1: i: " + str(e))
           if(menuActive != -1):
               #for i in range(0, len(((menuListActive[int(menuActive)])  [int(subMenuActive)] ))):
                   #print("Test1: i: " + str(i))
                   #print("Yeet")   [[  len(menuListActive [int(menuActive)]   [int(postModsSub)   ]    )-1][0]]
                   if(subMenuActive != -1 and ((menuListActive[int(menuActive)])[int(subMenuActive)] )[0][0] == 'O'): 
                      #print(ScaleTextSides(str(e+1)+ ": " + ((menuListActive[int(menuActive)])[int(subMenuActive)] )[e][subMenuActive][0], ' ', 20, True))
                      DisplayMenu(subMenuActive, menuActive, ((menuListActive[int(menuActive)])[int(subMenuActive)] )[2])
                   else:
                      if(e < len(menuListActive[ int(menuActive) ][int(subMenuActive)] )-1):
                         print(ScaleTextSides(str(e+1)+ ": " + ((menuListActive[int(menuActive)])[int(subMenuActive)] )[e], ' ', 20, True))

           else:
               print(ScaleTextSides(str(e+1)+ ": " + str((menuListActive[int(menuActive)][int(subMenuActive)])[e]), ' ', 20, True))


    postModsSub = subMenuActive    
    if(menuActive == -1):
        menuActive = int(input("Menu: "))-1
    elif(subMenuActive == 0):
        subMenuActive = int(input( ": "))#int(input(menuListActive[int(menuActive)][int(subMenuActive)]))
    elif(subMenuActive != 0):
        subMenu_Selection = int(input(": "))#int(input(menuListActive[int(menuActive)][int(subMenuActive)]))
      #  if(subMenu_Selection == int(input("subMenu: ")+1)):
        subMenuActive = 0


    currentActiveMenu = menuListActive[int(menuActive)]
    selectedSub = len(menuListActive [int(menuActive)]   [int(postModsSub)]    )-1

    if(str(currentActiveMenu[int(postModsSub)]    [selectedSub][0] == "O")): #  [  subMenuActive * ( selectedSub-2 * 2)  ]) == "O"):
      print("Yetettetette")
