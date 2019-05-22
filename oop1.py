class Employee:
	raise_amount=1.04#claas variable
	no_employee=0#class variable
	def __init__(self,first,last,pay):
		self.first=first#instance variable
		self.last=last#instance variable
		self.pay=pay
		self.email=first+last+'@gmail.com'#instance variable
		Employee.no_employee+=1# initialized class variable with class name
		# bcoz each time a new emplyer joins,the value increaments uniformly

	def fullname(self):#all functions in a class take self as the first argument
		return "{} {}".format(self.first,self.last)

	def pay_rise(self):
		self.pay=(self.pay*self.raise_amount)#initializsd class variable using self
											#bcoz,pay can cange for different employees
	@classmethod
	def from_string(cls,emp_str):
		first,last,pay=emp_str.split("-")
		return cls(first,last,pay)

	@staticmethod#creating a ststic method
	def isworkday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True


#creating a subclass ,it inherits from Employee
class Developer(Employee):
	def __init__(self,first,last,pay,pro_lang):
		super().__init__(first,last,pay)
		self.pro_lang=pro_lang


#subclass 2,inherits from employee,showing employees supervised a manager
class Manager(Employee):
	def __init__(self,first,last,pay,employees=None):

		super().__init__(first,last,pay)
		if employees is None:
			self.employees=[]
		else:
			self.employees=employees

	def add_emp(self,emp):#function that adds an employee
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):#removes an employee from the list
		if emp in self.employees:
			self.employees.remove(emp)



	def print_emp(self):#prints the number of employees a manager supervises
		for emp in self.employees:
			print("-->",emp.fullname())







emp_class1="Lawi-morush-2010"
new_emp=Employee.from_string(emp_class1)
print(new_emp.email)

print(Employee.no_employee)#prints 0,we've instantiated 0
emp1=Employee("lawrence","moruye",10000)#creating first instance
emp2=Employee("leony","kemmy",5000)#creating 2nd instance
print(emp2.fullname())#name of employee 2
print(Employee.fullname(emp1))#fullname of emp2
print(Employee.no_employee)#prints 2,we've instantiated 2

import datetime
daycheck=datetime.date(1998,4,26)
print(Employee.isworkday(daycheck))

dev1=Developer("lawrence","Moruye",50000,"python")
dev2=Developer("lawre","Morush",60000,"c++")
mgr1=Manager("neckl","nma",12000,[dev1])
print(mgr1.email)
mgr1.add_emp(dev2)
print(mgr1.print_emp())