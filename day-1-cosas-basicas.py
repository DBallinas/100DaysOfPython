#\n sirve para salto de linea
print("Hola\nBienvenido al sumario de Python")
len(input("What is your name? ")) #con len se cuenta los caracteres
age = input("What's your age? ")
print(age)

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
c=a
d=b
a=d
b=c
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#1. Create a greeting for your program.
print("Welcome to the python course!!")
#2. Ask the user for the city that they grew up in.
city =input("what city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet= input("What's your pet name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band's name is\n"+ city + " " + pet +"!!")
#5. Make sure the input cursor shows on a new line