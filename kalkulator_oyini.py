import random
new=['+','-','//','*']
s,k=0,0
l=0
while True:
    s1=random.randint(1,10)
    s2=random.randint(1,10)
    amal=random.choice(new)
    if amal=='+':
        ans=s1+s2
    elif amal=='-':
        ans=s1-s2
    elif amal=='//':
        ans=s1//s2
    elif amal=='*':
        ans=s1*s2
    print(f"{s1}{amal}{s2}")
    l+=1
    user=input()
    if user=='stop':
        break
    if int(user)==ans:
        s+=1
    else:
        k+=1
    if s==5 or k==5:
        if s>k:
            print('siz g\'olib bo\'ldingiz')
            print(f'{l} tadan {s} tasini topdingiz')
        else:
            print('siz mag\'olib bo\'ldingiz')
            print(f"Siz {k} ta xato urunish qildingiz")
        break