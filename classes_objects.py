# creating a class

class example:
    def __init__(self, par_1, par_2): #constructor, where "self" refers to the own class
        self.par_1 = par_1
        self.par_2 = par_2
    def method(self): #method example
        print(self.par_1)
        print(self.par_2)

#creating a object

a = example(1, 2) 
a.method() #executing method
del a.par_1 #deleting par_1 (we can also delete the object)

#creating a class with no attributes or methods

class another_example:
    pass

#inheritance

class child_of_example(example):
    pass

b = child_of_example(1, 2)
b.method()



