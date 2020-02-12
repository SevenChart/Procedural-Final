import math
import numpy as np
def number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
hmmm = ['up', 'down', '0', 'none', 'None']
cat = True
let = ['m1','m2','V1','V2','V3','Vo1','Vo2']
while cat:
    accelerating = input("Is the mass accelerating up the incline, down the incline, or not at all(up, down, or 0): ")
    if accelerating in hmmm:
        break
    else:
        accelerating = input("Is the collision elastic or inelastic(IE or E): ")
if (accelerating == '0' or accelerating == 'none'):
    F = input("What is the external force acting in the mass in this problem: ")
    if number(F):
        F = float(F)    
    N = input("What is the normal force acting on the mass in this problem: ")
    if number(N):
        N = float(N)
    Fg = input("What is the force due to gravity on the mass in this problem: ")
    if number(Fg):
        Fg = float(Fg)
    theta = input("What is the angle of elevation of the incline in this problem: ")
    if number(theta):
        theta = float(theta)
    m = input("What is the mass of the object/person in this problem: ")
    if number(m):
        m = float(m)
    unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
    wow = True
    while wow:
        if unknown == 'F':
            if (type(m) == float and type(theta) == float): 
                F = m * 9.8 * math.sin(theta)
                print(F)
                wow = False
            elif (type(N) == float and type(theta) == float):
                F = N * math.tan(theta)
                print(F)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'N':
            if (type(m) == float and type(theta) == float): 
                N = m * 9.8 * math.cos(theta)
                print(F)
                wow = False
            elif (type(F) == float and type(theta) == float):
                N = F * math.cos(theta)/math.sin(theta)
                print(N)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'Fg':
            if (type(m) == float): 
                Fg = m * 9.8
                print(Fg)
                wow = False
            elif (type(F) == float and type(theta) == float):
                Fg = F/math.sin(theta)
                print(Fg)
                wow = False
            elif (type(N) == float and type(theta) == float):
                Fg= N/math.cos(theta)
                print(N)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'theta':
            if (type(N) == float and type(m)): 
                theta = np.arccos(N/(m * 9.8)) 
                print(theta)
                wow = False
            elif (type(F) == float and type(N) == float):
                theta = np.arctan(F/N)
                print(theta)
                wow = False
            elif (type(F) == float and type(m) == float):
                theta = np.arcsin(F/m*9.8)
                print(theta)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'm':
            if (type(N) == float and type(theta) == float): 
                m = N/(9.8 * math.cos(theta))
                print(m)
                wow = False
            elif (type(F) == float and type(theta) == float):
                m = F/(9.8 * math.sin(theta))
                print(m)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        
if accelerating == 'up':
    F = input("What is the external force acting in the mass in this problem: ")
    if number(F):
        F = float(F)    
    N = input("What is the normal force acting on the mass in this problem: ")
    if number(N):
        N = float(N)
    Fg = input("What is the force due to gravity on the mass in this problem: ")
    if number(Fg):
        Fg = float(Fg)
    theta = input("What is the angle of elevation of the incline in this problem: ")
    if number(theta):
        theta = float(theta)
    m = input("What is the mass of the object/person in this problem: ")
    if number(m):
        m = float(m)
    a = input("What is the acceleration of the mass up the incline plane: ")
    if number(a):
        a = float(a)
    unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
    wow = True
    while wow:
        if unknown == 'F':
            if (type(m) == float and type(theta) == float and type(a) == float): 
                F = m*a - m * 9.8 * math.sin(theta)
                print(F)
                wow = False
            elif (type(N) == float and type(theta) == float and type(a) == float and type(N) == float):
                F = N * math.tan(theta) - m*a
                print(F)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'N':
            if (type(m) == float and type(theta) == float): 
                N = m * 9.8 * math.cos(theta)
                print(F)
                wow = False
            elif (type(F) == float and type(theta) == float and type(a) == float and type(m) == float):
                N = ((F + m*a)/math.sin(theta)) * math.cos(theta)
                print(N)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'Fg':
            if (type(m) == float and type(F) == float and type(theta) == float and type(a) == float):
                Fg = (F + m*a)/math.sin(theta)
                print(Fg)
                wow = False
            elif (type(N) == float and type(theta) == float):
                Fg = N/math.cos(theta)
                print(N)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'theta':
            if (type(N) == float and type(m)): 
                theta = np.arccos(N/(m * 9.8)) 
                print(theta)
                wow = False
            elif (type(F) == float and type(N) == float and type(m) == float and type(a) == float):
                theta = np.arctan((m*a+F)/N)
                print(theta)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'm':
            if (type(N) == float and type(theta) == float): 
                m = N/(9.8 * math.cos(theta))
                print(m)
                wow = False
            elif (type(F) == float and type(theta) == float):
                m = F/(9.8*math.sin(theta) - a)
                print(m)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
if accelerating == 'down':
    F = input("What is the external force acting in the mass in this problem: ")
    if number(F):
        F = float(F)    
    N = input("What is the normal force acting on the mass in this problem: ")
    if number(N):
        N = float(N)
    Fg = input("What is the force due to gravity on the mass in this problem: ")
    if number(Fg):
        Fg = float(Fg)
    theta = input("What is the angle of elevation of the incline in this problem: ")
    if number(theta):
        theta = float(theta)
    m = input("What is the mass of the object/person in this problem: ")
    if number(m):
        m = float(m)
    a = input("What is the acceleration of the mass down the incline plane: ")
    if number(a):
        a = float(a)
    unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
    wow = True
    while wow:
        if unknown == 'F':
            if (type(m) == float and type(theta) == float and type(a) == float): 
                F = m*a + m * 9.8 * math.sin(theta)
                print(F)
                wow = False
            elif (type(N) == float and type(theta) == float and type(a) == float and type(N) == float):
                F = N * math.tan(theta) + m*a
                print(F)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'N':
            if (type(m) == float and type(theta) == float): 
                N = m * 9.8 * math.cos(theta)
                print(F)
                wow = False
            elif (type(F) == float and type(theta) == float and type(a) == float and type(m) == float):
                N = ((F - m*a)/math.sin(theta)) * math.cos(theta)
                print(N)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'Fg':
            if (type(m) == float and type(F) == float and type(theta) == float and type(a) == float):
                Fg = (F - m*a)/math.sin(theta)
                print(Fg)
                wow = False
            elif (type(N) == float and type(theta) == float):
                Fg = N/math.cos(theta)
                print(N)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'theta':
            if (type(N) == float and type(m)): 
                theta = np.arccos(N/(m * 9.8)) 
                print(theta)
                wow = False
            elif (type(F) == float and type(N) == float and type(m) == float and type(a) == float):
                theta = np.arctan((m*a-F)/N)
                print(theta)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
        if unknown == 'm':
            if (type(N) == float and type(theta) == float): 
                m = N/(9.8 * math.cos(theta))
                print(m)
                wow = False
            elif (type(F) == float and type(theta) == float):
                m = F/(9.8*math.sin(theta)+ a)
                print(m)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (F, N, Fg, theta, m)?: ")
