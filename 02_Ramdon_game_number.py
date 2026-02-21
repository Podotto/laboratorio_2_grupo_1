import random

def main():
   
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinar el número!")
    print("He pensado un número entre 1 y 100. Intenta adivinarlo.")

    while not adivinado:
        intento = int(input("Ingresa tu número: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Correcto! El número era {numero_secreto}. Lo lograste en {intentos} intentos.")
            adivinado = True
        elif intento < numero_secreto:
            print("El número secreto es mayor. Intenta otra vez.")
        else:
            print("El número secreto es menor. Intenta otra vez.")

if __name__ == "__main__":
    main()