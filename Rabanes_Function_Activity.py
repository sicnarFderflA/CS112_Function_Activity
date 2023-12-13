
def same3(num1, num2, num3):
    ans = num1 * num2 * num3
    print(f"Result is {ans}")
    
def same12(num1 , num2, num3):
    ans = (num1 * num2) + num3
    print(f"Result is {ans}")

def same13(num1 , num2, num3):
    ans = (num1 * num3) + num2
    print(f"Result is {ans}")

def same23(num1 , num2, num3):
    ans = (num2 * num3) + num1
    print(f"Result is {ans}")

def notsame(num1, num2, num3):
    ans = num1 + num2 + num3
    print(f"Result is {ans}")


while True:
    print("Enter [0] to end the program.")
    num1 = int(input("Enter Number 1: "))
    if num1 == 0:
        print("Program Terminated")
        break
    else:
        check1 = True
    num2 = int(input("Enter Number 2: "))
    if num2 == 0:
        print("Program Terminated")
        break
    else:
        check2 = True
    num3 = int(input("Enter Number 3: "))
    if num3 == 0:
        print("Program Terminated")
        break
    else:
        check3 = True
  

    if check1 and check2 and check3 == True:
        if num1 == num2 == num3:
            same3(num1, num2, num3)

        elif num1 == num2:
            same12(num1,num2,num3)

        elif num1 == num3:
            same13(num1 , num2, num3)    

        elif num2 == num3:
            same23(num1 , num2, num3)

        else:
            notsame(num1,num2,num3)

    
