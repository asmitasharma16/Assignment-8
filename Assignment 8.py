#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
pi=3.14
class circle:
    def __init__(self,r):
        self.r=r

    def getArea(self):
        a=pi*self.r*self.r
        return(a)
    def getcircumference(self):
        c=2*pi*self.r
        return(c)
r=int(input('Enter radius of circle '))    
c1 =circle(r)
print('Area of circle is ',c1.getArea())
print('Circumference of circle is ',c1.getcircumference())


#Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
#1. Display - It should display all informations of the student. 
#2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.marks=marks
    def display(self):
        print('name:{} \nrollno:{} \nmark:{} \nage:{}'.format(self.name,self.rollno,self.marks,self.age))
name=input('Student\'s name ')
rollno=int(input('Rollno '))
age=int(input('age '))
marks=int(input('marks '))
s =student(name,rollno)
s.setAge(age)
s.setMarks(marks)
s.display()


#Q.3- Create a Temprature class and create two methods: 
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class Temperature:
    def convertFahrenheit(self,c):
        f=(c*9/5)+32
        return(f)
    def convertCelsius(self,f):
        c=(f-32)*(5/9)
        return(c)
ch=input('enter choice to enter temperature in Fahreheit(f) or Celsius(c) ')
T =Temperature()
if(ch=='f' or ch=='F'):
    f=int(input('Enter Temperature in Fahrenheit '))
    print('Temperature in celcius is ',end='')      
    print(T.convertCelsius(f))
elif(ch=='c' or ch=='C'):
    c=int(input('Enter Temperature in celcius '))
    print('Temperature in Fahrenheit is ',end='')
    print(T.convertFahrenheit(c))


#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
#Make methods to 
#1. Display-Display the details. 
#2. Add- Add the movie details.
class MovieDetails:
    def __init__(self,moviename,artistname,YOR,rating):
        self.moviename=moviename
        self.artistname=artistname
        self.YOR=YOR
        self.rating=rating
    def Display(self):
        print('MOVIE:{}\nARTIST NAME:{}\nYEAR OF RELEASE:{}\nRATINGES:{}'.format(self.moviename,self.artistname,self.YOR,self.rating))
    def Add(self,musicby):
        self.musicby=musicby
        print('MUSICBY:{}'.format(self.musicby))
moviename=input('Enter movie name ')
artistname=input('Enter artist name ')
YOR=int(input('Enter year of release '))
rating=int(input('Enter Ratings '))
musicby=input('Enter Music by to add more details ')
M =MovieDetails(moviename,artistname,YOR,rating)
M.Display()
M.Add(musicby)


#Q.5- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
    def __init__(self,animal_name):
        self.animal_name=animal_name
    def animal_attribute(self):
        print(('animal name is {}, its gender is {} and breed is {}').format(self.animal_name,self.gender,self.breed))
class Tiger(Animal):
    def __init__(self, name, gender, breed):
        self.name = name
        self.gender = gender
        self.breed = breed
        Animal.__init__(self, 'Tiger')
A=Tiger('Tegu','male','Bengal Tiger')
A.animal_attribute()


#Q.6- What will be the output of following code. 
class A:
        def f(self):
            return self.g()

        def g(self):
            return 'A'

class B(A):
        def g(self):
            return 'B'
a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())
'''
output:
A B
A B
'''

#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
class shape:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def Area(self):
        return(self.l*self.b)
class rectangle(shape):
    def __init__(self,l,b):
        super(rectangle,self).__init__(l,b)
class square(shape):
    def __init__(self,l,b):
        super(square,self).__init__(l,b)
l=int(input('enter length of rectangle '))
b=int(input('enter breadth of rectangle '))
r =rectangle(l,b)
print('Area of reactangle is {}'.format(r.Area()))
l=int(input('enter length of square '))
b=l
s =square(l,b)
print('Area of square is {} '.format(s.Area()))


