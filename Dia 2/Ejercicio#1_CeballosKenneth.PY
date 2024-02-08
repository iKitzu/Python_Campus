def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence


def main():
    print("¡Bienvenido al generador de la Secuencia de Fibonacci!")
    print("La Secuencia de Fibonacci comienza con 0 y 1, y cada término subsiguiente es la suma de los dos términos anteriores.")

    while True:
        try:
            n = int(input("Ingrese un valor entero para generar la secuencia hasta ese término (ingrese 0 para salir): "))
            
            if n < 0:
                print("Por favor, ingrese un valor no negativo.")
                continue

            if n == 0:
                print("¡Hasta luego! Gracias por usar el generador de Fibonacci.")
                break

            sequence = fibonacci(n)
            print(f"Secuencia de Fibonacci hasta el término {n}: {sequence}")

        except ValueError:
            print("Por favor, ingrese un valor entero válido.")

if __name__ == "__main__":
    main()
