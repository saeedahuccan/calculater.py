#------simple calculator app-----
print("Select operation")
print("1. Add")
print("2.  subtract")
print("3. multiply")
print("4.  Divide")
print("5. mudulo")
print("6. power")

choiceOperator = input("Enter your choice of operator 1/2/3/4/5/6: ")


firstNumber = int(input("Enter first Number : "))

secondNumber = int(input("Enter second Number : "))
if choiceOperator =="1":
    print("Result : " ,firstNumber + secondNumber)
elif choiceOperator =="2":
    print("Result : " ,firstNumber - secondNumber)
elif choiceOperator =="3":
    print("Result : " ,firstNumber * secondNumber)
elif choiceOperator =="4":
    print("Result : " ,firstNumber / secondNumber)
elif choiceOperator =="6":
    if secondNumber == 0:
        print("Error cant divide by 0 ")
    else:
        print("Result : " ,firstNumber % secondNumber)
elif choiceOperator =="6":
    print("Result : " ,firstNumber ** secondNumber)
else:
    print("invalid input ")    
            
            
            
                
    

