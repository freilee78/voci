import os

if os.path.exists("D:\snow.txt") == True:
    fobj = open("D:\snow.txt", "a")
    print("Wortliste gefunden")
else:
    fobj = file("D:\snow.txt", "w")
    print("Neue Wortliste erstellt")
    
def askopt():
    opt = inputInt("1 = Abfragen deutsch, 2 = Abfragen englisch, 3 = Vokabular erfassen, 9 = Verlassen")
    return opt

def fetchvoc():
    mlang = input("Bitte deutsch erfassen")
    mgen = input("Bitte Geschlecht erfassen m/f/n")
    flang = input("Bitte englisch erfassen")
    fgen = input("Bitte Geschlecht erfassen m/f")
    plur = input("Bitte Mehrzahl erfassen")
    bunit = input("Bitte Unit erfassen")
    fobj.write("\n%s;%s;%s;%s;%s;%s" %(mlang,mgen,flang,fgen,plur,bunit))

def train():
    fobj = open("D:\snow.txt", "a")
    

opt = askopt()
if opt == 3:
    fetchvoc()
print(opt)
    
fobj.close()
