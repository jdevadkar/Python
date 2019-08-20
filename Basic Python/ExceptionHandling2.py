# else cluase
def division(a,b):
    try:
        c =((a + b)/(a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
division(2,3)
division(3,3)