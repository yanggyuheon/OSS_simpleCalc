# Program make a simple calculator

import op
import log

normal_logger = log.make_logger('normal') # normal_logger 생성
error_logger = log.make_logger('error') # error_logger 생성

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
        
        # 숫자 입력받을 때 문자열 들어오는 것 예외 처리
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break
            except: # 예외 발생할 경우 실행
                print("Invalid Input. Please enter a number")
                error_logger.info("Invalid Input. Please enter a number")
            

        if choice == '1':
            print(num1, "+", num2, "=", op.add(num1, num2))
            normal_logger.info(f"{num1} + {num2} = {op.add(num1, num2)}")

        elif choice == '2':
            print(num1, "-", num2, "=", op.subtract(num1, num2))
            normal_logger.info(f"{num1} - {num2} = {op.subtract(num1, num2)}")

        elif choice == '3':
            print(num1, "*", num2, "=", op.multiply(num1, num2))
            normal_logger.info(f"{num1} * {num2} = {op.multiply(num1, num2)}")

        else:
            if num2 == 0:
                print("Divison by zero isn't possible")
                error_logger.info("Division by zero isn't possible")

            else:
                print(num1, "/", num2, "=", op.divide(num1, num2))
                normal_logger.info(f"{num1} / {num2} = {op.divide(num1, num2)}")

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
        print("Invalid Input. Please enter (1/2/3/4)")
        error_logger.info("Invalid Input. Please enter (1/2/3/4)")


