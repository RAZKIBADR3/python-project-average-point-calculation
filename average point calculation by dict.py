import os
class point :
    name = "X"
    N1 = 0.0
    N2 = 0.0
    efm = 0.0

    def enterdata(self) :
        li = []
        self.name = input("entre your name\n")
        self.N1 = float(input("entre your fisrt point\n"))
        self.N2 = float(input("entre your secondary point\n"))
        self.efm = float(input("entre your efm point\n"))
        
        li.append(self.N1)
        li.append(self.N2)
        li.append(self.efm)
        
        dict[self.name] = li


    def showdata(self) :
        NP = input("entre your name to show the point\n")
        os.system('cls')
        avaible = False 
        for i in dict.keys() :
            if NP == i :
                avaible = True
                print(dict[i])
        if avaible == False :
            print("this name is not avaible")
        N = input("entre 'entre' in keyboad to continue")
                

    def calculdata(self) :
        NC = input("entre your name to calcul your moyen\n")
        os.system('cls')
        avaible = False
        for i in dict.keys() :
            if NC == i :
                avaible = True
                LC = dict[NC]
                M1 = ( LC[0] + LC[1] ) / 2
                M2 = LC[2] * 2
                M = (M1 + M2) / 3
                print(M)
        if avaible == False :
            print("this name is not avaible")
        N = input("entre 'entre' in keyboad to continue")


dict = {}
x = point()
print("1-enter data\n2-show point\n3-calcul point\n4-exit")
CH = int(input("entre what you want\n"))
os.system('cls')
while CH!= 4 :
    if CH == 1 :
        x.enterdata()
    elif CH == 2 :
        x.showdata()
    elif CH == 3 :
        x.calculdata()
    else :
        print("this choose is not avaible")

    os.system('cls')
    print("1-enter data\n2-show point\n3-calcul point\n4-exit")
    CH = int(input("entre what you want\n"))
    os.system('cls')

os.system('cls')
print("programme finished")