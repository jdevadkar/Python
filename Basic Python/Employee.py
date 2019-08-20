import datetime
# Created Employee Class.
class Employee:
    # Class Init method
    def __init__(self,emp_id,name,department,date):
        self.emp_id = emp_id
        self.name=name
        self.department =department
        self.date =date
    # Printed Object as String format
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    