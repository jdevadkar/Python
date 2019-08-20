# simple class with init method
class Person:
    # init method
    def __init__(self,name):
        self._name =name
    # Sample method
    def say_hi(self):
        print("Hi My Name is "+ self._name)
# Object Creation
p = Person("Ram")
p.say_hi()