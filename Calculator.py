from idlelib.debugger_r import restart_subprocess_debugger
from time import process_time

number1=input("Enter Number 1: ")
number2=input("Enter Number 2: ")
operator=input("A: Add; S:Sub; M:Multiply; D: Divide: ")
if operator=="A":
    result=float(number1)+ float(number2)
    print(f"Addition of {number1} amd {number2} is " + str(result))
elif operator=="S":
    result = float(number1) - float(number2)
    print(f"Subtraction of {number1} amd {number2} is " + str(result))
elif operator=="M":
    result = float(number1) * float(number2)
    print(f"Multiplication of {number1} amd {number2} is " + str(result))
elif operator=="D":
    result = float(number1) / float(number2)
    print(f"Division of {number1} amd {number2} is " + str(result))
else:
    print("Wrong Choice")
