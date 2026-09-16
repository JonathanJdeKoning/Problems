class Bank:

    def __init__(self, balance: List[int]):
        self.arr = [-1] + balance
        self.n = len(balance)


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in range(1, self.n+1): return False
        if account2 not in range(1, self.n+1): return False
        if self.arr[account1] < money: return False
        self.arr[account1] -= money
        self.arr[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account not in range(1, self.n+1): return False
        self.arr[account] += money 
        return True       

    def withdraw(self, account: int, money: int) -> bool:
        if account not in range(1, self.n+1): return False
        if self.arr[account] < money: return False
        self.arr[account] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)