# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide (x,y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        else:
            if num2 == 0:
                print("Divison by zero isn't possible")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))

        loop_break = False # loop_break_1번째 체크
        loop_break2 = False # loop_break_2번째 체크

        while True:
            # input값 lower()로 소문자처리
            next_calculation = input("Let's do next calculation? (yes/no): ").lower()
            if next_calculation == "no":
                
                # loop break 이중 확인
                while True:
                    loop_out_check = input("Are you sure? (yes/no): ").lower()
                    
                    if loop_out_check == "yes":
                        loop_break2 = True
                        loop_break = True
                        break

                    elif loop_out_check == "no":
                        loop_break2 = True
                        break

                    else: # yes/no 이외의 값
                        print("Invalid Input. Please enter (yes/no)")

            elif next_calculation == "yes":
                break

            else: # yes/no 이외의 값
                print("Invalid Input. Please enter (yes/no)")
            
            # break Are you sure? 입력값 yes/no인 경우 
            if loop_break2 == True: 
                break

        # Let's do next calculation 입력값 no인 경우
        if loop_break == True:
            break

    else:
        print("Invalid Input")


