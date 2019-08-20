from Employee import Employee
from ShowEmployee import show_employee
from AddEmployee import add_employee
from ShowAllEmployee import show_all_employee
from UpdateEmployee import update_employee
import logging

# logging file configuration
#logging.basicConfig(filename ='/var/log/example.log',format='%(levelname)s %(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level =logging.DEBUG)
#logging console configuration
logging.basicConfig(format='%(levelname)s %(asctime)s- %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level =logging.DEBUG)

# While Loop Getting User Input
while True:
    choice =0
    print("1. Show Employee Details")
    print("2. Add Employee")
    print("3. Exit")
    print("4. Show Employees List")
    print("5. Update Employee")
    # Getting user Choice
    try:
        # Number Validation or Exception/Error Handling
        while (choice < 1) or (choice > 5):
            logging.info("getting User Input")
            choice = int(input("Enter Choice : "))
    except (ValueError,NameError):
        print("Please type in a number!")
             
    if choice == 1:
        logging.info("Called show_employee method")
        show_employee()
    elif choice == 2:
        logging.info("Called add_employee method")        
        add_employee()
    elif choice == 3:
        logging.info("User Closed application")
        break
    elif choice == 4:
        logging.info("Called show_all_employee method")        
        show_all_employee()
    elif choice == 5:
        logging.info("Called update_employee method")
        update_employee()
    else:
        logging.info("Choose a valid option")

