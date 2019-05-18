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
		

print(Employee.no_employee)#prints 0,we've instantiated 0
emp1=Employee("lawrence","moruye",10000)#creating first instance
emp2=Employee("leony","kemmy",5000)#creating 2nd instance
print(emp1.email)#obtain the name of employee1
print(emp2.fullname())#name of employee 2
print(Employee.fullname(emp1))#fullname of emp2
print(Employee.no_employee)#prints 2,we've instantiated 2