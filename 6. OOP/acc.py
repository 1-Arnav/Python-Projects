class Account:

    def __init__(self, file_path):
        self.filepath = file_path
        with open(file_path, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    
    def __init__(self, file_path, fee) -> None:
        Account.__init__(self, file_path)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

checking = Checking("balance.txt", 1)
checking.transfer(10)
print(checking.balance)
checking.commit()