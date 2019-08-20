from Employee import Employee
from Dictionary import dict
import datetime
import logging

# This Method Updated Employee in Dictionary.
def update_employee():
    # Exception Handling or Validation
    try:
        name =input("Enter Employee Name :")
    except (ValueError,NameError):
        print("Please type in a String!")
    for key in dict.keys():
        if key is name:
            # Exception Handling or Validation for Id
             try:
                emp_id=int(input("Enter Employee Id :"))
            except (ValueError,NameError):
                print("Please type in a Number!")
            # Exception Handling or validation For Department
            try:
                department =input("Enter Employee Department: ")
            except (ValueError,NameError):
                print("Please type in a String!")
            
            e= Employee(emp_id,name,department,datetime.datetime.now())
            dict[name] = e
            print(e)
            print(key)
    logging.info("Employee update successfully {}".format(e))