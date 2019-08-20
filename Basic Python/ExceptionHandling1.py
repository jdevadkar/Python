# TO handle multiple errors 
try:
    a = 3
    if a < 4 :
        # ZeroDivisionError occures
        b =a/(a-3)
    # NameError Occures
    print("value of b :",b)
# handle zerodivisionError or NameError
except (ZeroDivisionError , NameError):
    print("Error Occurred and Handled")