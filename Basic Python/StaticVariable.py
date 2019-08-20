# Created Class
class StaticExample:
    #static variable
    static_variable =5

# Access through class  
print(StaticExample.static_variable)

# access through an instance 
instance =StaticExample()
print(instance.static_variable)

# change with an instance
instance.static_variable =6
print(instance.static_variable)
print(StaticExample.static_variable)

# change through Class
StaticExample.static_variable =7
print(instance.static_variable)
print(StaticExample.static_variable)
