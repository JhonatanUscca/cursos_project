"""
FizzBuzz - Análisis de Lógica Condicional y Orden de Condiciones

Objetivo:
- Lógica condicional
- Orden de condiciones
- Ver límites de la IA
- Comprobar que la IA "sabe" el problema
- Aprender a revisar y corregir código generado
- No aceptar ciegamente la respuesta

Reglas del FizzBuzz:
- Si un número es divisible por 3, imprime "Fizz"
- Si es divisible por 5, imprime "Buzz"
- Si es divisible por ambos (3 y 5), imprime "FizzBuzz"
- Si no es divisible por ninguno, imprime el número

IMPORTANTE: El orden de las condiciones es CRÍTICO
"""


# ============================================================================
# VERSIÓN INCORRECTA 1: Orden incorrecto - verifica divisibilidad por 3 primero
# ============================================================================
def fizzbuzz_incorrecto_1(numero):
    """
    ❌ ERROR: Verifica divisibilidad por 3 primero
    Problema: Si un número es divisible por 3 y 5, solo imprime "Fizz"
    Ejemplo: 15 debería ser "FizzBuzz" pero será "Fizz"
    """
    if numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    elif numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"  # ⚠️ Esta línea NUNCA se ejecutará
    else:
        return str(numero)


# ============================================================================
# VERSIÓN INCORRECTA 2: Usa if separados en lugar de elif
# ============================================================================
def fizzbuzz_incorrecto_2(numero):
    """
    ❌ ERROR: Usa if separados en lugar de elif
    Problema: Puede imprimir múltiples valores o valores incorrectos
    Ejemplo: 15 imprimirá "Fizz" y "Buzz" por separado
    """
    resultado = ""
    if numero % 3 == 0:
        resultado += "Fizz"
    if numero % 5 == 0:
        resultado += "Buzz"
    if not resultado:
        resultado = str(numero)
    return resultado


# ============================================================================
# VERSIÓN INCORRECTA 3: Verifica divisibilidad por 5 primero
# ============================================================================
def fizzbuzz_incorrecto_3(numero):
    """
    ❌ ERROR: Verifica divisibilidad por 5 primero
    Problema: Si un número es divisible por 3 y 5, solo imprime "Buzz"
    Ejemplo: 15 debería ser "FizzBuzz" pero será "Buzz"
    """
    if numero % 5 == 0:
        return "Buzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"  # ⚠️ Esta línea NUNCA se ejecutará
    else:
        return str(numero)


# ============================================================================
# VERSIÓN CORRECTA: Orden correcto - verifica la condición más específica primero
# ============================================================================
def fizzbuzz_correcto(numero):
    """
    ✅ CORRECTO: Verifica la condición más específica primero
    Orden correcto: primero verificar si es divisible por AMBOS (3 y 5)
    Luego verificar condiciones individuales
    """
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return str(numero)


# ============================================================================
# VERSIÓN ALTERNATIVA CORRECTA: Usando múltiplo de 15
# ============================================================================
def fizzbuzz_correcto_alternativo(numero):
    """
    ✅ CORRECTO: Usa el múltiplo común (15 = 3 * 5)
    Esta es otra forma válida de verificar divisibilidad por ambos
    """
    if numero % 15 == 0:  # 15 es el mínimo común múltiplo de 3 y 5
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return str(numero)


# ============================================================================
# FUNCIÓN DE PRUEBA PARA COMPARAR TODAS LAS VERSIONES
# ============================================================================
def probar_implementaciones(numeros_prueba=None):
    """
    Función para probar y comparar todas las implementaciones
    Demuestra la importancia del orden de las condiciones
    """
    if numeros_prueba is None:
        # Números clave para probar: casos límite
        numeros_prueba = [1, 3, 5, 15, 30, 7, 9, 10, 21, 25, 45]
    
    print("\n" + "="*80)
    print("COMPARACIÓN DE IMPLEMENTACIONES DE FIZZBUZZ")
    print("="*80)
    print(f"{'Número':<8} {'Incorrecto 1':<15} {'Incorrecto 2':<15} {'Incorrecto 3':<15} {'Correcto':<15} {'Alt. Correcto':<15}")
    print("-"*80)
    
    for num in numeros_prueba:
        resultado1 = fizzbuzz_incorrecto_1(num)
        resultado2 = fizzbuzz_incorrecto_2(num)
        resultado3 = fizzbuzz_incorrecto_3(num)
        resultado_correcto = fizzbuzz_correcto(num)
        resultado_alt = fizzbuzz_correcto_alternativo(num)
        
        # Marcar errores
        marca_error1 = "❌" if resultado1 != resultado_correcto else "✓"
        marca_error2 = "❌" if resultado2 != resultado_correcto else "✓"
        marca_error3 = "❌" if resultado3 != resultado_correcto else "✓"
        
        print(f"{num:<8} {resultado1:<14}{marca_error1} {resultado2:<14}{marca_error2} {resultado3:<14}{marca_error3} {resultado_correcto:<15} {resultado_alt:<15}")
    
    print("="*80)
    print("\nLECCIONES APRENDIDAS:")
    print("1. El orden de las condiciones es CRÍTICO en lógica condicional")
    print("2. Siempre verifica la condición MÁS ESPECÍFICA primero")
    print("3. Usa 'elif' en lugar de múltiples 'if' cuando las condiciones son mutuamente excluyentes")
    print("4. La IA puede generar código incorrecto si no entiende bien el problema")
    print("5. SIEMPRE prueba tu código con casos límite (como 15, 30, 45)")


