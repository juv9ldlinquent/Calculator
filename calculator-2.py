def handle_input():
    supported_operators = ["+", "-", "*", "/"]
    userInput = input("""Type in a calculation.
    Eg. 2 + 3. Note that the supported operators are +, -, *, /. \n""")
    userInput = userInput.strip()
    for i in userInput:
        if i in supported_operators:
            currentOperation = i          
            operand1 = float(userInput[0: userInput.find(i)])
            operand2 = float(userInput[(userInput.find(i) + 1): len(userInput)])
        if not any(i in supported_operators for i in userInput):
            raise ValueError("Absent or unsupported operator!")  
            continue
        if i.isalpha():
            raise ValueError("You shouldn't have letters in your operation!")
            continue

    return operand1, operand2, currentOperation

def compute(operand1, operand2, currentOperation):
    match currentOperation:
        case "+":
            result = operand1 + operand2
            print("Result:", result)
        case "-":
            result = operand1 - operand2
            print("Result:", result)
        case "*":
            result = operand1 * operand2
            print("Result:", result)
        case "/":
            result = operand1 / operand2  
            print("Result:", result)   

def calculator():
    while True:
        try:
            print("Welcome to my calculator.")
            operand1, operand2, currentOperation = handle_input()
            compute(operand1, operand2, currentOperation)
            
            continueOrNot = input("Do you want to continue calculating? (Y/N)\n")
            if continueOrNot.upper() == "Y":
                continue
            elif continueOrNot.upper() == "N":
                print("Okay, goodbye!")
                break
            else:
                raise ValueError("I don't understand", continueOrNot)

        except ValueError as e:
            print("Error:", e)

calculator()