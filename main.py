




class Employee:
    def __init__(self,name,email,phone,dob,salary,department):
        self.name = name 
        self.email = email 
        self.phone= phone
        self.dob = dob
        self.salary = salary
        self.department= department
        
    def get_annual_salary(self):
            return self.salary *12
        
    def get_monthly_salary(self):
            pass 
        
    def get_name(self):
        return self.name
    
    def get_phone(self ):
        return self.phone
    
    def which_department(self ):
        return self.department
        
    
emp = Employee("Ghan","g@gmail","98989","test_date_of_birth",100, "cloud computing")
print(emp.name )
print(emp.email)
print(emp.get_annual_salary())
print(emp.get_phone())
print(emp.which_department())




emp1=Employee ("Nepal","google@gmail",'939393',"dateofbirth",200,"production")
print(emp1.name)
print(emp1.get_name())
print(emp1.get_phone())








