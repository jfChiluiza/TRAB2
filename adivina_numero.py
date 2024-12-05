import random

def main():
    print("¡Bienvenido al juego de adivinar el número!")
    print("He pensado en un número entre 1 y 100.")
    print("Tienes 10 intentos para adivinarlo. ¡Buena suerte!")

    # Generar un número aleatorio entre 1 y 100
    numero_aleatorio = random.randint(1, 100)
    intentos_restantes = 10

    while intentos_restantes > 0:
        try:
            # Solicitar al usuario que ingrese un número
            intento = int(input(f"\nIngresa tu número (Intentos restantes: {intentos_restantes}): "))
            
            # Validar el intento
            if intento < 1 or intento > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue

            # Comparar el intento con el número aleatorio
            if intento == numero_aleatorio:
                print("¡Correcto! Has adivinado el número. 🎉")
                break
            elif intento < numero_aleatorio:
                print("Demasiado bajo. Intenta con un número más alto.")
            else:
                print("Demasiado alto. Intenta con un número más bajo.")

            # Reducir el número de intentos restantes
            intentos_restantes -= 1

        except ValueError:
            print("Por favor, ingresa un número válido.")

    if intentos_restantes == 0:
        print(f"\nTe has quedado sin intentos. El número era: {numero_aleatorio}")
    print("Gracias por jugar. ¡Hasta la próxima!")

if __name__ == "__main__":
    main()
