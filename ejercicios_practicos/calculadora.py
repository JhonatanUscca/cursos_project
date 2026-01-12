"""
Calculadora Interactiva
Objetivo: Practicar bucles, condicionales, funciones simples y manejo de errores
"""


def sumar(a, b):
    """Función para sumar dos números"""
    return a + b


def restar(a, b):
    """Función para restar dos números"""
    return a - b


def multiplicar(a, b):
    """Función para multiplicar dos números"""
    return a * b


def dividir(a, b):
    """Función para dividir dos números con manejo de error"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def obtener_numero(mensaje):
    """
    Función para obtener un número del usuario con manejo de errores
    Patrón común: validación con try/except y bucle hasta éxito
    """
    while True:  # Bucle infinito hasta obtener un número válido
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Por favor ingresa un número válido")
            # El bucle continúa hasta que se ingrese un número válido


def mostrar_menu():
    """Función para mostrar el menú de opciones"""
    print("\n" + "="*40)
    print("CALCULADORA")
    print("="*40)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("="*40)


def realizar_operacion(operacion, num1, num2):
    """
    Función que usa condicionales para ejecutar la operación seleccionada
    Patrón común: if/elif/else para múltiples opciones
    """
    if operacion == 1:
        resultado = sumar(num1, num2)
        simbolo = "+"
    elif operacion == 2:
        resultado = restar(num1, num2)
        simbolo = "-"
    elif operacion == 3:
        resultado = multiplicar(num1, num2)
        simbolo = "*"
    elif operacion == 4:
        resultado = dividir(num1, num2)
        simbolo = "/"
    else:
        return None, None
    
    return resultado, simbolo


def main():
    """
    Función principal que demuestra el patrón común:
    - while True con break para salir del programa
    - Manejo de errores con try/except
    - Condicionales para validar entrada
    """
    print("¡Bienvenido a la Calculadora!")
    
    # Patrón común: while True con break para crear un bucle principal
    while True:
        mostrar_menu()
        
        try:
            # Obtener la opción del usuario
            opcion = input("Selecciona una opción (1-5): ").strip()
            
            # Condicional para salir del programa
            if opcion == "5":
                print("\n¡Gracias por usar la calculadora! ¡Hasta luego!")
                break  # Sale del bucle while True
            
            # Validar que la opción sea un número entre 1 y 4
            if opcion not in ["1", "2", "3", "4"]:
                print("Error: Opción no válida. Por favor selecciona 1, 2, 3, 4 o 5")
                continue  # Vuelve al inicio del bucle
            
            # Convertir opción a entero
            opcion = int(opcion)
            
            # Obtener los números usando la función con manejo de errores
            num1 = obtener_numero("Ingresa el primer número: ")
            num2 = obtener_numero("Ingresa el segundo número: ")
            
            # Realizar la operación
            resultado, simbolo = realizar_operacion(opcion, num1, num2)
            
            # Manejo de error para división por cero
            if resultado is None:
                print("Error: Operación no válida")
            else:
                print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}")
                
        except KeyboardInterrupt:
            # Manejo de error para interrupción del usuario (Ctrl+C)
            print("\n\nPrograma interrumpido por el usuario")
            break
        except Exception as e:
            # Manejo genérico de errores
            print(f"Error inesperado: {e}")
            print("Por favor intenta de nuevo")


# Patrón común: verificar si el script se ejecuta directamente
if __name__ == "__main__":
    main()
