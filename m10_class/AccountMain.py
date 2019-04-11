from m10_class.Account_init_str import Account
from m10_class.Checking_Account import CheckingAccount

def main():
    acc = Account('1515', 'LiSA')
    acc.deposit(50)
    print(acc.balance)
    acc.withdraw(51)
    print(acc.balance)
    print(acc, end = '\n\n')

    acc1 = Account('1515', 'LiSA', 624)
    acc1.deposit(68)
    print(acc1.balance)
    acc1.withdraw(800)
    print(acc1.balance)
    print(acc1, end = '\n\n')

    ca = CheckingAccount('1227', 'Maaya', 721)
    ca.deposit(987)
    print(ca.balance)
    ca.withdraw(7000)
    print(ca.balance)
    print(ca, end = '\n\n')

    ca1 = CheckingAccount('1227', 'Maaya', 721, 8000)
    ca1.deposit(279)
    print(ca1.balance)
    ca1.withdraw(9000)
    print(ca1.balance)
    print(ca1)

main()