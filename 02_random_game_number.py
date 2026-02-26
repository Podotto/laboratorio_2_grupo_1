import random

def main():
   
    number_secret = random.randint(1, 100)
    attempts = 0
    guess = False

    print("¡Bienvenido al juego de adivinar el número!")
    print("He pensado un número entre 1 y 100. Intenta adivinarlo.")

    while not guess:
        attempts = int(input("Ingresa tu número: "))
        attempts += 1

        if attempts == number_secret:
            print(f"¡Correcto! El número era {number_secret}. Lo lograste en {attempts} intentos.")
            adivinado = True
        elif attempts < number_secret:
            print("El número secreto es mayor. Intenta otra vez.")
        else:
            print("El número secreto es menor. Intenta otra vez.")

if __name__ == "__main__":
    main()