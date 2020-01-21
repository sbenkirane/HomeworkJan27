inputCalc = str(input("Input your equation seperated by spaces: "))
splitCalc = inputCalc.split(" ", 3)

num1 = float(splitCalc[0])
math = str(splitCalc[1])
num2 = float(splitCalc[2])

if math == "+":
    calculation = float(num2+num1)
    print(calculation)
elif math == "-":
    calculation = float(num2-num1)
    print(calculation)
elif math == "*":
    calculation = float(num2*num1)
    print(calculation)
elif math == "/":
    calculation = float(num2/num1)
    print(calculation)