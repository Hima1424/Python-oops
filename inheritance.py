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
class Std(Employee):
     raise_am=1.30
     def __init__(self, first, last,pay,prog_lang):
         super().__init__(first,last,pay)
         self.prog_lang=prog_lang
empl=Std('HIma','He',3,'python')
emple=Std('Manu','sre',4,'java')
#print(help(Std))
#print(empl.email)
#print(emple.email)\
#rint(empl.pay)
#empl.amt()
#print(empl.pay) 
print(Std.prog_lang)
