class Calculator():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        return self.first + self.second

call = Calculator(3, 5)
print(call.sum())

class Super_cal(Calculator):
    def minus(self):
        return self.first - self.second
    
    def sum(self):
        return self.first + self.second + 2

call_2 = Super_cal(2,3)
print(call_2.minus())

print(call_2.sum())