# Created Class
class StaticMethod1:
    # define variable
    name ='StaticMethod1'
    # Static method
    @classmethod
    def static(cls):
        print("% static () called ", cls.name)

# Created Class and inherited StaticMethod class
class StaticMethod2(StaticMethod1):
    # Define variable
    name = 'StaticMethod2'

# Created Class and inherited StaticMethod class
class StaticMethod3(StaticMethod1):
    # Define variable
    name ='StaticMethod3'

    #Satic method
    @classmethod
    def static(cls):
        print("% static() called ", cls.name)

# Called static Methods
StaticMethod1.static()
StaticMethod2.static()
StaticMethod3.static()