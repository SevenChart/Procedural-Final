import math
def KE(m, v):
    return (m * v**2)/2
def number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
hmmm = ['IE', 'E']
cat = True
let = ['m1','m2','V1','V2','V3','Vo1','Vo2']
while cat:
    IEvE = input("Is the collision elastic or inelastic(IE or E): ")
    if IEvE in hmmm:
        break
    else:
        IEvE = input("Is the collision elastic or inelastic(IE or E): ")
if IEvE == 'IE':
    m1 = input("What is the mass of the first object/person in this problem: ")
    if number(m1):
        m1 = float(m1)    
    m2 = input("What is the mass of the second object/person in this problem: ")
    if number(m2):
        m2 = float(m2)
    V1 = input("What is the initial velocity of the first mass in this problem: ")
    if number(V1):
        V1 = float(V1)
    V2 = input("What is the initial velocity of second mass in this problem: ")
    if number(V2):
        V2 = float(V2)
    V3 = input("What is the final velocity of both masses in this problem: ")
    if number(V3):
        V3 = float(V3)
    unknown = input("What do you want to solve for (m1, m2, V1, V2, V3)?: ")
    wow = True
    while wow:
        if unknown not in let:
            print("We don't have the facilities for that mate")
            unknown = input("What do you want to solve for (m1, m2, V1, V2, V3)?: ")
        if unknown == 'V3':
            if (type(m1) == float and type(m2) == float and type(V1) == float and type(V2) == float): 
                V3 = (m1*V1 + m2*V2)/(m1 + m2)
                print(V3)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, V3)?: ")
        if unknown == 'V1':
            if (type(m1) == float and type(m2) == float and type(V1) == float and type(V3) == float): 
                V1 = (V3 * (m1 + m2) - m2*V2)/m1
                print(V1)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, V3)?: ")
        if unknown == 'V2':
            if (type(m1) == float and type(m2) == float and type(V1) == float and type(V3) == float): 
                V2= (V3 * (m1 + m2) - m1*V1)/m2
                print(V2)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, V3)?: ")
        if unknown == 'm1':
            if (type(V2) == float and type(m2) == float and type(V1) == float and type(V3) == float): 
                m1 = (m2*(V3 - V2))/(V1 - V3) 
                print(m1)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, V3)?: ")
        if unknown == 'm2':
            if (type(m1) == float and type(m2) == float and type(V1) == float and type(V3) == float): 
                m2 = (m1*(V3 - V1))/(V2 - V3) 
                print(m2)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, V3)?: ")
if IEvE == 'E':
    m1 = input("What is the mass of the first object/person in this problem: ")
    if number(m1):
        m1 = float(m1)    
    m2 = input("What is mass of the second object/person this problem: ")
    if number(m2):
        m2 = float(m2)
    Vo1 = input("What is the initial velocity of the first object in this problem: ")
    if number(Vo1):
        Vo1 = float(Vo1)
    Vo2 = input("What is the inital velocity of the second mass in this problem: ")
    if number(Vo2):
        Vo2 = float(Vo2)
    V1 = input("What is the final velocity of the first mass in this problem: ")
    if number(V1):
        V1 = float(V1)
    V2 = input("What is the final velocity of the second mass in this problem: ")
    if number(V2):
        V2 = float(V2)
    unknown = input("What do you want to solve for (m1, m2, V1, V2, Vo1, Vo2)?: ")
    wow = True
    while wow:
        if unknown not in let:
            print("We don't have the facilities for that mate")
            unknown = input("What do you want to solve for (m1, m2, V1, V2, Vo1, Vo2)?: ")
        if unknown == 'm1':
            if (type(Vo1) == float and type(m2) == float and type(Vo2) == float and type(V2) == float and type(V1) == float): 
                m1 = (m2*(V2 - Vo2))/(Vo1-V1)
                print(m1)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, Vo1, Vo2)?: ")
        if unknown == 'm2':
            if (type(Vo1) == float and type(m1) == float and type(Vo2) == float and type(V2) == float and type(V1) == float): 
                m2 = (m1*(V1 - Vo1))/(Vo2-V2)
                print(m2)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, Vo1, Vo2)?: ")
        if unknown == 'Vo1':
            if (type(m2) == float and type(m1) == float and type(Vo2) == float and type(V2) == float and type(V1) == float): 
                Vo1 = (m1*V1 + m2*V2 - m2*Vo2)/m1
                print(Vo1)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, Vo1, Vo2)?: ")
        if unknown == 'Vo2':
            if (type(m2) == float and type(m1) == float and type(Vo1) == float and type(V2) == float and type(V1) == float): 
                Vo2 = (m1*V1 + m2*V2 - m1*Vo1)/m2
                print(Vo2)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, Vo1, Vo2)?: ")
        if unknown == 'V1':
            if (type(m2) == float and type(m1) == float and type(Vo1) == float and type(V2) == float and type(Vo2) == float): 
                V1 = (m1*Vo1 + m2*Vo2 - m2*Vo2)/m1
                print(V1)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, Vo1, Vo2)?: ")
        if unknown == 'V2':
            if (type(m2) == float and type(m1) == float and type(Vo1) == float and type(V1) == float and type(Vo2) == float): 
                V2 = (m1*Vo1 + m2*Vo2 - m1*Vo1)/m2
                print(V2)
                wow = False
            else:
                print("You don't quite have the facilites for that mate")
                unknown = input("What do you want to solve for (m1, m2, V1, V2, Vo1, Vo2)?: ")
    if (KE(m1, Vo1) + KE(m2, Vo2) == KE(m1, V1) + KE(m2, V2)):
        print("This collision is perfectly elastic")
    else:
        print("This collision is NOT perfectly elastic")
