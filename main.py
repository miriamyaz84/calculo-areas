from area import calcular_area_cuadrado, calcular_area_circulo, calcular_area_triangulo

def main():
    while True:
        print("\n=== Calculadora de Áreas ===")
        print("1. Calcular área de un Cuadrado")
        print("2. Calcular área de un Círculo")
        print("3. Calcular área de un Triángulo")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            try:
                lado = float(input("Ingresa el lado del cuadrado: "))
                area = calcular_area_cuadrado(lado)
                if area is not None:
                    print(f"Área del cuadrado: {area:.2f}")
                else:
                    print("Error: el lado debe ser mayor que 0.")
            except ValueError:
                print("Error: debes ingresar un número válido.")

        elif opcion == "2":
            try:
                radio = float(input("Ingresa el radio del círculo: "))
                area = calcular_area_circulo(radio)
                if area is not None:
                    print(f"Área del círculo: {area:.2f}")
                else:
                    print("Error: el radio debe ser mayor que 0.")
            except ValueError:
                print("Error: debes ingresar un número válido.")

        elif opcion == "3":
            try:
                base = float(input("Ingresa la base del triángulo: "))
                altura = float(input("Ingresa la altura del triángulo: "))
                area = calcular_area_triangulo(base, altura)
                if area is not None:
                    print(f"Área del triángulo: {area:.2f}")
                else:
                    print("Error: base y altura deben ser mayores que 0.")
            except ValueError:
                print("Error: debes ingresar números válidos.")

        elif opcion == "4":
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
