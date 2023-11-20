class Person:
    def _init_(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        def greet(self):
            print(f"Hello my name is {self.name} and I am a {self.gender} person.")

person =  Person("Jason", 18, "Male")
person.greet()