# Este programa lee un archivo Excel llamado "calificaciones_alumnos.xlsx" que contiene las calificaciones de varios alumnos
# en diferentes materias. Luego, genera una gráfica de barras para cada materia mostrando las calificaciones de cada alumno,
# asegurándose de que las etiquetas en el eje X no se encimen.

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel
df = pd.read_excel("calificaciones_alumnos.xlsx")

# Extraer nombres de alumnos y calificaciones
nombres = df['Nombre']
calculo_integral = df['Mat_CalculoIntegral']
programacion_oop = df['Mat_ProgramacionOOP']
estructura_datos = df['Mat_EstructuraDatos']

# Definir el ancho de las barras
bar_width = 0.2

# Crear una figura y ejes para la gráfica
fig, ax = plt.subplots(figsize=(10, 6))

# Posición de las barras en el eje X
r1 = range(len(nombres))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Graficar las barras para cada materia
ax.bar(r1, calculo_integral, color='blue', width=bar_width, edgecolor='grey', label='Cálculo Integral')
ax.bar(r2, programacion_oop, color='green', width=bar_width, edgecolor='grey', label='Programación OOP')
ax.bar(r3, estructura_datos, color='red', width=bar_width, edgecolor='grey', label='Estructura de Datos')

# Añadir etiquetas y título
ax.set_xlabel('Alumnos', fontweight='bold')
ax.set_ylabel('Calificaciones', fontweight='bold')
ax.set_title('Calificaciones de los Alumnos en Diferentes Materias')
ax.set_xticks([r + bar_width for r in range(len(nombres))])
ax.set_xticklabels(nombres, rotation=45, ha='right')  # Rotar las etiquetas para que no se encimen

# Añadir una leyenda
ax.legend()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
