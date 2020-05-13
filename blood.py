hospital=[]
detail=[]
raree=[]
rare=[]
print('Are you a Admin or User')
x=input('Enter :')
if(x== 'Admin'):
    n = int(input('Enter number of hospitals u want to add: '))
    for i in range (0,n):
     k = input('Enter name of hospitals u want to add:')
     hospital.append(k)

elif(x== 'User'):
    y=input('Do u want to register or request or view as Admin:' )
    if(y== 'register'):
         v= int(input('How many peoples blood u want to register: '))
         for j in range (0,v):
            name=input('Enter your name')
            bloodtype=input('Enter your bloodtype:' )
            mix= name + bloodtype
            detail.append(mix)
            continue
    elif(y== 'request'):
            search=input('Which blood group are you looking for :')
            type=input('Enter :')
            if(search=='AB+'):
                 print(name)
            if(search=='AB-'):
                 print(name)
            if(search=='B+'):
                 print(name)
            if(search=='B-'):
                 print(name)
            if(search=='O+'):
                 print(name)
            if(search=='O-'):
                 print(name)
b=input('R u looking for rare bloodgroup: ')
if(b=='yes'):
     q=input('Enter bloodgroup:')
     if(q=='AB+'):
        print(name)
     if(q=='AB-'):
         print(name)

    


 

if(x== 'Admin'):
    n = int(input('Enter number of hospitals u want to add: '))
    for i in range (0,n):
     k = input('Enter name of hospitals u want to add:')
     hospital.append(k)
elif(x== 'User'):
    y=input('Do u want to register or request:' )
    if(y== 'register'):
         v= int(input('How many peoples blood u want to register: '))
         for j in range (0,v):
             name=input('Enter your name')
             
             bloodtype=input('Enter your bloodtype:' )
             mix= name + bloodtype
             detail.append(mix)
             continue
                   
    elif(y== 'request'):
            search=input('Which blood group are you looking for :')
            if(search=='AB+'):
                 print(name)
            if(search=='AB-'):
                 print(name)
            if(search=='B+'):
                 print(name)
            if(search=='B-'):
                 print(name)
            if(search=='O+'):
                 print(name)
            if(search=='O-'):
                 print(name)

t=input('Do you want to view data as admin:')
if(t=='yes'):
     print(detail)
print(hospital)