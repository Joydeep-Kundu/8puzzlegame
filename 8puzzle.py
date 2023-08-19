import random
l=[1,2,3,4,5,6,7,8,'']
m=[[],[],[]]
goal=[[1,2,3],[4,5,6],[7,8,'']]
# i=0
for i in range(3):
    for j in range(3):
        x=random.choice(l)
        m[i].append(x)
        l.remove(x)
# print(m)
loc=None
for n,i in enumerate(m):
    for o,j in enumerate(i):
        if j=='':
            loc=[n,o]
# print(loc)
c=0;
while 1:
    l=True
    for i in range(3):
        if goal[i]!=m[i]:
            l=False
    if l:  
        print(f'winner in {c} steps ')
        break
    for i in m:
        print(i)
    print()
    print('avilable moves x(for exit) ',end=' ')
    if loc[0]!=0:
        print('w(for up)',end=' ')
    if loc[0]!=2:
        print('s(for down)',end=' ')
    if loc[1]!=0:
        print('a(for left)', end=' ')
    if loc[1]!=2:
        print('d(for right)')
    print()
    inp=input("enter your move: ");
    if inp=='x':
        break
    if loc[0]!=0 and inp=='w':
        m[loc[0]][loc[1]],m[loc[0]-1][loc[1]]=m[loc[0]-1][loc[1]],m[loc[0]][loc[1]]
        loc[0]-=1
    if loc[0]!=2 and inp =='s':
        m[loc[0]][loc[1]],m[loc[0]+1][loc[1]]=m[loc[0]+1][loc[1]],m[loc[0]][loc[1]]
        loc[0]+=1
    if loc[1]!=0 and inp=='a':
        m[loc[0]][loc[1]-1],m[loc[0]][loc[1]]=m[loc[0]][loc[1]],m[loc[0]][loc[1]-1]
        loc[1]-=1
    if loc[1]!=2 and inp=='d':
        m[loc[0]][loc[1]+1],m[loc[0]][loc[1]]=m[loc[0]][loc[1]],m[loc[0]][loc[1]+1]
        loc[1]+=1
    c+=1
    