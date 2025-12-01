def calculator():
    print("Welcome to my calculator!")
    userInput = input("Type in an operation.\n")
    operation = ['+', '-', '*', '/']
    #Determine operation 
       
    try:
        if "+" in userInput:
            userInput = userInput.strip()
            positionOfPlusSign = userInput.find("+")
            addend = float(userInput[0: positionOfPlusSign])
            adder = float(userInput[positionOfPlusSign + 1: len(userInput)])
            print(addend, adder)
            total = addend + adder
            print(total)

        elif "-" in userInput:
            userInput = userInput.strip()
            positionOfMinusSign = userInput.find("-")           
            sub1 = float(userInput[0: positionOfMinusSign])
            sub2 = float(userInput[positionOfMinusSign + 1: len(userInput)])
            diff = sub1 - sub2
            print(diff)

        elif "*" in userInput:
            userInput = userInput.strip()
            positionOfTimesSign = userInput.find("*")           
            multiplicand = float(userInput[0: positionOfTimesSign])
            multiplier = float(userInput[positionOfTimesSign + 1: len(userInput)])
            prod = multiplicand * multiplier
            print(prod)

        elif "/" in userInput:
            userInput = userInput.strip()
            positionOfOverSign = userInput.find("/")           
            dividend = float(userInput[0: positionOfOverSign])
            divisor = float(userInput[positionOfOverSign + 1: len(userInput)])
            quot = dividend / divisor
            if divisor == 0:
                raise ZeroDivisionError("Infinite Result")
            else:
                print(quot)

        for i in userInput:
            if i.isalpha() == True:
                raise ValueError
        
        else:
            raise ValueError("Absent or unsupported operator.")

    except ValueError:
        print("Enter a valid input.")

calculator()

