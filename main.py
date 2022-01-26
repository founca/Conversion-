
units_convert = [0.393701, 2.54, 0.08333333, 12, 0.3333333, 3]
currency_convert = [0.89, 1.13]
temp_convert = [33.8, -457.87, -17.22, -272.12, 225.928]

def main():
    global units_convert
    global currency_convert
    global temp_convert
   

    language = int(input("1 - English \n2 - Español \n3 - French \nSelect: "))
    if language == 1:
        english()
    elif language == 2:
        spanish()
    else:
        print("Not an option")


def english():
    global name
    print("_________________________")
    print(" ")
    name = input("Enter your name: ")
    print(" ")
    print("Welcome", name, "what would you like to convert?")
    print("Select a conversion below.")
    user_decision = int(input("\n1 for Temperature \n2 for Currency  \n3 for Units \nSelect a number: "))
    if user_decision == 1:
        temperature()
    elif user_decision == 2:
        currency()
    elif user_decision == 3:
        units()
    else:
        print("Don't be silly", name, "that isn't one of the options. Now you have to redo it over again... sigh")
        english()


def temperature():
    print(" ")
    print("_________________________")
    print(" ")
    print("You've selected temperature")
    print("What temperatures are you converting", name, "?")
    print("Select temperatures below")
    print(" ")
    user_input = int(input("1 - Celsius to Fahrenheit \n2 - Kelvin to Fahrenheit \n3 - Fahrenheit to Celsius \n4 - "
                           "Kelvin to Celsius \n5 - Fahrenheit to Kelvin \n\nSelect an option: "))
    if user_input == 1:
        print("_________________________")
        print(" ")
        print("You've selected 1, Celsius to Fahrenheit")
        print(" ")
        degrees = int(input("Enter the Celsius amount: "))
        conversion = degrees * (temp_convert[0])
        print("When you convert", degrees, "Celsius in to Fahrenheit you get", round(conversion), "Fahrenheit")
        continuing()
    elif user_input == 2:
        print("_________________________")
        print(" ")
        print("You've selected 2, Kelvin to Fahrenheit")
        print(" ")
        degrees = int(input("Enter the Kelvin amount: "))
        conversion = degrees * (temp_convert[1])
        print("When you convert", degrees, "Kelvin in to Fahrenheit you get", round(conversion), "Fahrenheit")
        continuing()
    elif user_input == 3:
        print("_________________________")
        print(" ")
        print("You've selected 3, Fahrenheit to Celsius")
        print(" ")
        degrees = int(input("Enter the Fahrenheits amount: "))
        conversion = degrees * (temp_convert[2])
        print("When you convert", degrees, "Fahrenheit in to Celsius you get", round(conversion), "Celsius")
        continuing()
    elif user_input == 4:
        print("_________________________")
        print(" ")
        print("You've selected 4, Kelvin to Celsius")
        print(" ")
        degrees = int(input("Enter the Kelvin amount: "))
        conversion = degrees * (temp_convert[3])
        print("When you convert", degrees, "Kelvin in to Celsius you get", round(conversion), "Celsius")
        continuing()
    elif user_input == 5:
        print("_________________________")
        print(" ")
        print("You've selected 5, Fahrenheit to Kelvin")
        print(" ")
        degrees = int(input("Enter the Fahrenheit amount: "))
        conversion = degrees * (temp_convert[4])
        print("When you convert", degrees, "Fahrenheit in to Kelvin you get", round(conversion), "Kelvin")
        continuing()
    else:
        print("That wasn't one of the options")
        temperature()


def currency():
    print(" ")
    print("_________________________")
    print(" ")
    print("You've selected currency")
    print("Which currency are you converting", name, "?")
    print("Select down below")
    print(" ")
    print("1 - United State Dollar to Euro \n2 - Euro to United State Dollar ")
    user_input = int(input("Which conversion rate do you choose: "))
    if user_input == 1:
        print("_________________________")
        print(" ")
        print("You've selected USD TO Euro")
        print(" ")
        money = int(input("Enter the amount: "))
        conversion = (currency_convert[0]) * money
        print(money, "$, is turned into", conversion, "€")
        continuing()
    elif user_input == 2:
        print("_________________________")
        print(" ")
        print("You've selected Euro TO USD")
        print(" ")
        money = int(input("Enter the amount: "))
        conversion = (currency_convert[1]) * money
        print(money, "€, is turned into", conversion, "$")
        continuing()
    else:
        print("That wasn't one of the options")
        currency()


