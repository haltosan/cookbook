'''
raw format:
pg, tag 1, tag 2, tag 3, ...
end of tag is ', '
tag can't contain ,
'''

from termcolor import colored

primary = "blue"
secondary = "cyan"
basic = "white"

def b(txt):
  print(colored(txt,basic))
def bn(txt):
  print(colored(txt,basic),end="")

def p(txt):
  print(colored(txt,primary))

def s(txt):
  print(colored(txt,secondary))

def showColors():
  available = 'red, green, yellow, blue, magenta, cyan, white'.split(", ")
  for i in available:
    print(colored(i,i),end=" ")
  print()

def createSearchFile():
  a = open("raw.txt","r")
  raw = a.read()
  a.close()

  tags = []  #this is used to sort the search table
  searchTable = {}

  b("**enumerate tags**")
  lines = raw.split("\n")
  for i in lines:
    cells = i.split(", ")
    for l in range(1,len(cells)):
      if(not cells[l] in tags):
        b("  add"+cells[l])
        tags.append(cells[l])
        searchTable[cells[l]] = []
      searchTable[cells[l]].append(cells[0])

  for tag in searchTable:
    searchTable[tag].sort()

  tags.sort()
  a = open("search.txt","w")  #clear the output file
  a.write("")
  a.close()

  a = open("search.txt","a")

  for tag in tags:
    buf = ""  #string buffer
    buf = buf+tag+":"
    for page in searchTable[tag]:
      buf = buf+page+", "
    buf = buf[:-2]  #remove last ', '
    a.write(buf+"\n")
  a.close()

def searchFor(term):
  a = open("search.txt","r")
  raw = a.read()
  a.close()
  lines = raw.split("\n")

  first = 0
  last = len(lines)-1
  c = 0
  while(True):
    c+=1
    mid = int((first+last)/2)
    midWord = lines[mid].split(":")[0]
    if(midWord<term):  #up
      first = mid+1
    elif(midWord>term):  #down
      last = mid-1
    else:
      print("")
      p("*"+midWord+"*")
      s(" "+lines[mid].split(":")[1])
      print("")
      break
    if(c>len(lines)):
      b("Timeout. I don't think it's here")
      break

def addEntry():
  bn("What page number?\n> ")
  num = input("")
  bn("Enter tags separated by ', ' (comma then space)\n> ")
  tags = input("")
  a = open("raw.txt","a")
  a.write(num+", "+tags+"\n")
  a.close()

def getColors():
  global primary, secondary, basic
  a = open("settings.txt","r")
  raw = a.read()
  a.close()
  lines = raw.split("\n")
  primary = lines[0].split(":")[0]
  secondary = lines[0].split(":")[1]
  basic = lines[0].split(":")[2]

def run():
  howdy = '''
                                                                                
      //   ) )                                //   ) )                          
    //         ___      ___     / ___       //___/ /   ___      ___     / ___  
    //        //   ) ) //   ) ) //\\ \\       / __  (   //   ) ) //   ) ) //\\ \\   
  //        //   / / //   / / //  \\ \\     //    ) ) //   / / //   / / //  \\ \\  
  ((____/ / ((___/ / ((___/ / //    \\ \\   //____/ / ((___/ / ((___/ / //    \\ \\ 
  '''
  getColors()
  p(howdy)

  while(True):
    p("---What do you want to do?---")
    s("1) Search for something")
    s("2) Add 1 entry")
    s("3) Add many entries")
    s("4) Refresh the search table")
    s("5) Change color scheme")
    s("99) Exit")
    bn("> ")
    choice = input("")
    if(choice=="1"):
      b("Enter search term")
      bn("> ")
      term = input("")
      searchFor(term)
    elif(choice=="2"):
      addEntry()
    elif(choice=="3"):
      while(True):
        addEntry()
        bn(" Keep going? (y/n)\n > ")
        cont = input("").lower()
        if(cont=="y" or cont=="yes"):
          break
    elif(choice=='4'):
      createSearchFile()
    elif(choice=='5'):
      available = 'red, green, yellow, blue, magenta, cyan, white'.split(", ")
      while(True):
        b(" Here are the available colors:")
        showColors()
        bn(" What do you want as the primary color\n > ")
        primary = input("")
        if(primary in available):
          break
        else:
          b(" Unknown color")
      while(True):
        b(" Here are the available colors:")
        showColors()
        bn(" What do you want as the secondary color\n > ")
        secondary = input("")
        if(secondary in available):
          break
        else:
          b(" Unknown color")
      while(True):
        b(" Here are the available colors:")
        showColors()
        bn(" What do you want as the basic color\n > ")
        basic = input("")
        if(basic in available):
          break
        else:
          b(" Unknown color")
      print("")
      s(" Here are your choices")
      s(" "+primary+" "+secondary+" "+basic)
      print("")
      a = open("settings.txt","w")
      a.write(primary+":"+secondary+":"+basic)
      a.close()
      getColors()
      
    elif(choice=="99"):
      break
    else:
      b("Unknown option")

  p("Have a nice day!")

run()
