import math
def number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
bruh = ['F', 'm', 'a', 'Fg', 'N']
F = input("What is the external force in this problem: ")
if number(F):
    F = float(F) 
m = input("What is the mass of the object in this problem: ")
if number(m):
    m = float(m) 
a = input("What is the acceleration of the mass in this problem: ")
if number(a):
    a = float(a) 
Fg = input("What is the force of gravity on the mass in this problem: ")
if number(Fg):
    Fg = float(Fg)
N = input("What is the normal force on the mass in this problem: ")
if number(N):
    N = float(N) 
unknown = input("What do you want to solve for (F, m, a, Fg, N)?: ")
wow = True
while wow:
    if unknown not in bruh:
        print("We don't have the facilities for that mate")
        unknown = input("What do you want to solve for (F, m, a, Fg, N)?: ")
    if unknown == 'F':
        if (type(m) == float and type(a) == float):
            F = m*a
            print(F)
            wow = False
        elif (type(N) == float and type(a) == float):
            F = (N*a)/9.8
            print(F)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (F, m, a, Fg, N)?: ")
    if unknown == 'm':
        if (type(N) == float):
            m = N/9.8
            print(m)
            wow = False
        elif (type(F) == float and type(a) == float):
            m = F/a
            print(m)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (F, m, a, Fg, N)?: ")
    if unknown == 'a':
        if (type(m) == float and type(F) == float):
            a = F/m
            print(a)
            wow = False
        elif (type(N) == float and type(a) == float):
            a = (F*9.8)/N
            print(F)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (F, m, a, Fg, N)?: ")
    if unknown == 'Fg':
        if (type(m) == float and type(a) == float):
            Fg = m*9.81
            print(Fg)
            wow = False
        elif (type(N) == float):
            Fg = -1*N
            print(Fg)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (F, m, a, Fg, N)?: ")
    if unknown == 'N':
        if (type(m) == float):
            N = m*9.81
            print(N)
            wow = False
        elif (type(F) == float, type(a) == float):
            N = F*9.8/a
            print(N)
            wow = False
        else:
           print("You don't quite have the facilites for that mate")
           unknown = input("What do you want to solve for (F, m, a, Fg, N)?: ")
