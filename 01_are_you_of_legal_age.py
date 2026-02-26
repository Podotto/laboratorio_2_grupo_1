def main():
    print("===¿Eres mayor de edad?===")
    age = int(input("Ingrese su edad: "))

    if age >= 18:
        print("Eres un adulto. ¡Felicidades! Eres mayor de edad")

    elif age < 0:
        print("Error. Edad no válida.")

    else:
        print("Eres un niño. Lamentable eres menor de edad")


if __name__ == "__main__":
    while True:
        main()
