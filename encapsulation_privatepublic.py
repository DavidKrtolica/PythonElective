##DEFINING A PRIVATE VARIABLE
class Person: 
   def __init__(self, name, alias):
      self.name = name       # public
      self.__alias = alias   # private

   def who(self):
      print('name  : ', self.name)
      print('alias : ', self.__alias)


##JAVA WAY OF ENCAPSULATION
class P: 
    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x > 1000:
            self.__x = 1000
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x


##PYTHONIC WAY FOR ENCAPSULATING
class O:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x > 1000:
            self.__x = 1000
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x


##CAR OBJECT EXERCISE
class Car:
    def __init__(self, model, year, km, hp):
        self.model = model
        self.year = year
        self.km = km
        self.hp = hp
    
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def km(self):
        return self.__km
    @km.setter
    def km(self, km):
        self.__km = km

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    ##STRING METHOD (ALSO REPRESENTATION) - FOR USERS
    def __str__(self):
        return f'Model: {self.model}, year: {self.year}, {self.km}km, {self.hp}hp'

    ##REPRESENTATION METHOD - FOR DEBUGGING
    def __repr__(self):
        return f'{self.__dict__}'