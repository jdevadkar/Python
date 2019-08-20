#To handle simple runtime Error
a =[1,3,4]
try:
    print("Second element:",a[1])
    print("Forth Element :",a[3])
except IndexError:
    print("List index Out of bound")