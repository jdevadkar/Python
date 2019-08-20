from Employee import Employee
from Dictionary import dict
import datetime
import logging

# This method Added Employee in dictionary
def add_employee():
    try:
        emp_id = int(input("Enter Employee Id : "))
    except (ValueError,NameError):
        print("Please type a number!")
    try:
        name =str(input("Enter Enployee Name : "))
    except (ValueError,NameError):
        print("Please type a String!")
    try:
        department =str(input("Enter Employee Department : "))
    except (ValueError,NameError):
        print("Please type String!")
    e =Employee(emp_id,name,department,datetime.datetime.now())
    dict[name]= e
    logging.info("Employee Added Sucessfully")