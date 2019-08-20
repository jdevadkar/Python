# Import Employee1 class
from Employee1 import Employee1
#created empty list
lists = []
# test Method
def test_system():
    # Created Employee1 Objects
    employee1 = Employee1(1,'bhds', 'dgf','rer')
    employee2 = Employee1(2, 'kljhk', 'dfhbhg','hgjdg')
    employee3 = Employee1(3, 'kljhk', 'dfhbhg','hgjdg')
    employee4 = Employee1(4, 'bn h', 'uurd','sjhjs')
    # Called add_employee method
    print("Called add method",add_employee(employee1,employee2,employee3,employee4))
    desplay_employee()
    #called delete_employee method
    print("Deleted Employee1",delete_employee(employee1))

    update_employee()
    desplay_employee()

# this method added employee in list
def add_employee(employee1,employee2,employee3,employee4):
    lists.append(employee1)
    lists.append(employee2)
    lists.append(employee3)
    lists.append(employee4)
    print("Employees added Successfully")
# this method deleted e employee into list
def delete_employee(employee):
    lists.remove(employee)
    print("Employee Deleted Sucessfully")

# this method printed all employee in list
def desplay_employee():
    print("All Employee")
    for i in lists:
        print(i)

# this method update employee
def update_employee():
    id =int(input("Enter Employee Id : "))
    for i in lists:
        if i == id:
            print("ID",i.Id)
            i.name="pratap"
            lists.append(i)
            desplay_employee()
# Called test_Sytsem Method
test_system()