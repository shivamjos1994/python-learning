class Addition:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def sub(self):
        if self.a > self.b:
            return self.a-self.b
        else:
            return self.b-self.a



class Maximum:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def max(self):
        if self.a > self.b:
            return self.a
        else:
            return self.b
