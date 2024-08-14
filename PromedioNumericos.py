# Este programa abre un archivo de Excel llamado "calificaciones_alumnos.xlsx",
# identifica los campos numéricos y calcula el promedio de cada uno de esos campos.

import pandas as pd

# Cargar el archivo Excel
file_path = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(file_path)

# Identificar campos numéricos
campos_numericos = df.select_dtypes(include=[float, int]).columns.tolist()

# Imprimir los campos numéricos
print(f"Los campos numéricos son: {campos_numericos}")

# Calcular el promedio de cada campo numérico
promedios = df[campos_numericos].mean()

# Imprimir los promedios de los campos numéricos
print("Promedios de los campos numéricos:")
for campo, promedio in promedios.items():
    print(f"{campo}: {promedio:.2f}")
