import math
def number(s):
    try:
        float(s)
        return True
    except ValueError:
       return False
V = input("What is the velocity of the mass in this problem: ")
if number(V):
    V = float(V)    
Fc = input("What is the centripetal force acting on the mass in this problem: ")
if number(Fc):
    Fc = float(Fc)
m = input("What is the mass of the object in this problem: ")
if number(m):
    m = float(m)
r = input("What is the radius of the circular path that the mass is traveling on in this problem: ")
if number(r):
    r = float(r)
ac = input("What is the centripetal acceleration of the mass in this problem: ")
if number(ac):
    ac = float(ac)
bruh = ['V', 'Fc', 'm', 'r','ac']
unknown = input("What do you want to solve for (V, Fc, m, r, ac)?: ")
wow = True
while wow:
    if unknown not in bruh:
        print("We don't have the facilities for that mate")
        unknown = input("What do you want to solve for (V, Fc, m, r, ac)?: ")
    if unknown == 'V':
        if (type(Fc) == float and type(r) == float and type(m) == float): 
            V = math.sqrt(Fc*r/m)
            print(V)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (V, Fc, m, r, ac)?: ")
    if unknown == 'Fc':
        if (type(m) == float and type(r) == float and type(V) == float): 
            Fc = V**2 * m/r
            print(Fc)
            wow = False
        elif (type(ac) == float and type(m) == float): 
            Fc = m * ac
            print(Fc)
            wow = False
        else:
            print("You don't quite have the facilites for that mate")
            unknown = input("What do you want to solve for (V, Fc, m, r, ac)?: ")
    if unknown == 'm':
        if (type(Fc) == float and type(r) == float and type(V) == float): 
            m = Fc*r/(V**2)
            print(m)
            wow = False
        elif (type(ac) == float and type(Fc) == float): 
            m = Fc/ac
            print(m)
            wow = False
        else:
            print("You don't quite have the facilites for that mate")
            unknown = input("What do you want to solve for (V, Fc, m, r, ac)?: ")
    if unknown == 'Fc':
        if (type(m) == float and type(r) == float and type(V) == float): 
            Fc = V**2 * m/r
            wow = False
        elif (type(ac) == float and type(m) == float): 
            Fc = m * ac
            wow = False
        else:
            print("You don't quite have the facilites for that mate")
            unknown = input("What do you want to solve for (V, Fc, m, r, ac)?: ")
    if unknown == 'r':
        if (type(Fc) == float and type(V) == float and type(m) == float): 
            r = (m * V**2)/Fc
            print(r)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (V, Fc, m, r, ac)?: ")
    if unknown == 'ac':
        if (type(r) == float and type(V) == float): 
            ac = (V**2)/r
            print(ac)
            wow = False
        elif (type(Fc) == float and type(m) == float): 
            ac = (V**2)/r
            print(ac)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (V, Fc, m, r, ac)?: ")

