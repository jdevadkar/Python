# Employee1 Class
class Employee1:
    'Id, name, department, job_title'

    # init method assign employee values
    def __init__(self, id,name,department,job_title):
        self.Id =id
        self.name=name
        self.department=department
        self.job_title =job_title

    # Print object in string Format Like toString Method
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
