# Este programa abre un archivo de Excel llamado "calificaciones_alumnos.xlsx",
# cuenta los registros y campos de la tabla, identifica los campos numéricos,
# agrega una columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100 con un decimal,
# ordena la tabla por la columna "Nombre", y guarda el archivo actualizado.

import pandas as pd
import numpy as np

# Cargar el archivo Excel
file_path = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(file_path)

# Contar el número de registros y campos
num_registros = df.shape[0]
num_campos = df.shape[1]

# Imprimir el número de registros y campos
print(f"El archivo tiene {num_registros} registros y {num_campos} campos.")

# Identificar campos numéricos
campos_numericos = df.select_dtypes(include=[np.number]).columns.tolist()

# Imprimir los campos numéricos
print(f"Los campos numéricos son: {campos_numericos}")

# Generar valores aleatorios entre 0 y 100 con un decimal para la nueva columna "Mat_Fisica"
np.random.seed(0)  # Para reproducibilidad, opcional
