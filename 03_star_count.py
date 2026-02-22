def main():
    print("==contador de estrellas==")
    stars = int(input("Ingrese el número de estrellas: "))
    for _ in range(1, stars + 1):
        print("*")


if __name__ == "__main__":
    while True:
        main()
