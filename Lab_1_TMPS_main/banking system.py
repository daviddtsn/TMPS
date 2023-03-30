class Account:
    def init(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance


class AccountRepository:
    def init(self):
        self.accounts = {}

    def add_account(self, account: Account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number: str):
        return self.accounts.get(account_number)


class AccountService:
    def init(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def create_account(self, account_number: str):
        account = Account(account_number)
        self.account_repository.add_account(account)

    def deposit(self, account_number: str, amount: float):
        account = self.account_repository.get_account(account_number)
        if account is None:
            raise ValueError("Account not found")
        account.deposit(amount)

    def withdraw(self, account_number: str, amount: float):
        account = self.account_repository.get_account(account_number)
        if account is None:
            raise ValueError("Account not found")
        account.withdraw(amount)

    def get_balance(self, account_number: str):
        account = self.account_repository.get_account(account_number)
        if account is None:
            raise ValueError("Account not found")
        return account.get_balance()