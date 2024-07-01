# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print(f"-------------------------------------------------------")
    print(f"Please provide details below for your SAVINGS account")
    #Looping till users enter a valid value
    while True:
        savings_balance = input("What is your account balance?\n")
        if is_float(savings_balance):
            #convert string to a float
            savings_balance = float(savings_balance)
            break
        else:
            print("You have entered a non numeric value for balance. Please try again.")
            
    
    while True:
        savings_interest = input("What is the APR for the account?\n")
        if is_float(savings_interest):
            #convert string to a float
            savings_interest = float(savings_interest)
            #checking to see if APR is > 0 and less than 100
            if (savings_interest > 0) & (savings_interest < 100):
                break
            else:
                print("APR should be between 0 and 100. Please try again.")
        else:
            print("You have entered a non numeric value for APR. Please try again.")
            
    
    while True:
        savings_maturity = input("What is the number of months on the account?\n")
        if savings_maturity.isdigit():
            #convert str to int
            savings_maturity = int(savings_maturity)
            break
        else:
            print("You have entered an invalid number for number of months. Please try again.")
            

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
     print(f"-------------------------------------------------------")
    print(f"Savings Account details: ")
    print(f"-------------------------")
    print("Starting balance: $",format(savings_balance, ",.2f"))
    print("APR: ",format(savings_interest, ",.2f"),"%")
    print(f"Months for interest calculation: {savings_maturity}")
    print("Interest Earned: $",format(interest_earned, ",.2f"))
    print("Updated balance: $",format(updated_savings_balance, ",.2f"))
    print(f"-------------------------------------------------------")
    
    """Some print statements for readability"""
    print(f"")
    print(f"")


    print(f"-------------------------------------------------------")
    print(f"Please provide details below for your CD account")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # Looping till users enter a valid value
    while True:
        cd_balance = input("What is your account balance?\n")
        if is_float(cd_balance):
            #convert str to float
            cd_balance = float(cd_balance)
            break
        else:
            print("You have entered a non numeric value for balance. Please try again.")
        

    while True:
        cd_interest = input("What is the APR for the account?\n")
        if is_float(cd_interest):
            #convert str to float
            cd_interest = float(cd_interest)
            #checking to see if APR is > 0 and less than 100
            if (cd_interest > 0) & (cd_interest < 100):
                break
            else:
                print("APR should be between 0 and 100. Please try again.")
        else:
            print("You have entered a non numeric value for CD interest. Please try again")
        
    while True:
        cd_maturity = input("What is the number of months maturity on the CD\n")
        if cd_maturity.isdigit():
            #convert str to int
            cd_maturity = int(cd_maturity)
            break
        else:
            print("You have entered an invalid number for number of months maturity on CD. Please try again.")
           

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"CD Account details: ")
    print(f"-------------------------")
    print("Starting balance: $",format(cd_balance, ",.2f"))
    print("APR: ",format(cd_interest, ",.2f"),"%")
    print(f"CD maturity in terms of months: {cd_maturity}")
    print("Interest Earned: $",format(interest_earned, ",.2f"))
    print("Updated balance: $",format(updated_cd_balance, ",.2f"))
    print(f"-------------------------------------------------------")
  
if __name__ == "__main__":
    # Call the main function.
    main()
