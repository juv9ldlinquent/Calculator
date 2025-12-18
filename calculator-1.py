def inputHandling():
    userInput = input("Type in an operation. Eg. 2 + 3. Note that the only supported operators are +, -, /, *\n")
    operations = ['+', '-', '*', '/']

    # Handling input    
    for i in userInput:
        # Check for operator and assign operands
        if not any(op in userInput for op in operations):
            raise ValueError("Unsupported or absent operator.")


        elif i in operations:
            positionOfOperator = userInput.find(i)
            operand1 = float(userInput[0: positionOfOperator])
            operand2 = float(userInput[positionOfOperator + 1: len(userInput)])


        # Handle error with letters
        elif i.isalpha():
            raise ValueError("Invalid operation. Refer to above instructions")
    # assign operator       
    currentOperation = userInput[positionOfOperator]
    return operand1, operand2, currentOperation

def operation(operand1, operand2, currentOperation):
    # perform desired operation
    match currentOperation:
        case "+":
            return operand1 + operand2

        case "-":
           return operand1 - operand2

        case "*":
            return operand1 * operand2

        case "/":
            return operand1 / operand2

def calculator():
    # Flow control
    print("Welcome to my calculator!")
    while True:
        try:
            operand1, operand2, currentOperation = inputHandling()
            result = operation(operand1, operand2, currentOperation)
            print("Result:", result)
        except ValueError as e:
            print("Error:", e)
        # Allow user to enter another calculation
        try:
            continueOrNot = input("Do you want to continue calculating? (Y/N) > ")
            if continueOrNot.upper() == "Y":
                continue
            elif continueOrNot.upper() == "N":
                print("Okay, goodbye.")
                break
            else:
                raise ValueError("I don't understand", continueOrNot)
                continue
        except ValueError as e:
            print("Error:", e)

calculator()