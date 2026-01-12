"""
Ejercicio C: Análisis de Datos Básico

Este script:
1. Lee un archivo CSV con dos columnas de números
2. Calcula estadísticas simples: media, mediana, desviación estándar
3. Genera un gráfico de dispersión (scatter plot) de una columna vs. la otra

Demuestra cómo Cursor puede ayudarte con pandas y matplotlib
sin necesidad de recordar toda la sintaxis.
"""

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    LIBRERIAS_DISPONIBLES = True
except ImportError as e:
    print(f"⚠️  Error al importar librerías: {e}")
    print("Por favor instala las librerías necesarias:")
    print("  pip install pandas matplotlib")
    LIBRERIAS_DISPONIBLES = False


def leer_csv(archivo_csv):
    """
    Lee un archivo CSV usando pandas
    Cursor puede ayudarte a escribir esto con solo pedirle: "lee un CSV con pandas"
    """
    try:
        # pandas hace muy fácil leer un CSV
        df = pd.read_csv(archivo_csv)
        print(f"✅ Archivo leído correctamente: '{archivo_csv}'")
        print(f"\nPrimeras filas del dataset:")
        print(df.head())
        print(f"\nForma del dataset: {df.shape[0]} filas, {df.shape[1]} columnas")
        return df
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{archivo_csv}'")
        print("\n💡 Puedes crear un archivo CSV de ejemplo con dos columnas numéricas.")
        print("   Por ejemplo, crea 'datos.csv' con contenido como:")
        print("   col1,col2")
        print("   10,20")
        print("   15,25")
        print("   20,30")
        return None
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None


def calcular_estadisticas(df):
    """
    Calcula estadísticas simples: media, mediana, desviación estándar
    de cada columna numérica
    
    Puedes pedirle a Cursor: "calcula media, mediana y desviación estándar"
    """
    print("\n" + "="*60)
    print("ESTADÍSTICAS DESCRIPTIVAS")
    print("="*60)
    
    # Seleccionar solo las columnas numéricas
    columnas_numericas = df.select_dtypes(include=['number']).columns.tolist()
    
    if len(columnas_numericas) < 2:
        print("❌ Error: El CSV debe tener al menos 2 columnas numéricas")
        return
    
    # Calcular estadísticas para cada columna
    for columna in columnas_numericas:
        media = df[columna].mean()
        mediana = df[columna].median()
        desviacion = df[columna].std()
        minimo = df[columna].min()
        maximo = df[columna].max()
        
        print(f"\n📊 Columna: {columna}")
        print(f"   Media:          {media:.2f}")
        print(f"   Mediana:        {mediana:.2f}")
        print(f"   Desv. Estándar: {desviacion:.2f}")
        print(f"   Mínimo:         {minimo:.2f}")
        print(f"   Máximo:         {maximo:.2f}")
    
    return columnas_numericas


def crear_scatter_plot(df, col1, col2):
    """
    Crea un gráfico de dispersión (scatter plot) de col1 vs. col2
    
    Puedes pedirle a Cursor: "Traza un scatter plot de col1 vs. col2"
    y la IA escribirá el código de matplotlib por ti
    """
    print(f"\n📈 Generando gráfico de dispersión: {col1} vs. {col2}")
    
    # Crear la figura y el gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(df[col1], df[col2], alpha=0.6, s=100, color='steelblue', edgecolors='black', linewidth=1)
    
    # Personalizar el gráfico
    plt.xlabel(col1, fontsize=12, fontweight='bold')
    plt.ylabel(col2, fontsize=12, fontweight='bold')
    plt.title(f'Gráfico de Dispersión: {col1} vs. {col2}', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Añadir líneas de referencia para la media
    plt.axvline(x=df[col1].mean(), color='red', linestyle=':', linewidth=2, label=f'Media {col1}: {df[col1].mean():.2f}')
    plt.axhline(y=df[col2].mean(), color='green', linestyle=':', linewidth=2, label=f'Media {col2}: {df[col2].mean():.2f}')
    
    # Añadir leyenda
    plt.legend()
    
    # Ajustar layout
    plt.tight_layout()
    
    # Guardar el gráfico
    nombre_archivo = f'scatter_plot_{col1}_vs_{col2}.png'
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    print(f"✅ Gráfico guardado como '{nombre_archivo}'")
    
    # Mostrar el gráfico
    # En Cursor/VS Code, esto abrirá una ventana externa o panel de plots
    plt.show()


def crear_csv_ejemplo():
    """
    Crea un archivo CSV de ejemplo si no existe
    Esto demuestra cómo puedes crear datos de prueba
    """
    import csv
    
    nombre_archivo = 'datos_ejemplo.csv'
    datos_ejemplo = [
        ['col1', 'col2'],
        [10, 20],
        [15, 25],
        [20, 30],
        [25, 35],
        [30, 40],
        [35, 45],
        [40, 50],
        [45, 55],
        [50, 60],
        [55, 65],
        [60, 70],
        [65, 75],
        [70, 80],
        [75, 85],
        [80, 90],
    ]
    
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos_ejemplo)
    
    print(f"✅ Archivo CSV de ejemplo creado: '{nombre_archivo}'")
    return nombre_archivo


def main():
    """
    Función principal que ejecuta el análisis completo
    """
    if not LIBRERIAS_DISPONIBLES:
        print("\n❌ Las librerías necesarias no están instaladas.")
        print("Por favor instala: pip install pandas matplotlib")
        return
    
    print("="*60)
    print("ANÁLISIS DE DATOS BÁSICO CON PANDAS Y MATPLOTLIB")
    print("="*60)
    print("\nEste ejercicio demuestra:")
    print("- Cómo leer un CSV con pandas")
    print("- Cómo calcular estadísticas básicas")
    print("- Cómo crear un gráfico de dispersión con matplotlib")
    print("- Cómo Cursor puede ayudarte con la sintaxis de estas librerías")
    
    # Intentar leer el CSV
    archivo_csv = input("\n📁 Ingresa el nombre del archivo CSV (o presiona Enter para crear uno de ejemplo): ").strip()
    
    if not archivo_csv:
        print("\n💡 Creando archivo CSV de ejemplo...")
        archivo_csv = crear_csv_ejemplo()
        print("   Puedes editar este archivo o crear tu propio CSV con dos columnas numéricas")
    
    # Leer el CSV
    df = leer_csv(archivo_csv)
    
    if df is None:
        return
    
    # Calcular estadísticas
    columnas_numericas = calcular_estadisticas(df)
    
    if not columnas_numericas or len(columnas_numericas) < 2:
        return
    
    # Crear el gráfico de dispersión
    # Usar las dos primeras columnas numéricas
    col1 = columnas_numericas[0]
    col2 = columnas_numericas[1]
    
    print(f"\n📊 Usando columnas: '{col1}' y '{col2}'")
    
    # Preguntar si quiere crear el gráfico
    crear_grafico = input("\n¿Quieres crear el gráfico de dispersión? (s/n): ").strip().lower()
    
    if crear_grafico in ['s', 'si', 'sí', 'y', 'yes', '']:
        crear_scatter_plot(df, col1, col2)
        print("\n✅ Análisis completado!")
        print("\n💡 Observación:")
        print("   La IA puede escribir el código de matplotlib por ti.")
        print("   Solo necesitas describir lo que quieres: 'Traza un scatter plot de col1 vs. col2'")
    else:
        print("\n✅ Análisis completado sin generar gráfico.")


if __name__ == "__main__":
    main()
