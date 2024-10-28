import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

# Cargar el dataset
file_path = 'C:\Jose\Pruebas Empresas\Prueba Tecnica Aprendiz U_Bancolombia\Lemonade.txt'  # Reemplazar con la ruta correcta
data = pd.read_csv(file_path, delimiter=',') 

'''
# Mostrar las primeras filas del dataset para explorarlo
print(data.head())

# Resumen general de los datos
print(data.info())

# Descripción estadística de los datos
print(data.describe())
'''

# Análisis estadístico para las columnas numéricas
columns = ['Temperature', 'Rainfall', 'Flyers', 'Sales']

# Calculamos estadísticas básicas: media, mediana, moda, varianza, desviación estándar, percentiles
for col in columns:
    print(f"--- {col} ---")
    print(f"Media: {data[col].mean()}")
    print(f"Mediana: {data[col].median()}")
    print(f"Desviación Estándar: {data[col].std()}")
    print(f"Varianza: {data[col].var()}")
    print(f"Mínimo: {data[col].min()}")
    print(f"Máximo: {data[col].max()}")
    print(f"Percentil 25: {np.percentile(data[col], 25)}")
    print(f"Percentil 50 (Mediana): {np.percentile(data[col], 50)}")
    print(f"Percentil 75: {np.percentile(data[col], 75)}")
    print(f"Asimetría (Skewness): {skew(data[col])}") # Medidas de forma
    print(f"Curtosis (Kurtosis): {kurtosis(data[col])}") # Medidas de forma

    # Detectar outliers usando el método del rango intercuartílico (IQR)
    Q1 = np.percentile(data[col], 25)
    Q3 = np.percentile(data[col], 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
    print(f"Outliers encontrados: {len(outliers)}")
    print(outliers)
    print("\n")