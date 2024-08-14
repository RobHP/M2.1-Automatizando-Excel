# Este programa abre un archivo de Excel llamado "calificaciones_alumnos.xlsx",
# agrega una columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100 con un decimal,
# y guarda el archivo actualizado.

import pandas as pd
import numpy as np

# Cargar el archivo Excel
file_path = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(file_path)

# Generar valores aleatorios entre 0 y 100 con un decimal para la nueva columna "Mat_Fisica"
np.random.seed(0)  # Para reproducibilidad, opcional
df['Mat_Fisica'] = np.random.uniform(0, 100, df.shape[0]).round(1)

# Guardar el DataFrame actualizado en un nuevo archivo Excel
df.to_excel('calificaciones_alumnos_actualizado.xlsx', index=False)

print("Columna 'Mat_Fisica' agregada y archivo guardado como 'calificaciones_alumnos_actualizado.xlsx'")
