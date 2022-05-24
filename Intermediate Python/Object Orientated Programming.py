class Coordinate(object):   
    #very basic type is object
    def __init__(self,x,y): 
    #special method to create an instance (object) of the class, x & y is what data initializes a Coordinate Object, self is a parameter to refer to an instance (object) of the class type called Coordinate that is a placeholder instance since we have yet to actually create a specific instance.
        self.x = x
        self.y = y 
        #two data attributes for every Coordinate type object passed in, as __init__ is always called automatically 
    def distance(self,other):
    #procedral methods, functions that only work with this class, what a person can do with ur objects or this class
    #self used to refer to any instance, while other is another parameter to the method. Both are Coordinate Objects
        x_diff_sq = (self.x - other.x)**2 
        y_diff_sq = (self.y - other.y)**2
        #need self. and other. to assess the data attributes
    def __str__(self):
    #Python calls the __str__ method when used with print on class object & we can choose what it does when we print the class object of type Coordinate & do what is defined here. e.g. you want to print <3,4> when I call an object of coordinate type
        return '<' + str(self.x) + ',' + str(self.y) + '>'
    #str has to return a string, hence need str the self.x & self.y
        
c = Coordinate(3,4)
origin = Coordinate(0,0)
#creates a new object, c and origin of type Coordinate which passes in 3 and 4 data and 0,0 to the __init__, calling an instance of the class, self is taken by python to be c/origin as it is the placeholder

print(origin.x)
print(c.x)
#assessing data attributes == instances/object variables

print(c.distance(origin))
#saying this object c is of the type Coordinate, find a method in the class that is named distance, sees that there is another parameter other, which we place in the paranthesis
#==
print(Coordinate.distance(c,origin))
#name of class, method being called, all the variables including self

print (c)
#uninformative print representation that just says c is a coordinate type object at a memory location, hence there is a need of def __str__method

print(type(c)) 
print(Coordinate)
# <class __main__.Coordinate>, the type of object c is a class coordinate and Coordinate is a class
print(type(Coordinate))
# <type 'type'>, a Coordinate class is a type of object

print(isinstance(c,Coordinate))
#True, isinstance checks if the object c is indeed a Coordinate class type

# If you want to do this operators to a coordinate object, python does not know actually, hence we need to def it as a method in the class coordinate but the thing is we can decide what the __add__ does, which python would do when self + other
#__add__(self, other) -> self+other
#__sub__(self, other) -> self-other
#__eq__(self, other) -> self == other
#__lt__(self,other) -> self < other
#__len__(self) -> len(self)
#__str__(self) -> print self

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age = newage
    def set_name(self,newname=''):
        # newname='' is the default argument for formal parameters id no actual arg given
        self.name = newname
    def __str__(self):
        return 'animal:' + str(self.name) + ':' + str(self.age)
    #getter that returns the values of any of the data attributes. Setter that set the data attributes to whatever that has been passed in

class Cat(Animal): 
#python sees that cat's parent class is Animal, hence all the attributes and methods Animal the Cat class has. Hence __init__ is not missing, it looks at the parent if there is since there is not one in the child class. Always look at child, if not look at the parent if not continue upwards
    def speak(self):
        print('meow')
        #adding a new functionality called speak()
    def __str__(self):
        return 'cat:' + str(self.name) + ':' + str(self.age)
        #overiding
        
a = Animal(3)
#recall dot notation can be used to access the data attributes (data or methods)
a.age
#better to use gettter and stters to access
a.get_age()
a.set_name()
#for the formal parameters there are no arguments (), hence by default the argument is the default ''
a.set_name('fluffy')
print(a.get_name())
#prints 'fluffy' as the default argument '' is now 'fluffy' actual argument that is passed into the definition
class Animal(object):
    def __init__(self,age):
        self.years = age
        self.name = None
    def get_age(self):
        return self.years
#if the author changes the data attribute that age would be the number of years. a.age would get an attritbute error, unlike a.get_age()
    