# ============================================================================
# FUNCIÓN PARA EJECUTAR FIZZBUZZ CON UNA IMPLEMENTACIÓN ESPECÍFICA
# ============================================================================
def ejecutar_fizzbuzz_rango(inicio, fin, funcion_fizzbuzz=fizzbuzz_correcto):
    """
    Ejecuta FizzBuzz para un rango usando la función especificada
    Permite probar diferentes implementaciones
    """
    print(f"\nFizzBuzz del {inicio} al {fin}:")
    print("-" * 40)
    
    for numero in range(inicio, fin + 1):
        resultado = funcion_fizzbuzz(numero)
        print(f"{numero:3d}: {resultado}")
    
    print("-" * 40)


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================
def main():
    """
    Función principal que demuestra diferentes implementaciones
    y permite al usuario probar y comparar
    """
    print("="*80)
    print("FIZZBUZZ - ANÁLISIS DE LÓGICA CONDICIONAL")
    print("="*80)
    print("\nEste programa demuestra:")
    print("- La importancia del ORDEN de las condiciones")
    print("- Errores comunes que la IA puede generar")
    print("- Cómo revisar y corregir código generado")
    print("- Por qué NO debes aceptar ciegamente la respuesta de la IA")
    
    while True:
        print("\n" + "="*80)
        print("MENÚ:")
        print("1. Ver comparación de todas las implementaciones (casos clave)")
        print("2. Ejecutar FizzBuzz correcto (1 a 30)")
        print("3. Ejecutar FizzBuzz incorrecto 1 (1 a 30) - Ver error")
        print("4. Ejecutar FizzBuzz incorrecto 2 (1 a 30) - Ver error")
        print("5. Ejecutar FizzBuzz incorrecto 3 (1 a 30) - Ver error")
        print("6. Probar número específico con todas las versiones")
        print("7. Salir")
        print("="*80)
        
        try:
            opcion = input("\nSelecciona una opción (1-7): ").strip()
            
            if opcion == "1":
                probar_implementaciones()
                
            elif opcion == "2":
                ejecutar_fizzbuzz_rango(1, 30, fizzbuzz_correcto)
                
            elif opcion == "3":
                print("\n⚠️ EJECUTANDO VERSIÓN INCORRECTA 1:")
                print("Observa cómo 15, 30, etc. muestran 'Fizz' en lugar de 'FizzBuzz'")
                ejecutar_fizzbuzz_rango(1, 30, fizzbuzz_incorrecto_1)
                
            elif opcion == "4":
                print("\n⚠️ EJECUTANDO VERSIÓN INCORRECTA 2:")
                print("Esta versión puede funcionar pero usa un patrón menos eficiente")
                ejecutar_fizzbuzz_rango(1, 30, fizzbuzz_incorrecto_2)
                
            elif opcion == "5":
                print("\n⚠️ EJECUTANDO VERSIÓN INCORRECTA 3:")
                print("Observa cómo 15, 30, etc. muestran 'Buzz' en lugar de 'FizzBuzz'")
                ejecutar_fizzbuzz_rango(1, 30, fizzbuzz_incorrecto_3)
                
            elif opcion == "6":
                try:
                    numero = int(input("Ingresa un número para probar: "))
                    print(f"\nProbando el número {numero}:")
                    print(f"  Incorrecto 1: {fizzbuzz_incorrecto_1(numero)}")
                    print(f"  Incorrecto 2: {fizzbuzz_incorrecto_2(numero)}")
                    print(f"  Incorrecto 3: {fizzbuzz_incorrecto_3(numero)}")
                    print(f"  Correcto:    {fizzbuzz_correcto(numero)}")
                    print(f"  Alt. Correcto: {fizzbuzz_correcto_alternativo(numero)}")
                except ValueError:
                    print("Error: Por favor ingresa un número entero válido")
                    
            elif opcion == "7":
                print("\n¡Gracias por usar el programa! Recuerda:")
                print("- Siempre revisa el código generado por la IA")
                print("- Prueba con casos límite")
                print("- El orden de las condiciones importa")
                break
            else:
                print("Error: Opción no válida. Por favor selecciona 1-7")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
