class Bank:
    """
    n accounts, numbered 1 to n
    init bal is stored in balance

    execute all valid transactions. valid if
    acc numbers b/t [1, n]
    amount transferred <= bal of account
    """

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.num_accounts = len(balance)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """
        Transfers money dollars from the account numbered account1 to the account numbered account2.
        Return true if the transaction was successful, false otherwise.
        """
        if self.withdraw(account1, money):
            if self.deposit(account2, money):
                return True
            self.deposit(account1, money) # give money back to account1 if deposit fails
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        """
        Deposit money into account, return true if success, false otherwise
        """
        if account < 1 or account > self.num_accounts:
            return False
        self.balance[account - 1] += money
        return True

        

    def withdraw(self, account: int, money: int) -> bool:
        """
        withdraw money from acc, return t if success
        """
        if account < 1 or account > self.num_accounts:
            return False
        if self.balance[account - 1] < money:
            return False

        self.balance[account - 1] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
