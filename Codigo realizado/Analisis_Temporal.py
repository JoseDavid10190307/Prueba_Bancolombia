import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos desde la ruta local 
file_path = r"C:\Jose\Pruebas Empresas\Prueba Tecnica Aprendiz U_Bancolombia\Lemonade.txt" # Reemplazar con la ruta correcta
df = pd.read_csv(file_path, sep=",")

# Conversión de la columna 'Date' a formato datetime
df['Fecha'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce', dayfirst=True)

# Identificación de fechas que no se pudieron convertir
invalid_dates = df[df['Fecha'].isna()]

# Intentar convertir fechas que son en formato 'mes/día/año'
for index, row in invalid_dates.iterrows():
    try:
        # Intentar convertir la fecha en el formato 'mes/día/año'
        df.at[index, 'Fecha'] = pd.to_datetime(row['Date'], format='%m/%d/%Y', errors='coerce')
    except Exception as e:
        print(f"No se pudo convertir la fecha {row['Date']} en ninguna de las conversiones.")

# Análisis de ventas promedio por día de la semana
df['Día'] = pd.to_datetime(df['Fecha']).dt.day_name()
ventas_por_dia = df.groupby('Día')['Sales'].mean().sort_values(ascending=False)

# Graficando ventas promedio por día de la semana
plt.figure(figsize=(10, 5))
ventas_por_dia.plot(kind='bar', color='skyblue')
plt.title('Ventas Promedio por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Ventas Promedio')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Cambios de temperatura y ventas promedio por mes
df['Mes'] = pd.to_datetime(df['Fecha']).dt.month
df['Año'] = pd.to_datetime(df['Fecha']).dt.year

# Calculando temperatura y ventas promedio por mes
temperatura_por_mes = df.groupby('Mes')['Temperature'].mean()
ventas_por_mes = df.groupby('Mes')['Sales'].mean()

# Graficando temperaturas y ventas promedio por mes
plt.figure(figsize=(12, 6))
plt.plot(temperatura_por_mes.index, temperatura_por_mes, label='Temperatura Promedio', marker='o')
plt.plot(ventas_por_mes.index, ventas_por_mes, label='Ventas Promedio', marker='o')
plt.title('Temperatura y Ventas Promedio por Mes')
plt.xlabel('Mes')
plt.ylabel('Valores Promedio')
plt.xticks(ticks=range(1, 13), labels=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.legend()
plt.grid()
plt.show()

# Graficando ventas a lo largo del tiempo
ventas_tiempo = df.groupby('Fecha')['Sales'].sum()

plt.figure(figsize=(14, 7))
plt.plot(ventas_tiempo.index, ventas_tiempo, label='Ventas Diarias', color='blue', linewidth=2)
plt.title('Ventas a lo Largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Total de Ventas')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()