class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
#Defining a class containing one function and two variables


x = person("John", "Doe") #creating a variable with the class person
x.printname() #using the print function that is a part of the class

class professor(person):
    pass
#An example where we create a new class student that just inherits all of the variables and functions of person

y = professor("Matt", "McGeehan")
y.printname()
#Creating and printing under the class professor

class student(person):
    def __init__(self, fname, lname, major, year): 
        #creating a class that inherits all of the variables/functions of person as well as additional information
        super().__init__(fname, lname) #When adding more information on top of what was already inherited you have to use the super function
        #The super() function is used to inherit the parent classes original properties
        self.major = major
        self.gradYear = year
    
    def printstudent(self):
        print(self.firstname, self.lastname, self.major, self.gradYear)

z = student("Matt", "Rafferty", "Cybersecurity", 2027)
z.printname()
z.printstudent()