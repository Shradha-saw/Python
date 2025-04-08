num1 = int(input("enter num1 :"))
num2 = int(input("enter num2 :"))
choice = input("Enter choic add-1, and sub-1, mul-3, div-4, squareofnumer-5, remainder-6, Floor-division-7")
if choice == '1':
    print("Addition is:",num1 +num2)
elif choice == '2':
    print("Substrction is:", num1 - num2)
elif choice == '3':
    print("multiplication is:", num1 * num2)
elif choice =='4':
    print("Division is: ", num1 / num2) 
elif choice == '5':
    print("Square of num1 is : ",num1 ** 2)
    print("Square of num2 is: ",num2 ** 2)
elif choice == '6':
    print("Remainder is: ", num1 % num2)     
elif choice == '7':
    print("Floor Division is: ", num1 // num2)       
else:
    print("Invalid Choice....!")               