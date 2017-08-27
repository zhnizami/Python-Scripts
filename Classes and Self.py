print("Classes and Self")
print("Calculator")
                                                                        #Second Class#
class Calculator:
    def __init__(self):#Constructor Definition
        print("Second Class is created successfully!")
    def setValues(self,num1,num2): #Assign values Method
        self.num1=num1
        self.num2=num2
    def AddMethod(self):
        add= self.num1 + self.num2
        print( "The answer is=",str(add))
        print ("Successfully Added!")

    def SubMethod(self):
        print("The answer is=",str(self.num1-self.num2))
        print("Successfully Subracted!")
        
    def MulMethod(self):
        mul = self.num1 * self.num2
        print("The answer is=",str(mul))
        print("Successfully Multiplied!")

    def DivMethod(self):
        print("The answer is=",str(self.num1/self.num2))
        print("Successfully Divided!")
        
    def __del__(self):
        print("Class object destroyed!")
                                                                    #Second Class END Here#

                                                                    #This is the MAIN Class!#
calclass= Calculator()
r=1;    
while r!=0:
    n1=int(input("Enter the first value:"))
    n2=int(input("Enter the second value:"))
    calclass.setValues(n1,n2)
    print("Press 1 for Addition")
    print("Press 2 for Subraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    rq= int(input())
    if rq==1:
        calclass.AddMethod()
    elif rq==2:
        calclass.SubMethod()
    elif rq==3:
        calclass.MulMethod()
    elif rq==4:
        calclass.DivMethod()
    else:
        print("Invalid Operator!")
    r=int(input("Do you want to perform another calculation? 1/0"))
calclass.__del__()
print("Program Ended!")
                                                                 #Main Class END Here!#

