print("Hello!!! Welcome to the rollercoaster!!")
heightcm = int(input("What's your height in cm? "))

if heightcm >= 120:
    print("Congratulations!! You can go to the rollercoaster!")
else:
    print("Sorry, you can't ride")
#Table of Operators
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == Equal to
# != Not equal to

#Ejercicio de par(even) o impar(odd)
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number") 
#Ejercicio de Bim con mas opciones
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
bim = round(weight/(height*height))
if bim<18.5:
    print(f"Your BMI is  {bim} , you are underweight")
elif bim<25:
    print(f"Your BMI is {bim}, you are normal weight")
elif bim<30:
    print(f"Your BMI is {bim}, you are slightly overweight")
elif bim<35:
    print(f"Your BMI is {bim}, you are obese")
else:
    print(f"Your BMI is {bim}, you are clinically obese")
#Exercise sobre años bisiestos
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")

else:
    print("Not leap year.")

#Ejercicio de if simultaneos
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3 #Esto es igual que bill = bill + 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

#Ejercicio sobre menu de pizzas
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
bill = 0
if size == "S":
    bill +=15
    if add_pepperoni == "Y":
        bill +=2
    else:
        bill +=0
elif size == "M":
    bill+=20
    if add_pepperoni == "Y":
        bill+=3
    else:
        bill+=0
elif size == "L":
    bill+=25
    if add_pepperoni =="Y":
        bill+=3
    else:
        bill+=0
else:
    print("No se eligio un valor correcto de tamaño de pizza")

if extra_cheese == "Y":
    bill+=1
else:
    bill+=0

print(f"El valor de la cuenta es de {bill}")
#Ejercicio de calculadora del amor
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
combined_string = name1 + name2
lower_string = combined_string.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")

true = t + r + u + e

l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")

love = l + o + v + e
love_score = int(str(true) + str(love))

if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score<=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
#######################################Ejercicio Treasure Island#############################################################
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
answer1 = input('You\'re at a crosroad, type "left" or "right".').lower()

if answer1 == "left":
    answer2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if answer2 == "wait":
        answer3 = input('You arrive at the island unarmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?? "Red", "Yellow" or "Blue" ').lower()
        if answer3 == "red":
            print("Burned by fire. Game Over")
        elif answer3 == "yellow":
              print("Congratulations, you win!!")
        elif answer3=="blue":
            print("You enter a room of beasts. Game Over!!!!")
        else:
            print("Game Over")
    else:
        print("You got attacked by an angry trout. Game Over!!")
else:
    print("Sorry, you fall into a hole!! Game Over!!")