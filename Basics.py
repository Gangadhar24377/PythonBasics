# Variables
""" name = "John Smith"
age = 20
patient_status = "new"
print(name, age, patient_status) """

# Recieving Input
""" name = input("What is your name? ")
print("Hello " + name) """

# Type Conversion

#int() -> integer, bool() -> boolean, float() -> basically decimals, str() -> string

""" birth_year = int(input("Enter your birth year: "))
age = 2023-birth_year
print(age) """



""" first_num= float(input("Enter Your First Num: "))
sec_num= float(input("Enter Your Sec Num: " ))
sum = first_num + sec_num
print("Sum is: " + str(sum)) """

# Strings

""" course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.find('y')) # -> Gives the index, Strings are immutable
print(course.replace('for', '4'))
print(course.find('Python'))
print('Python' in course) # in operator, gives boolean value """

## Arithmetic operators

# Uk nigga

# operator precedence

# brackets and shi eg: 10 + 3*2 = 16 but (10+3)*2 = 26

## Comparision operators
""" x = 3 >= 2
x = 3 <= 2
x = 3 == 2 
x = 3 != 2 # not equal """

# Logical operators

""" price = 25
print(price > 10 and price < 30) # and operator

print(price > 10 or price < 30) # or operator

print(not price > 10) # not operator """

# if statements

""" temp = int(input("Temp: "))

if temp > 35:
    print("Hot day")
elif temp > 20:
    print("U aint sweating")
else:
    print("Not hot day") """


""" weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in (L)bs: "+ str(converted))
else:
    converted = weight * 0.45
    print("Weight in (K)gs: " + str(converted)) """

# while loops

i = 1

while i <= 5:
    print(i * '*')
    i +=1