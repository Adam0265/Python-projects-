# credit card system  

class creditCard:
    def __init__(self,customer,account,bank,acnt,limit):
        self.customer = customer
        self.account = account
        self.bank = bank
        self.acnt = acnt #account identifier
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        return self.customer
    
    def get_bank(self):
        return self.bank
    
    def get_account(self):
        return self.account
    
    def get_limit(self):
        return self.limit
    
