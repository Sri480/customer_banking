""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods
    Interest here refers to interest earned, not the interest rate
    """
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # This method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

    #This method returns the balance on the account
    def get_balance():
        """Returns the balance on the Account"""
        return self.balance

    #This method retirms the interest earned on the account
    def get_interest():
        """Returns the interest earned on the Account"""
        return self.interest

 

"""CD_Account is a child class of parent class Account
CD_Account has the additional property of months, which is the maturity of the CD in terms of months
"""
class CD_Account(Account):
    """Constructor for CD_Account
    Interest here refers to interest earned, not the interest rate
    Months refers to the length or maturity of the CD in terms of months
    """
    def __init__(self,balance,interest, months):
        Account.__init__(self,balance,interest)
        self.months = months
    
    #This method sets the months attribute to the months passed in as a parameter
    def set_months(self, months):
        self.months = months

    #This method returns the length of the CD in terms of months
    def get_months(self):
        """Returns the length of the CD"""
        return self.months


