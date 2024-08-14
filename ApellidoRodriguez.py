# Este programa abre un archivo de Excel llamado "calificaciones_alumnos.xlsx",
# cuenta los registros y campos de la tabla, identifica los campos numéricos,
# agrega una columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100 con un decimal,
# ordena la tabla por la columna "Nombre", guarda el archivo actualizado,
# y lista todos los alumnos que se apellidan "Rodriguez".

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
df['Mat_Fisica'] = np.random.uniform(0, 100, df.shape[0]).round(1)

# Ordenar la tabla por la columna "Nombre"
df = df.sort_values(by='Nombre')

# Guardar el DataFrame actualizado en un nuevo archivo Excel
df.to_excel('calificaciones_alumnos_actualizado.xlsx', index=False)

print("Columna 'Mat_Fisica' agregada, tabla ordenada por 'Nombre', y archivo guardado como 'calificaciones_alumnos_actualizado.xlsx'")

# Filtrar los alumnos que se apellidan "Rodriguez"
alumnos_rodriguez = df[df['Nombre'].str.contains('Rodríguez', case=False, na=False)]

# Imprimir los alumnos que se apellidan "Rodriguez"
print("Alumnos que se apellidan 'Rodriguez':")
print(alumnos_rodriguez)
