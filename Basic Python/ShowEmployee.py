# This method Showed single Employee
from Dictionary import dict
import logging

def show_employee():
    try:
        logging.info("Checking dictionary is empty or not.")        
        if len(dict.keys()) == 0:
            logging.info("Nothing to Show")
        else:
            logging.info("Getting details.")
            # Exception Handling for name or validation
            try:
                name =str(input("Enter Name :"))
            except (ValueError,NameError):
                print("please type in a String")
            emp=dict.get(name, "Not Found")
            print(emp)
    except TypeError:
        logging.info("Type error occurred and Handled")