def units():
    print(" ")
    print("_________________________")
    print(" ")
    print("You've selected units")
    print("Which measurements are you converting", name, "?")
    print("Select down below")
    print(" ")
    user_input = int(input("1 - Centimeters to Inches \n2 - Inches to Centimeters \n3 - Inches to Feet \n4 - Feet to "
                           "Inches \n5 - Feet to Yards \n6 - Yards to Feet \nWhich conversion rate do you choose: "))
    if user_input == 1:
        print("_________________________")
        print(" ")
        print("You've selected 1, Centimeters to Inches")
        length = int(input("Enter the length: "))
        conversion = length * (units_convert[0])
        print(" ")
        print("The length will now become", conversion, "Inches")
        continuing()
    elif user_input == 2:
        print("_________________________")
        print(" ")
        print("You've selected 2, Inches to Centimeters")
        length = int(input("Enter the length: "))
        conversion = length * (units_convert[1])
        print(" ")
        print("The length will now become", conversion, "Centimeters")
        continuing()
    elif user_input == 3:
        print("_________________________")
        print(" ")
        print("You've selected 3, Inches to Feet")
        length = int(input("Enter the length: "))
        conversion = length * (units_convert[2])
        print(" ")
        print("The length will now become", conversion, "Feet")
        continuing()
    elif user_input == 4:
        print("_________________________")
        print(" ")
        print("You've selected 4, Feet to Inches")
        length = int(input("Enter the length: "))
        conversion = length * (units_convert[3])
        print(" ")
        print("The length will now become", conversion, "Inches")
        continuing()
    elif user_input == 5:
        print("_________________________")
        print(" ")
        print("You've selected 5, Feet to Yards")
        length = int(input("Enter the length: "))
        conversion = length * (units_convert[4])
        print(" ")
        print("The length will now become", conversion, "Yards")
        continuing()
    elif user_input == 6:
        print("_________________________")
        print(" ")
        print("You've selected 6, Yards to Feet")
        length = int(input("Enter the length: "))
        conversion = length * (units_convert[5])
        print(" ")
        print("The length will now become", conversion, "Feet")
        continuing()
    else:
        print("That wasn't one of the options")
        units()


def spanish():
    global name
    print("_________________________")
    print(" ")
    name = input("Introduzca su nombre: ")
    print(" ")
    print("¿Bienvenido", name, "Qué te gustaría convertir?")
    print("Seleccione una conversión a continuación.")
    user_decision = int(input("\n1 para la Temperatura \n2 para Moneda  \n3 para Unidades \nSeleccionar un numero: "))
    if user_decision == 1:
        temperatura()
    elif user_decision == 2:
        moneda()
    elif user_decision == 3:
        unidades()
    else:
        print("No seas tonto", name, "esa no es una de las opciones. Ahora tienes que rehacerlo de nuevo.... suspiro")
        spanish()


def temperatura():
    print(" ")
    print("_________________________")
    print(" ")
    print("Has seleccionado la temperatura")
    print("¿Qué temperaturas estás convirtiendo", name, "?")
    print("Seleccione las temperaturas a continuación")
    print(" ")
    user_input = int(input("1 - Celsius a Fahrenheit \n2 - Kelvin a Fahrenheit \n3 - Fahrenheit a Celsius \n4 - "
                           "Kelvin a Celsius \n5 - Fahrenheit a Kelvin \n\nSeleccione una opción: "))
    if user_input == 1:
        print("_________________________")
        print(" ")
        print("Has seleccionado 1, Celsius a Fahrenheit")
        print(" ")
        degrees = int(input("Ingrese la cantidad Celsius: "))
        conversion = degrees * (temp_convert[0])
        print("Cuando te conviertes", degrees, "Celsius en Fahrenheit obtienes", round(conversion), "Fahrenheit")
        continuo()
    elif user_input == 2:
        print("_________________________")
        print(" ")
        print("Has seleccionado 2, Kelvin a Fahrenheit")
        print(" ")
        degrees = int(input("Ingrese la cantidad de Kelvin: "))
        conversion = degrees * (temp_convert[1])
        print("Cuando te conviertes", degrees, "Kelvin en Fahrenheit obtienes", round(conversion), "Fahrenheit")
        continuing()
    elif user_input == 3:
        print("_________________________")
        print(" ")
        print("Has seleccionado 3, Fahrenheit a Celsius")
        print(" ")
        degrees = int(input("Ingrese la cantidad en Fahrenheits: "))
        conversion = degrees * (temp_convert[2])
        print("Cuando te conviertes", degrees, "Fahrenheit en Celsius obtienes", round(conversion), "Celsius")
        continuing()
    elif user_input == 4:
        print("_________________________")
        print(" ")
        print("Has seleccionado 4, Kelvin a Celsius")
        print(" ")
        degrees = int(input("Ingrese la cantidad en Kelvin: "))
        conversion = degrees * (temp_convert[3])
        print("Cuando te conviertes", degrees, "Kelvin en Celsius obtienes", round(conversion), "Celsius")
        continuing()
    elif user_input == 5:
        print("_________________________")
        print(" ")
        print("You've selected 5, Fahrenheit to Kelvin")
        print(" ")
        degrees = int(input("Ingrese la cantidad en Fahrenheits: "))
        conversion = degrees * (temp_convert[4])
        print("Cuando te conviertes", degrees, "Fahrenheit en Kelvin obtienes", round(conversion), "Kelvin")
        continuing()
    else:
        print("TEsa no era una de las opciones")
        temperatura()


