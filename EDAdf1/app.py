import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel (asegúrate de cambiar 'archivo.xlsx' por el nombre de tu archivo)
archivo_excel = 'dataset_aleatorio.xlsx'
df = pd.read_excel(archivo_excel)

# Asegúrate de que la columna 'Ingreso' esté presente en tu archivo
if 'Ingreso' not in df.columns:
    print("La columna 'Ingreso' no se encontró en el archivo.")
else:
    # Extraer la columna 'Ingreso'
    ingresos = df['Ingreso'].dropna()  # Ignorar valores nulos si existen

    # Calcular estadísticas
    media = ingresos.mean()
    mediana = ingresos.median()
    varianza = ingresos.var()
    desviacion = ingresos.std()
    cuartiles = ingresos.quantile([0.25, 0.5, 0.75])
    quintiles = ingresos.quantile([0.2, 0.4, 0.6, 0.8])

    # Imprimir resultados
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Varianza: {varianza:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")
    print("\nCuartiles:")
    print(cuartiles)
    print("\nQuintiles:")
    print(quintiles)

    # Crear un box plot para la columna 'Ingreso'
    plt.figure(figsize=(8, 6))  # Tamaño de la figura
    sns.boxplot(data=ingresos, color='skyblue')  # Crear el box plot
    plt.title("Box Plot de la Columna 'Ingreso'")  # Título
    plt.xlabel('Ingreso')  # Etiqueta del eje X
    plt.ylabel('Valor')  # Etiqueta del eje Y

    # Mostrar la gráfica
    plt.show()
