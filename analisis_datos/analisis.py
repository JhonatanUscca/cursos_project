import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar datos del CSV
df = pd.read_csv('ventas.csv', parse_dates=['fecha'])

# Revisar tipos de datos
df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce')
df['precio'] = pd.to_numeric(df['precio'], errors='coerce')

# 2. Calcular ventas totales por mes
df['mes'] = df['fecha'].dt.to_period('M')
df['ingreso'] = df['cantidad'] * df['precio']

ventas_por_mes = df.groupby('mes')['ingreso'].sum().sort_index()
print("Ventas totales por mes:")
print(ventas_por_mes.to_frame())

# 3. Determinar producto más vendido y producto con mayores ingresos
ventas_prod = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingreso': 'sum'
})

mas_vendido = ventas_prod['cantidad'].idxmax()
mayor_ingreso = ventas_prod['ingreso'].idxmax()

print(f"\nProducto más vendido en unidades: {mas_vendido} (total {ventas_prod.loc[mas_vendido, 'cantidad']})")
print(f"Producto con mayores ingresos: {mayor_ingreso} (total {ventas_prod.loc[mayor_ingreso, 'ingreso']:.2f} €)")

# 4. Graficar ventas por mes
ventas_por_mes.index = ventas_por_mes.index.astype(str)

plt.figure(figsize=(6,4))
ventas_por_mes.plot(kind='bar')
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ingresos (€)")
plt.tight_layout()
plt.savefig("ventas_por_mes.png")
plt.show()

# 5. Graficar top 5 productos por ingresos
top5 = ventas_prod.nlargest(5, 'ingreso')

plt.figure(figsize=(6,4))
plt.bar(top5.index, top5['ingreso'])
plt.title("Top 5 Productos por Ingresos")
plt.xlabel("Producto")
plt.ylabel("Ingresos (€)")
plt.tight_layout()
plt.savefig("top5_productos.png")
plt.show()
