print("Hello"[4]) ##imprime el valor numero 4 contando desde 0
#Types of dates
#String
print("123" + "456")
city = "tuxtla"
print(city)
#Int
edad = 14
print(123+456)
#Float
PI=3.1416
print(PI)
#Boolean
True
False

num = len(input("What's your name? "))#Se declara a num como valor int
new_num = str(num) #Num se convierte a string en una nueva variable
print(type(num)) #se revisa que tipo de datos es num usando type
print("Your name has "+ new_num+ " characters")

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
res=(int(two_digit_number[0])+int(two_digit_number[1]))#con int se convierten a enteros
resul = str(res)
print(two_digit_number[0] +' + '+ two_digit_number[1] + ' = '+ resul)
####################################
#PEMDAS
# ()
# **
# */
# +-
#Ejercicio sobre peso y altura
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
float_height = float(height) #convierte los valores a float
float_weight = float(weight)
res = int(float_weight / (float_height**2))
#Write your code below this line 👇
print(res)

print(round(2.666666666666666,2))#permite redondear hacia arriba los resultados
print(f"tu altura es {height}")
###############################################################
#Ejercicio sobre calculo de vida restante
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
age_int=int(age)
daysa = age_int*365
daysr = str(32850-daysa)
weeksa=age_int*52
weeksr=str(4680-weeksa)
monthsa=age_int*12
monthsr = str(1080-monthsa)

print("You have " +daysr+ " days, " +weeksr+ " weeks, and " +monthsr+ " months left.")

#Ejercicio de calculadora de propinas
print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
porcentaje = int(input("What percentage tip would you like  to give? 10/12 or 15? "))
people = int(input("How many people to split the bill? "))

resultado = (total+((total) * float(porcentaje))/100)/people
resultado = "{:.2f}".format(resultado) #{:.2f} sirve para mostrar el resultado con 2 decimales extras.
print("Each person should pay: $" + resultado)