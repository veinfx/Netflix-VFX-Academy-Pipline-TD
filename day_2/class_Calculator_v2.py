class Calculator():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        return self.first + self.second

call = Calculator(3, 5)
print(call.sum())