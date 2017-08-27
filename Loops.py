a=1
s=0
names= ["Zohaib","Hasan","Nizami","Python","Programming"]
print("Start Program?")
r=input("Press 1/0:")
while r !=0 :
    print("Press 1 for FOR Loop")
    print("Press 2 for WHILE Loop")

    loopname = int(input())
    if loopname==1:
            print("Executing FOR Loop ")
            for N in names:
                if N=="Zohaib":
                    print(N,"0")
                elif N=="Hasan":
                    print(N,"1")
                elif N=="Nizami":
                    print(N,"2")
                elif N=="Python":
                    print(N,"3")
                elif N=="Programming":
                    print(N,"4")
    elif loopname==2:
       print("Executing WHILE Loop ")
       while a!=0:
            print("The current sum the values is:",s)
            a=float(input("Enter a value or press 0 to quit:"))
            s+=a
      
    else:
        print("Incorrect input!")
    print("Do you want to perform another operation?")
    r=input("Press 1 for Yess and 0 for No ")

