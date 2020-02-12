import math
def number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
dx = input("What is the delta x in this problem: ")
if number(dx):
    dx = float(dx)    
t = input("What is the change in time of this problem: ")
if number(t):
    t = float(t)
Vi = input("What is the initial velocity in this problem: ")
if number(Vi):
    Vi = float(Vi)
Vf = input("What is the final velocity in this problem: ")
if number(Vf):
    Vf = float(Vf)
a = input("What is the acceleration in this problem: ")
if number(a):
    a = float(a)
bruh = ['Vi', 'Vf', 'a', 't', 'dx']
unknown = input("What do you want to solve for (dx, t, Vi, Vf, a)?: ")
wow = True
while wow:
    if unknown not in bruh:
        print("We don't have the facilities for that mate")
        unknown = input("What do you want to solve for (dx, t, Vi, Vf, a)?: ")
    if unknown == 'dx':
        if (type(Vi) == float and type(a) == float and type(t) == float): 
            dx = Vi*t + (a*t**2)/2
            print(dx)
            wow = False
        elif (type(Vf) == float and type(a) == float and type(t) == float): 
            dx = Vf*t - (a*t**2)/2
            print(dx)
            wow = False
        elif (type(Vi) == float and type(a) == float and type(Vf) == float):
            dx = (Vf**2 - Vi**2)/(2*a)
            print(dx)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (dx, t, Vi, Vf, a)?: ")
    if unknown == 'Vi':
        if (type(a) == float and type(t) == float and type(Vf) == float): 
            Vi = Vf - a*t
            print(Vi)
            wow = False
        elif (type(t) == float and type(a) == float and type(dx) == float):
            Vi = (2*dx - a*t**2)/(2*t)
            print(Vi)
            wow = False
        elif (type(dx) == float and type(a) == float and type(Vf) == float):
            Vi = math.sqrt(Vf**2-(2*a*dx))
            print(Vi)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (dx, t, Vi, Vf, a)?: ")
    if unknown == 'Vf':
        if (type(a) == float and type(t) == float and type(Vi) == float): 
            Vf = Vi + a*t
            print(Vf)
            wow = False
        elif (type(dx) == float and type(a) == float and type(Vi) == float):
            Vf = math.sqrt(Vf**2+(2*a*dx))
            print(Vf)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (dx, t, Vi, Vf, a)?: ")
    if unknown == 'a':
        if (type(Vi) == float and type(Vf) == float and type(t) == float): 
            a = (Vf - Vi)/t
            print(a)
            wow = False
        elif (type(Vi) == float and type(dx) == float and type(Vf) == float):
            a = (Vf**2 - Vi**2)/(2*dx)
            print(a)
            wow = False
        elif (type(dx) == float and type(t) == float and type(Vi) == float):
            a = (2*(dx - Vi * t))/(t**2)
            print(a)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (dx, t, Vi, Vf, a)?: ")
    if unknown == 't':
        if (type(Vi) == float and type(Vf) == float and type(a) == float): 
            t = (Vf - Vi)/a
            print(t)
            wow = False
        elif (type(Vi) == float and type(dx) == float and type(Vf) == float):
            t1 = (-1*Vi + math.sqrt((Vi)**2 - 4*(a/2)*(-dx)))/a
            t2 = (-1*Vi - math.sqrt((Vi)**2 - 4*(a/2)*(-dx)))/a
            if (t1 > 0 and t2 < 0):
                t = t1
            elif (t1 < 0 and t2 > 0):
                t = t2
            elif t1 == t2:
                t = t1
            print(t)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (dx, t, Vi, Vf, a)?: ")
