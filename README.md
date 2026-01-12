# Cursor con Python: Desarrollo Inteligente con IA

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Cursor](https://img.shields.io/badge/Cursor-AI%20Powered-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📚 Introducción

En los últimos años, los entornos de desarrollo han evolucionado desde simples editores de texto hasta completos IDE inteligentes. Con la irrupción de la inteligencia artificial, ahora es posible contar con asistentes de código integrados que ayudan a escribir, comprender y mejorar programas. 

**Cursor** es un editor de código potenciado por IA que ejemplifica esta nueva generación de herramientas. Este manual pedagógico cubrirá en profundidad el uso de Cursor enfocado en el desarrollo en Python, orientado a alumnos principiantes en programación asistida por IA. 

A lo largo de sus módulos, aprenderás desde los fundamentos de Cursor, su instalación y funciones básicas, hasta flujos de trabajo avanzados, comparación con otros entornos (VS Code, PyCharm, Jupyter) y el desarrollo de proyectos completos empleando esta herramienta.

## 🔗 Repositorio

**GitHub:** [https://github.com/JhonatanUscca/cursos_project](https://github.com/JhonatanUscca/cursos_project)

## 📋 Índice de Contenidos

### Fundamentos y Masterclass

1. **Introducción a Cursor**
   - ¿Qué es Cursor?
   - Instalación y configuración inicial
   - Diferencias con otros editores (VS Code, PyCharm, Jupyter)

2. **Explorando la Interfaz y Funcionalidades Clave**
   - Navegación básica
   - Comandos de IA integrados
   - Autocompletado inteligente
   - Generación de código con IA

3. **Desarrollo con Python en Cursor**
   - Configuración del entorno Python
   - Trabajo con proyectos Python
   - Debugging y testing
   - Gestión de dependencias

4. **Flujo de Trabajo Avanzado**
   - Refactorización asistida por IA
   - Generación de documentación
   - Optimización de código
   - Integración con Git

5. **Implementación y Despliegue**
   - Preparación de proyectos para producción
   - Mejores prácticas
   - Deployment de aplicaciones

6. **Casos de Uso**
   - Proyectos prácticos incluidos
   - Ejemplos reales de desarrollo con IA

## 🚀 Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- Cursor IDE instalado ([Descargar Cursor](https://cursor.sh/))
- Git (opcional, para control de versiones)

### Instalación de Dependencias

Este proyecto utiliza varias librerías de Python. Para instalar todas las dependencias necesarias, ejecuta:

```bash
pip install -r requirements.txt
```

O instala las librerías individualmente según el proyecto que quieras ejecutar:

#### Librerías Principales

**Para Análisis de Datos:**
```bash
pip install pandas matplotlib numpy
```

**Para Aplicaciones Web:**
```bash
pip install flask
```

**Para Procesamiento de PDFs:**
```bash
pip install PyPDF2
```

**Librerías Estándar (incluidas en Python):**
- `pathlib` - Manejo de rutas y archivos
- `json` - Procesamiento de JSON
- `os` - Operaciones del sistema
- `re` - Expresiones regulares
- `collections` - Estructuras de datos avanzadas
- `tkinter` - Interfaz gráfica (incluida en Python estándar)

### Instalación Completa (Recomendada)

```bash
# Clonar el repositorio
git clone https://github.com/JhonatanUscca/cursos_project.git
cd cursos_project

# Instalar todas las dependencias
pip install pandas matplotlib numpy flask PyPDF2
```

## 📁 Estructura del Proyecto

```
cursos_project/
│
├── ejercicios_practicos/          # Ejercicios básicos de Python
│   ├── calculadora.py             # Calculadora interactiva
│   ├── FizzBuzz.py                # Ejercicio de lógica condicional
│   ├── analisis.py                # Análisis de datos básico
│   └── datos_*.csv                # Datos de ejemplo
│
├── app_basica/                     # Aplicación web Flask
│   ├── app.py                     # Aplicación principal
│   ├── templates/                  # Plantillas HTML
│   └── tareas.json                 # Base de datos JSON
│
├── proyecto_automatizacion/        # Scripts de automatización
│   ├── organizar.py               # Organizador de archivos
│   └── archivos_prueba/           # Carpeta de prueba (ignorada por Git)
│
├── analisis_datos/                 # Proyectos de análisis
│   ├── analisis.py                # Script de análisis
│   └── ventas.csv                 # Datos de ejemplo
│
├── contador_palabras/              # Utilidad de conteo
│   ├── contador.py                # Contador de palabras
│   └── *.txt                      # Archivos de texto de ejemplo
│
├── ejemplo/                        # Ejemplos diversos
│   ├── primo.py                   # Verificación de números primos
│   ├── ejercicio_autocompletar.py # Ejemplo de autocompletado
│   └── main.py                    # Ejemplos varios
│
└── ejemplo_extra/                  # Ejemplos adicionales
    ├── notas.py                   # Aplicación con Tkinter
    └── ejemplo.txt                # Archivos de ejemplo
```

## 🎯 Proyectos Incluidos

### 1. Calculadora Interactiva
**Ubicación:** `ejercicios_practicos/calculadora.py`

Calculadora que demuestra:
- Bucles (`while`, `break`)
- Condicionales (`if/elif/else`)
- Funciones simples
- Manejo de errores

**Ejecutar:**
```bash
python ejercicios_practicos/calculadora.py
```

### 2. FizzBuzz - Análisis de Lógica Condicional
**Ubicación:** `ejercicios_practicos/FizzBuzz.py`

Demuestra la importancia del orden de condiciones con múltiples implementaciones (correctas e incorrectas).

**Ejecutar:**
```bash
python ejercicios_practicos/FizzBuzz.py
```

### 3. Análisis de Datos con Pandas y Matplotlib
**Ubicación:** `ejercicios_practicos/analisis.py`

Análisis básico de datos CSV que muestra:
- Lectura de archivos CSV
- Cálculo de estadísticas (media, mediana, desviación estándar)
- Generación de gráficos de dispersión

**Ejecutar:**
```bash
python ejercicios_practicos/analisis.py
```

### 4. Aplicación Web Flask
**Ubicación:** `app_basica/app.py`

Aplicación web simple para gestión de tareas que demuestra:
- Desarrollo web con Flask
- Persistencia de datos con JSON
- Templates HTML

**Ejecutar:**
```bash
cd app_basica
python app.py
```
Luego abre `http://localhost:5000` en tu navegador.

### 5. Organizador de Archivos
**Ubicación:** `proyecto_automatizacion/organizar.py`

Script que organiza archivos automáticamente por tipo en carpetas.

**Ejecutar:**
```bash
python proyecto_automatizacion/organizar.py
```

## 💡 Características Destacadas

### ✨ Desarrollo Asistido por IA
- Autocompletado inteligente
- Generación de código contextual
- Refactorización automática
- Explicación de código

### 🎓 Enfoque Pedagógico
- Ejercicios progresivos
- Comentarios explicativos
- Casos de uso reales
- Mejores prácticas

### 🔧 Herramientas Modernas
- Integración con Git
- Debugging avanzado
- Gestión de dependencias
- Testing integrado

## 📖 Cómo Usar Este Repositorio

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/JhonatanUscca/cursos_project.git
   ```

2. **Navega al directorio:**
   ```bash
   cd cursos_project
   ```

3. **Instala las dependencias:**
   ```bash
   pip install pandas matplotlib numpy flask PyPDF2
   ```

4. **Explora los proyectos:**
   - Cada carpeta contiene un proyecto independiente
   - Lee los comentarios en cada archivo para entender el código
   - Ejecuta los scripts para verlos en acción

5. **Experimenta con Cursor:**
   - Abre el proyecto en Cursor
   - Usa el autocompletado de IA
   - Pide a la IA que explique o mejore el código
   - Experimenta con diferentes comandos de IA

## 🛠️ Comandos Útiles de Cursor

- `Ctrl + K` - Generar código con IA
- `Ctrl + L` - Chat con IA
- `Ctrl + Shift + L` - Editar selección con IA
- `Ctrl + I` - Comando inline de IA

## 📝 Notas Importantes

- Los archivos en `archivos_prueba/` están excluidos del repositorio (ver `.gitignore`)
- Algunos proyectos requieren archivos de datos (CSV, TXT) que se generan automáticamente
- Los gráficos generados se guardan en el mismo directorio del script

## 🤝 Contribuciones

Este es un proyecto educativo. Siéntete libre de:
- Hacer fork del proyecto
- Crear ramas para experimentar
- Proponer mejoras
- Compartir tus propios ejercicios

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Jhonatan Uscca**
- GitHub: [@JhonatanUscca](https://github.com/JhonatanUscca)
- Repositorio: [cursos_project](https://github.com/JhonatanUscca/cursos_project)

## 🙏 Agradecimientos

Este proyecto forma parte del curso "Cursor con Python: Desarrollo Inteligente con IA" con Alberto Matilla.

---

**⭐ Si este proyecto te ha sido útil, considera darle una estrella en GitHub!**
