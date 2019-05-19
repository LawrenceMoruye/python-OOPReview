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

emp_class1="Lawi-morush-2010"
new_emp=Employee.from_string(emp_class1)
print(new_emp.email)

print(Employee.no_employee)#prints 0,we've instantiated 0
emp1=Employee("lawrence","moruye",10000)#creating first instance
emp2=Employee("leony","kemmy",5000)#creating 2nd instance
print(emp2.fullname())#name of employee 2
print(Employee.fullname(emp1))#fullname of emp2
print(Employee.no_employee)#prints 2,we've instantiated 2

