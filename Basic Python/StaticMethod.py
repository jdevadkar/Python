# Created Class
class StaticMethod:
    # define variable
    name ='Example'
    # Static method
    @staticmethod
    def static():
        print("% static () called ", StaticMethod.name)

# Created Class and inherited StaticMethod class
class StaticMethod1(StaticMethod):
    # Define variable
    name = 'StaticMethod1'

# Created Class and inherited StaticMethod class
class StaticMethod2(StaticMethod):
    # Define variable
    name ='StaticMethod2'

    #Sattic method
    @staticmethod
    def static():
        print("% static called ", StaticMethod2.name)

# Called static Methods
StaticMethod.static()
StaticMethod1.static()
StaticMethod2.static()