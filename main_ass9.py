from operations_ass9 import MyMathModule,MyException

try:
    num = float(input("Enter a number: ")) 
    m = MyMathModule(num)



    if num == 0:
        raise MyException("Number cannot be zero")
    if num<0:
        raise MyException("Number cannot be negative")

    print("Enter Choice")
    opr=input("1.Square 2.Floor 3. Ceiling 4.Log 5.Factorial -> ")

    if opr=="1":
        print("Square:", m.square())


    elif opr=="2":
        print("Floor:", m.floor())


    elif opr=="3":
       print("Ceiling:",m.ceil())


    elif opr=="4":
        print("Logarithm:", m.logarithm())


    elif opr=="5":
        print("Factorial",m.factorial())

    else:
        print("Invalid Input")

except MyException as e: 
    print("Exception:", e.msg())