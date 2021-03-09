class Person:
    spicies = 'Mammal' ## CLASS VARIABLE, SHARED BY ALL OBJECTS CREATED (STATIC) 

    #def __init__(self, name): ## UNIQUE INSTANCE VARIABLE WHICH IS DYNAMIC
        #self.name = name

    def __init__(self, *args): 
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        else:
            self.name = 'No No No'

    #def __init__(self, name=None, age=None):
        #self.name = name
        #self.age = age

    def name_age(self):
        return name + ' ' + age



class Instructor:
    def __init__(self, course):
        self.course = course

    

class Student(Person, Instructor):
    def __init__(self, name, course):
        Person.__init__(self, name)
        Instructor.__init__(self, course)
        #super().__init__(name)