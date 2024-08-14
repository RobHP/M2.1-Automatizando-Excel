# Este programa abre un archivo de Excel llamado "calificaciones_alumnos.xlsx",
# identifica los campos numéricos y calcula el promedio del campo "Promedio".

import pandas as pd

# Cargar el archivo Excel
file_path = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(file_path)

# Identificar campos numéricos
campos_numericos = df.select_dtypes(include=[float, int]).columns.tolist()

# Imprimir los campos numéricos
print(f"Los campos numéricos son: {campos_numericos}")

# Calcular el promedio del campo "Promedio"
promedio_campo = df['Promedio'].mean()

# Imprimir el promedio del campo "Promedio"
print(f"El promedio del campo 'Promedio' es: {promedio_campo:.2f}")
