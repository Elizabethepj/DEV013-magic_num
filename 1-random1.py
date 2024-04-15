from random import randint


def request_number():
    while True:
        try:
            numero = int(input("Es tu turno. Adivina el número secreto: "))
            return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido")


def user_turn(secret_num):
    user_num = request_number()
    if user_num == secret_num:
        print("¡Felicidades! Has acertado.")
        return True
    elif user_num > secret_num:
        print("Esta vez no lo has logrado. El número es menor\n")
    else:
        print("Esta vez no lo has logrado. El número es mayor\n")
    return False


def pc_turn(secret_num):
    system_num = randint(1, 100)
    print(f"El número que la computadora ha ingresado es: {system_num}")
    if system_num == secret_num:
        print("¡La pc ha acertado!")
        return True
    elif system_num > secret_num:
        print("La pc no lo ha conseguido. El número secreto es menor.\n")
    else:
        print("La pc no lo ha conseguido. El número secreto es mayor. \n")
        return False


def play_again():
    while True:
        answer = input("¿Quieres jugar otra vez? (s/n)")
        if answer.lower() == "s":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Por favor, ingresa 's' para sí o 'n' para no.")


def magic_num():
    while True:
        secret_num = randint(1, 100)
        print(secret_num)
        user_attempts = 0
        system_attempts = 0

        print("¡Bienvenida!")
        print("Competirás con la pc para encontrar un número secreto")
        print("Este se encuentra entre el número 1 y el número 100 ")

        while True:
            user_attempts += 1
            if user_turn(secret_num):
                print(f"Lo has conseguido en el intento # {user_attempts}")
                break

            system_attempts += 1
            if pc_turn(secret_num):
                print(f"La pc lo consiguió en el intento # {system_attempts}")
                break

        if not play_again():
            print("Gracias por jugar. Hasta luego.")
            break
        # sale del bucle si la respuesta no es s


# # Llama la función
magic_num()


# def magic_num():
#     while True:  # Bucle externo para permitir jugar de nuevo
#         secret_num = randint(1, 100)
#         user_attempts = 0
#         system_attempts = 0

#         print("Bienvenida al juego del número mágico")
#         print("Competirás con la pc para encontrar el número mágico")
#         print("Este se encuentra entre el número 1 y el número 100 ")

#         while True:
#             # Turno de la usuaria
#             user_attempts += 1
#             while True:
#                 try:
#                     user_num = int(
#                         input("Es tu turno. Adivina el número mágico: "))
#                     break  # Sale del bucle si la conversión fue exitosa
#                 except ValueError:
#                     print("Por favor, ingresa un número entero válido.")

#             if user_num == secret_num:
#                 print("¡Felicidades! Has acertado.")
#                 print(f"Lo has conseguido en el intento número "
#                       f"{user_attempts}")

#                 break
#             elif user_num > secret_num:
#                 print("Esta vez no lo has conseguido. El número mágico es menor.")
#             else:
#                 print("Esta vez no lo has conseguido. El número mágico es mayor")

#             # Turno de la computadora
#             system_attempts += 1
#             system_num = randint(1, 100)
#             print(f"El número que la computadora ha ingresado es: "
#                   f"{system_num}")

#             if system_num == secret_num:
#                 print(f"En su intento nro "
#                       f"{system_attempts}, la pc lo ha conseguido")
#                 break
#             elif system_num > secret_num:
#                 print("La computadora no lo ha conseguido. El número mágico es menor.")
#             else:
#                 print("La computadora no lo ha conseguido.El número mágico es mayor")

#         # Pregunta si la usuaria quiere jugar de nuevo
#         play_again = input("¿Quieres jugar otra vez? (s/n): ")
#         if play_again.lower() != 's':
#             print("Gracias por jugar. ¡Hasta luego!")
#             break  # Sale del bucle externo si la respuesta no es 's'
