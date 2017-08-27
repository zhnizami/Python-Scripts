print("Funtions and Methods")
print("Calculator")
r=1;
def AddMethod(num1=0,num2=0):#giving default values so that null value exception may not occur!
    add= num1 + num2
    print( "The answer is=",str(add))
    print ("Successfully Added!")

def SubMethod(num1=0,num2=0): #giving default values so that null value exception may not occur!
    print("The answer is=",str(num1-num2))
    print("Successfully Subracted!")

def MulMethod(num1=0,num2=0):#giving default values so that null value exception may not occur!
    mul = num1 * num2
    print("The answer is=",str(mul))
    print("Successfully Multiplied!")

def DivMethod(num1=0,num2=0):#giving default values so that null value exception may not occur!
    print("The answer is=",str(num1/num2))
    print("Successfully Divided!")
    
while r!=0:
    n1=int(input("Enter the first value:"))
    n2=int(input("Enter the second value:"))
    print("Press 1 for Addition")
    print("Press 2 for Subraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    rq= int(input())
    if rq==1:
        AddMethod(n1,n2)
    elif rq==2:
        SubMethod(n1,n2)
    elif rq==3:
        MulMethod(n1,n2)
    elif rq==4:
        DivMethod(n1,n2)
    else:
        print("Invalid Operator!")
    r=int(input("Do you want to perform another calculation? 1/0"))