#Python allows us to asses data from outside class definition
print(a.age)
#allows us to write to data from outside class definition
a.age = 'infinite'
#allows us to create data attribute for an instance from outside class definition
a.size = 'tiny'

#parent class (superclass)
#child class (subclass), inherits all data & behaviours of parent class, add more info/behaviour or even override the behaviour


class Rabbit(Animal):
    tag = 1
    #class variable, values shared between all the instances of the class
    def __init__(self,age,parent1=None,parent2=None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid (#instance variable) = Rabbit.tag (#assess class variable)
        Rabbit.tag += 1 #after each instance of Rabbit is created, the class variable increments by 1, which is shared by all instances, hence eg. r1.rid = 1, r2.rid = 2, r3.rid = 3
    #hence class variable tag is used to give an unique id to each new rabbit instance 
            
            
class Person(Animal):
    def __init__(self, name, age):
            Animal.__init__(self,age) #calls Animal's initialization
            self.set_name(name) #call Animal's method
            self.friends = []  #adding a new data attribute
    def get_friends(self):
            return self.friends #new getter method
    def add_friend(self,fname):
            if fname not in self.friends:
                self.friends.append(fname)
    def speak(self):
            print('hello')
    def age_diff(self,other):
            diff = self.age - other.age
            print(abs(diff), 'year difference'))
    def __str__(self):
        return 'person:' + str(self.name) + ":" + str(self.age)
    
p1 = Person('Jack', 30)
p2 = Person('Tom', 25)
print(p1.get_name())
print(p2.get_name())
print(p2.get_age())
print(p1)
p1.speak()
p1.age_diff(p2)

import random
class Student(Person):
    def __init(self, name, age, Major='')
        Person.__init__(self,name,age)
        self.major = major
    def change_major(self,major):
        self.major = major
    def speak(self):   #overriding the speak method
        r = random.random()
        if r <0.25:
            print("i have homework to do")
        elif 0.25<= r < 0.5:
            print("i need to sleep soon")
        elif 0.5 <= r < 0.75:
            print("i should go eat soon")
        else:
            print("i am procrastinating by watching tv now")
    def __str__(self):
        return "student:" + str(self.name) + ":" + 'age:' + str(self.age) + ":" + str(self.major)

#Q1
import math
class Coordinate(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def magnitude(self):
        value = math.sqrt((self.x)**2 + (self.y)**2)
        return value
    def translate(self,dx,dy):
        self.dx = dx
        self.dy = dy
        self.x = self.x + self.dx
        self.y = self.y + self.dy
    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
        
#Q2
class Celsius(object):
    def __init__(self,temperature=0):
        self.temperature = temperature
        
    def to_fahrenheit(self):
        fahrenheit = self.temperature * 9/5 + 32
        return fahrenheit
    
    def get_temperature(self):
        return self._temperature
    
    def set_temperature(self,value):
        if value < -273:
            self._temperature = -273
        else:
            self._temperature = value
        return self.temperature

    temperature = property(get_temperature,set_temperature)

#Celsius has 1 attribute data called _temperature that stores the value. Underscore designates a private attribute that can only be accessed inside this class. def set_temperature assigns the value to the attribute, self._temperature. def get_temperature returns the set_temperature. The property allows python to assess the _temperature attribute and assigns it to a public attribute temperature

#Q3
import time
class StopWatch(object):
    def __init__(self):
        self.start_time = time.time()
        self.end_time = -1
    #should not use optional arguments in __init__(). 2 instance attributes
        
    def start(self):
        self.start_time = time.time()
        self.end_time = -1
        
    def stop(self):
        self.end_time = time.time()
        
    def elapsed_time(self):
        elapsed = (self.end_time - self.start_time)
        if elapsed > 0:
            return round(elapsed,1)
        else:
            return None
        
#Q4
import numpy as np
class Line(object):
    def __init__(self,c0,c1):
        self.c0 = c0
        self.c1 = c1
    def __call__(self,x):
        return self.c0 + self.c1 * x
    def table(self,L,R,n):
        if n == 0:
            return "Error in printing table"
        n=1 if L==R else n
        x_list = np.linspace(L,R,n)
        y_list = np.vectorize(self.__call__)(x_list)
        table = ''
        for x,y in zip(x_list,y_list):
            table += ( f'{x:10.2f}{y:10.2f}\n')
        return table

#Q1
class Time(object):
    def __init__(self,_hours,_minutes,_seconds):
        self._hours = _hours
        self._minutes = _minutes
        self._seconds = _seconds
        
    def get_elapsed_time(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds

    def set_elapsed_time(self,_seconds):
        self._hours = _seconds // 3600 % 24
        remainder = _seconds % 3600
        self._minutes = remainder // 60
        self._seconds = remainder % 60
        
    def __str__(self):
        return 'Time: %d:%d:%d'%(self._hours, self._minutes, self._seconds)
    
    elapsed_time = property(get_elapsed_time,set_elapsed_time)

            
class Account(object):
    def __init__(self, owner, account_number, amount):
        self._owner = owner
        self._account_number = account_number
        self._balance = amount #new object,instance balance
        
    def deposit(self,amount):
        self._balance += amount
        
    def withdraw(self,amount):
        self._balance -= amount
        
    def __str__(self):
        return  '%s, %s, balance: %d'%(self._owner, self._account_number, _self.balance)
            
#Q2
class Account(object):
    def __init__(self, owner, account_number, amount):
        self._owner = owner
        self._account_number = account_number
        self._balance = amount #new object,instance balance
        
    def deposit(self,amount):
        self._balance += amount
        
    def withdraw(self,amount):
        self._balance -= amount
        
    def __str__(self):
        return  '%s, %s, balance: %d'%(self._owner, self._account_number, _self.balance)          
            
#Q3
class Diff(object):
    def __init__(self, f, h=1E-4):
        self.f = f
        self.h = h
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x)) / h
        
#Q4
import copy
class Polynomial(object):
    def __init__(self, coeff):
        self.coeff = coeff
    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            newcoeff = copy.deepcopy(self.coeff)
            for i in range (0,len(order.coeff)):
                newcoeff[i] = self.coeff[i] + other.coeff[i]
        else:
            newcoeff = copy.deepcopy(other.coeff)
            for i in range (0,len(self.coeff)):
                newcoeff[i] = self.coeff[i] + other.coeff[i]
        return Polynomial(newcoeff)
    def __sub__(self, other):
        if len(self.coeff) > len(other.coeff):
            newcoeff = copy.deepcopy(self.coeff)
            for i in range (0, len(other.coeff)):
                newcoeff[i] = self.coeff[i] - other.coeff[i]
        else:
            newcoeff = copy.deepcopy(other.coeff)
            for i in range (0, len(self.coeff)):
                newcoeff[i] = self.coeff[i] - other.coeff[i]
            for j in range (len(self.coeff),len(other.coeff)):
                newcoeff[j] = -other.coeff[j]
        return Polynomial(newcoeff)
    def __call__(self,x):
        p_x = 0
        for i in range(0, len(self.coeff)):
            p_x += self.coeff[i] * x ** i
        return p_x
    def __mul__(self, other):
        l = []
        for x in range(0,len(self.coeff) + len(other.coeff) -1 ):
            l.append(0)
        for i in range(0,len(self.coeff)):
            for j in range(0,len(other.coeff)):
                newcoefficientvalue = self.coeff[i] * other.coeff[j]
                l[i+j] += newcoefficientvalue
        return Polynomial(l)
            
    def differentiate(self):
        for i in range(len(self.coeff)-1):
            self.coeff[i]=self.coeff[i+1]*(i+1)
        del(self.coeff[-1])
            
    def derivative(self):
        derivative = Polynomial(self.coeff[:])
        derivative.differentiate()
        return derivative

The first method is differentiate which returns None but changes the coefficients
of the current polynomial instance on which it is called.
The second method is derivative, which returns a new Polynomial instance with
containing the new coefficients