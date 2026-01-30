class bankaccount:
    def __init__(self, balance, fullmark):
        self.balance = balance
        self.fullmark = fullmark
        
    def __add__(self, other):
        self.balance += other.balance
        
    def __str__(self):
        return f"Balance: {self.balance}"


