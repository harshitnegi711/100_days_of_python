def Add(a,b):
    return a+b

def Sub(a,b):
    return a-b

def Mul(a,b):
    return a*b

def Div(a,b):
    return a/b

def Calculator():

    num1=float(input("enter the values : "))
    mood=False
    while mood is not True:
        operations={'+':Add,'-':Sub,'*':Mul,'/':Div}
        for symbol in operations:
            print(symbol)
        operation = input("choose an opreration from above :")

        num2=float(input("enter the value : "))

        calculation_function=operations[operation]
        answer=calculation_function(num1,num2)
        print(f"{num1}{operation}{num2}={answer}")
        i=input("press '1' to continue with the answer and '0' to exit and '2' for next calculation : ")
        if i=='1':
           num1=answer
        elif i=='2':
            Calculator()
        else:
            mood=True


Calculator()