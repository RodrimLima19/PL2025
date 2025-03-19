class Exp:
    def __init__(self, type, exp1, op, exp2):
        self.type = type
        self.exp1 = exp1
        self.op = op
        self.exp2 = exp2

    def calc(self):
        if self.op == '+':
            return self.exp1.calc() + self.exp2.calc()
        elif self.op == '-':
            return self.exp1.calc() - self.exp2.calc()
        elif self.op == '*':
            return self.exp1.calc() * self.exp2.calc()
        elif self.op == '/':
            return self.exp1.calc() / self.exp2.calc()

class Num:
    def __init__(self, value):
        self.value = value

    def calc(self):
        return self.value
    


    
