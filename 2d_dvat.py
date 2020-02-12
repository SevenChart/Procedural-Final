import math
#VeryLimitedFunctionality
print("This program assumes that acceleration on the x-axis is zero")
def number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
t = input("What is the change in time in this problem: ")
if number(t):
    t = float(t)    
theta = input("What is the angle of elevation of the initial velocity in this problem: ")
if number(theta):
    theta = float(theta)
alpha = input("What is the angle of depression of the final velocity in this problem: ")
if number(alpha):
    alpha = float(alpha)
Vi= input("What is the initial velocity in this problem: ")
if number(Vi):
    Vi = float(Vi)
Vf = input("What is the final velocity in this problem: ")
if number(Vf):
    Vf = float(Vf)
dx = input("What is the delta x in this problem: ")
if number(dx):
    dx = float(dx)
ay = input("What is the acceleration on the y-axis in this problem: ")
if number(ay):
    ay = float(ay)
dy = input("what is the vertical displacement in this problem: ")
if number(dy):
    dy = float(dy)
unknown = input("What do you want to solve for (t, dx, dy, Vf)?: ")
yo = ['dx', 'Vf', 't', 'dy']
wow = True
while wow:
    if unknown not in yo:
        print("We don't have the facilities for that mate")
        unknown = input("What do you want to solve for (t, dx, dy, Vf)?: ")
    if unknown == 't':
        if (type(Vi) == float and type(theta) == float and type(dx) == float):
            t = dx/(Vi * math.cos(theta))
            print(t)
            wow = False
        elif (type(Vi) == float and type(dy) == float and type(theta) == float and type(ay) == float):
            t1 = (-1*Vi + math.sqrt((Vi*math.sin(theta))**2 - 4*(ay/2)*(-dy)))/ay
            t2 = (-1*Vi - math.sqrt((Vi*math.sin(theta))**2 - 4*(ay/2)*(-dy)))/ay
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
           unknown = input("What do you want to solve for (t, dx, dy, Vf)?: ")
    if unknown == 'dy':
        if (type(Vi) == float and type(theta) and type(t) == float and type(ay)): 
            dy = Vi * math.sin(theta) * t + (ay * t**2)/2
            print(dy)
            wow = False
        else:
            print("You don't quite have the facilites for that mate")
            unknown = input("What do you want to solve for (t, dx, dy, Vf)?: ")
    if unknown == 'dx':
        if (type(Vi) == float and type(t) and type(theta) == float): 
            dx = t * Vi * math.cos(theta)
            print(dx)
            wow = False
        else:
            print("You don't quite have the facilites for that mate")
            unknown = input("What do you want to solve for (t, dx, dy, Vf)?: ")
    if unknown == 'Vf':
        if (type(Vi) == float and type(theta)== float and type(alpha) == float): 
            Vf = Vi * math.cos(theta) * math.cos(alpha)
            print(Vf)
            wow = False
        else:
            print("You don't quite have the facilites for that mate")
            unknown = input("What do you want to solve for (t, dx, dy, Vf)?: ")
