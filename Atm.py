# ATM SIMULATOR

print("please insert the card")
balance= 1000
user_pin= "1234"
entered_pin=input("please enter the pin:")
if entered_pin!=user_pin:
    print("invalid PIN Exiting")
    atm_on=False
else:
    atm_on=True

while atm_on:
    print("main menu")
    print("1.Check balance")
    print("2.Deposit money")
    print("3.withdraw money")
    print("4.exit")
    choice=input("enter ypour choice:")
    if choice == "1":
        print("your current balance is $" + str(balance))
    elif choice == "2":
        amount=float(input("enter the amount of deposit:$"))
        balance += amount
        print('$' + str(amount)+"deposited successfully")
    elif choice=="3":
        amount=float(input("enter the amount of withdraw:$"))
        if amount>balance:
            print("insufficient balance")
        else:
            balance-=amount
            print("$"+str(amount)+"withdrawl successfully")
    elif choice == "4":
        print("Thank You for using the ATM, Good Bye")
        atm_on = False
    else:
        print("Invalid choice, please try again.")    
