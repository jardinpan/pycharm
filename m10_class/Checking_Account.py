from m10_class.Account_init_str import Account

class CheckingAccount(Account):
    def __init__(self, number, name, balance, credit_limit = 10000):
        super(CheckingAccount, self).__init__(number, name, balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        try:
            if amount <= self.balance + self.credit_limit:
                self.balance -= amount
            else:
                raise ValueError
        except ValueError:
            print('超過信用額度')

    def __str__(self):
        return (super(CheckingAccount, self).__str__() + ', credit limit:{0}'.format(self.credit_limit))

def main():
    ca = CheckingAccount('1227', 'Maaya', 721)
    ca.deposit(987)
    print(ca.balance)
    ca.withdraw(7000)
    print(ca.balance)
    print(ca, end='\n\n')

    ca1 = CheckingAccount('1227', 'Maaya', 721, 8000)
    ca1.deposit(279)
    print(ca1.balance)
    ca1.withdraw(9000)
    print(ca1.balance)
    print(ca1)

if __name__ == '__main__':  # 確保被其他import時也不會執行main()
    main()