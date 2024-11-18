print (2 + 3)

# The below line prints hello world
# Python interpreter will ignore comments
print('Hello World!') 

print('Goodbye!') # Comments can be placed anywhere after a comment

# Data Types


# Numbers

#int - integers
print (type(5))

#float are decimals
print(type(3.14159))

#complex
print(type(2 + 3j))

#Number Operations
print(2+3)
print(2-3)
print(2*3) #multiplication
print(10/5) #float division
print(10//5) #integer division
print(int(10//3.5)) #integer division (with typecast)
print(5%2) #modulo (remainder)

# Strings - "Hello World" 'Hello World'
print("Hello!!")
print('It\'s Monday!') #use \ to escape
print(type('hello'))

#Concatenation
print('Hello' + ' ' +'World!')

#string methods
print('Hello'.upper()) #capitalises string
print('Hello'.lower()) #lower case string
print('Hello World'.replace('World', 'There')) #creplaces string

#booleon - true or false
print(True)
print(type(True))

#Falsy values
print(bool(0)) #evaluates to false value
print(bool('')) #evaluates to false value
print(bool('ldkjl')) #evaluates to true
print(bool(None))
print(bool([]))#evaluates to false value
print(bool(()))#evaluates to false value
print(bool({}))#evaluates to false value

#Comparison Operators <, >, <=, >=, ==
print(2 < 3)
print(2 > 3)
print(2 >= 3)
print(3 == 3)

#Logical Operators - and, or, not
print(True and False)
print(False or True)
print (5 > 3 and 2 < 5)

#Variables
num1 = 5
num2 = 4
print(num1 + num2)
num2 = 10
print(num1 + num2)

#String interpolation
name = 'Cherylynn'
print("My name is " + name + " and I live in Corrimal" )
#f-string
print(f"My name is {name} and I live in Corrimal" )