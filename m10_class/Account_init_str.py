class Account:
    def __init__(self, number, name, balance = 0):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError
            self.balance += amount
        except ValueError:
            print('金額必須是正整數')

    def withdraw(self, amount):
        try:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError
        except ValueError:
            print('餘額不足')
    def __str__(self):
        return ('number:{0}, name:{1}, balance:{2}'.format(self.number, self.name, self.balance))

def main():
    acc = Account('1515', 'LiSA')
    acc.deposit(50)
    print(acc.balance)
    acc.withdraw(51)
    print(acc.balance)
    print(acc, end='\n\n')

    acc1 = Account('1515', 'LiSA', 624)
    acc1.deposit(68)
    print(acc1.balance)
    acc1.withdraw(800)
    print(acc1.balance)
    print(acc1, end='\n\n')

if __name__ == '__main__': #確保被其他import時也不會執行main()
    main()