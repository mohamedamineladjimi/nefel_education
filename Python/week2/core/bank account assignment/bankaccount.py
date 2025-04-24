class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit (self,amount):
        self.balance += amount
        return self
    def withdraw (self,amount):
        if(self.balance - amount )>=0:
            self.balance -= amount
        else:
            print("Insufficient Funds:charging a fee of 5$ ")
            self.balance -= 5
            return self
    def display_account_info(self):
            print(f"Balance:{self.balance}")
            return self
    def yeild_interest(self):
            if self.balance > 0:
                self.balance += (self.balance * self.int_rate)
            return self
savings= BankAccount(.05,1000)
checking =BankAccount(.02,5000)

savings.deposit(60).deposit(10).deposit(10).withdraw(400).yeild_interest().display_account_info()

            

            