

class SavingAccount:
    pass


class CheckingAccount:
    pass


class BankAccount(SavingAccount, CheckingAccount):
    pass


class Stock:
    pass


class Bond:
    pass


class Security(Stock, Bond):
    pass


class Asset(BankAccount, Security, RealEstate):
    pass


class InterestBearingItem(BankAccount, Security):
    pass


class RealEstate:
    pass


class InsurableItem(RealEstate, BankAccount):
    pass


