
respuesta = "si"
while respuesta == "si":
    sentence = str(input("Escribe una cadena de caracteres"))
    option = str(input("Elige la opcion que mas quieras: minusculas(m) o mayusculas(M)."))
    if option == "m":
        print(sentence.lower())
    elif option == "M":
        print(sentence.upper())
    elif option != "m" or "M":
        print("Tienes que escoger entre m y M")
        for option in range(2):
            option = str(input("Elige la opcion que mas quieras: minusculas(m) o mayusculas(M)."))
            if option == "m":
                print(sentence.lower())
                break
            elif option == "M":
                print(sentence.upper())
                break
            else:
                print("No es correcto")
    respuesta = input("¿Quieres volver a introducir otra cadena de caracteres? Si(si) o No(no)")
    if respuesta != "si" and "no":
        print("Eleccion incorrecta")
        print("SALIENDO ...")

print(50 * "-")

print("Gracias por usar nuestros servicios.")