class Employee:
    raise_am=1.3
    def __init__(self, first, last,pay):
        self.first = first
        self.last = last
        self.email=first+'.'+last+'@gmail.com'
        self.pay = pay
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def amt(self):
        self.pay=int(self.pay+self.raise_amt)

    def __str__(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return '{}-{}'.format(self.first, self.last)
    def __add__(self,other):
        return self.pay+self.other
    def __len__(self):
        return len(self.full_name())
empl=Employee('HIma','He',3)
emple=Employee('Manu','sre',4)
print(repr(empl)) 
print(str(emple))
print(len(emple))
