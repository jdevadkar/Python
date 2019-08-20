# parent class
class Parent:
    #Hidden Variable No access to outside class
    __variable =10

    # parent class init method
    def __init__(self):
        print("Parent __init__ method" ,self.__variable)
    # parent class method
    def parentFunction(self):
        print("Parent Function" ,self.__variable)
# parent class object creation and called parent method
p=Parent()
p.parentFunction()

# child class inherited by parent class
class child(Parent):
    #child class init method
    def __init__(self):
        print("child __init__ method",self.__variable )
    # child class method
    def childFunction(self):
        print("child function",self.__variable)
# child class object creation
c = child()
c.childFunction()
# child class called parent class method
c.parentFunction()