def moneda():
    print(" ")
    print("_________________________")
    print(" ")
    print("Has seleccionado la moneda")
    print("¿Qué moneda estás convirtiendo", name, "?")
    print("Seleccione abajo")
    print(" ")
    print("1 - Dólar estadounidense a euro \n2 - Euro aDólar estadounidense ")
    user_input = int(input("Que tasa de conversión eliges: "))
    if user_input == 1:
        print("_________________________")
        print(" ")
        print("Ha seleccionado USD A Euro")
        print(" ")
        money = int(input("Introduce la cantidad: "))
        conversion = (currency_convert[0]) * money
        print(money, "$, se convierte en", conversion, "€")
        continuo()
    elif user_input == 2:
        print("_________________________")
        print(" ")
        print("Ha seleccionado Euro A USD")
        print(" ")
        money = int(input("Introduce la cantidad: "))
        conversion = (currency_convert[1]) * money
        print(money, "€, se convierte en", conversion, "$")
        continuo()
    else:
        print("Esa no era una de las opciones")
        moneda()


def unidades():
    print(" ")
    print("_________________________")
    print(" ")
    print("Has seleccionado unidades")
    print("¿Qué medidas estás convirtiendo", name, "?")
    print("Seleccione abajo")
    print(" ")
    user_input = int(input("1 - Centímetros a Pulgadas \n2 - Pulgadas a Centímetros \n3 - Pulgadas a Pies \n4 - Pies a Pulgadas \n5 - Pies a Yardas \n6 - Yardas a Pies \n¿Qué tasa de conversión eliges?: "))
    if user_input == 1:
        print("_________________________")
        print(" ")
        print("Has seleccionado 1, centímetros a pulgadas")
        length = int(input("Ingrese la longitud: "))
        conversion = length * (units_convert[0])
        print(" ")
        print("La longitud ahora se convertirá", conversion, "Pulgadas")
        continuing()
    elif user_input == 2:
        print("_________________________")
        print(" ")
        print("Has seleccionado 2, pulgadas a centímetros")
        length = int(input("Ingrese la longitud: "))
        conversion = length * (units_convert[1])
        print(" ")
        print("La longitud ahora se convertirá", conversion, "Centímetros")
        continuing()
    elif user_input == 3:
        print("_________________________")
        print(" ")
        print("Has seleccionado 3, Pulgadas a Pies")
        length = int(input("Ingrese la longitud: "))
        conversion = length * (units_convert[2])
        print(" ")
        print("La longitud ahora se convertirá", conversion, "Pies")
        continuing()
    elif user_input == 4:
        print("_________________________")
        print(" ")
        print("Has seleccionado 4, pies a pulgadas")
        length = int(input("Ingrese la longitud: "))
        conversion = length * (units_convert[3])
        print(" ")
        print("La longitud ahora se convertirá", conversion, "Pulgadas")
        continuing()
    elif user_input == 5:
        print("_________________________")
        print(" ")
        print("Has seleccionado 5, pies a yardas")
        length = int(input("Ingrese la longitud: "))
        conversion = length * (units_convert[4])
        print(" ")
        print("La longitud ahora se convertirá", conversion, "Yardas")
        continuing()
    elif user_input == 6:
        print("_________________________")
        print(" ")
        print("Has seleccionado 6, yardas a pies")
        length = int(input("Ingrese la longitud: "))
        conversion = length * (units_convert[5])
        print(" ")
        print("La longitud ahora se convertirá", conversion, "Pies")
        continuing()
    else:
        print("Esa no era una de las opciones")
        units()



def continuing():
    print("_________________________")
    print(" ")
    print("Would you like to restart the app?")
    user_input = (input("Enter y for yes or n for no: "))
    if user_input != ('y' or 'Y'):
        print("_________________________")
        print(" ")
        print("Okay, have a great day", name, "!")
    elif user_input == ('y' or 'Y'):
        english()


def continuo():
    print("_________________________")
    print(" ")
    print("¿Quieres reiniciar la aplicación?")
    user_input = (input("Ingrese s para sí o n para no: "))
    if user_input != ('s' or 'S'):
        print("_________________________")
        print(" ")
        print("Está bien, que tengas un gran día", name, "!")
    elif user_input == ('s' or 'S'):
        spanish()


main()
