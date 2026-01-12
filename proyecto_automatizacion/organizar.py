from pathlib import Path

# 1. Carpeta objetivo (relativa al directorio del script)
# La carpeta está en el mismo directorio que este script
carpeta_objetivo = Path(__file__).parent / "archivos_prueba"

# Verificar si la carpeta existe, si no, crearla
if not carpeta_objetivo.exists():
    print(f"⚠️  La carpeta '{carpeta_objetivo}' no existe.")
    respuesta = input("¿Deseas crearla? (s/n): ").strip().lower()
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        carpeta_objetivo.mkdir(parents=True, exist_ok=True)
        print(f"✅ Carpeta '{carpeta_objetivo}' creada exitosamente.")
        print("💡 Coloca algunos archivos en esta carpeta y vuelve a ejecutar el script.")
    else:
        print("❌ No se puede continuar sin la carpeta. Saliendo...")
        exit(1)
elif not carpeta_objetivo.is_dir():
    print(f"❌ Error: '{carpeta_objetivo}' existe pero no es una carpeta.")
    exit(1)

# 2. Categorías de archivos
categorias = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
}

# 3. Crear un diccionario extensión -> categoría para búsqueda rápida
extension_a_categoria = {}
for categoria, exts in categorias.items():
    for ext in exts:
        extension_a_categoria[ext.lower()] = categoria

categorias_predeterminadas = ["Otros"]  # Para lo que no encaje

# 4. Listar archivos (solo archivos, no carpetas)
try:
    archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]
except PermissionError:
    print(f"❌ Error: No tienes permisos para acceder a '{carpeta_objetivo}'")
    exit(1)

# 5. Verificar si hay archivos para organizar
if not archivos:
    print(f"ℹ️  No hay archivos para organizar en '{carpeta_objetivo}'")
    print("💡 Coloca algunos archivos en esta carpeta y vuelve a ejecutar el script.")
    exit(0)

print(f"\n📁 Encontrados {len(archivos)} archivo(s) para organizar...\n")

# 6. Mover cada archivo a su categoría
archivos_movidos = 0
for archivo in archivos:
    # Evitar mover el script mismo
    if archivo.name == "organizar.py":
        continue

    try:
        ext = archivo.suffix.lower()
        categoria = extension_a_categoria.get(ext, "Otros")
        destino_dir = carpeta_objetivo / categoria
        destino_dir.mkdir(exist_ok=True)  # Crea la carpeta si no existe
        archivo.rename(destino_dir / archivo.name)
        print(f"✅ Movido: {archivo.name} → {categoria}/")
        archivos_movidos += 1
    except Exception as e:
        print(f"❌ Error al mover {archivo.name}: {e}")

print(f"\n🎉 ¡Organización completada! {archivos_movidos} archivo(s) movido(s).")
