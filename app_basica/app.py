from flask import Flask, request, redirect, render_template
import json
import os

app = Flask(__name__)

# ===== Datos =====
tareas = []
siguiente_id = 1
DATOS_FILE = 'tareas.json'

# ===== Funciones de persistencia =====
def guardar_datos():
    with open(DATOS_FILE, 'w') as f:
        json.dump({'siguiente_id': siguiente_id, 'tareas': tareas}, f)

def cargar_datos():
    global tareas, siguiente_id
    if os.path.exists(DATOS_FILE):
        with open(DATOS_FILE, 'r') as f:
            data = json.load(f)
            tareas = data['tareas']
            siguiente_id = data['siguiente_id']

# ===== Funciones de gestión de tareas =====
def agregar_tarea(texto):
    global siguiente_id
    tareas.append({'id': siguiente_id, 'texto': texto, 'hecho': False})
    siguiente_id += 1
    guardar_datos()

def completar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = True
            break
    guardar_datos()

# ===== Rutas =====
@app.route('/')
def index():
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)

@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

# ===== Inicialización =====
if __name__ == '__main__':
    cargar_datos()
    app.run(debug=True)
