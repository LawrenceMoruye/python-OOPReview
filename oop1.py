class Employee:
	def __init__(self,first,last,pay):
		self.first=first#instance variable
		self.last=last#instance variable
		self.pay=pay
		self.email=first+last+'@gmail.com'#instance variable

	def fullname(self):#all functions in a class take self as the first argument
		return "{} {}".format(self.first,self.last)


emp1=Employee("lawrence","moruye",10000)#creating first instance
emp2=Employee("leony","kemmy",5000)#creating 2nd instance
print(emp1.email)#obtain the name of employee1
print(emp2.fullname())#name of employee 2
print(Employee.fullname(emp1))#fullname of emp2