import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos desde la ruta local
file_path = r"C:\Jose\Pruebas Empresas\Prueba Tecnica Aprendiz U_Bancolombia\Lemonade.txt"
df = pd.read_csv(file_path, sep=",")

# Mostrar las primeras filas del DataFrame para verificar que se ha cargado correctamente
print(df.head())

# Separando las variables dependiente e independientes
X = df[['Temperature', 'Rainfall', 'Flyers']]  # Variables independientes
y = df['Sales']  # Variable dependiente

# Dividiendo los datos en conjuntos de entrenamiento y prueba (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creando y entrenando el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizando predicciones con los datos de prueba
y_pred = model.predict(X_test)

# Evaluando el modelo
r2 = r2_score(y_test, y_pred)  # Coeficiente de determinación R^2
mse = mean_squared_error(y_test, y_pred)  # Error cuadrático medio

# Resultados
coeficientes = model.coef_
intercepto = model.intercept_

# Imprimir resultados
print(f"R^2: {r2}")
print(f"MSE: {mse}")
print(f"Coeficientes: {coeficientes}")
print(f"Intercepto: {intercepto}")

# Visualizar la relación entre Temperature y Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Temperature', y='Sales', label='Datos Reales', color='blue')
plt.title('Relación entre Temperatura y Ventas')
plt.xlabel('Temperatura')
plt.ylabel('Ventas')
plt.legend()
plt.show()

# Gráfico de dispersión de las predicciones vs valores reales
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, label='Predicciones', color='green')
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--r', lw=2, label='Línea de Referencia')  # Línea de referencia
plt.title('Predicciones vs Valores Reales')
plt.xlabel('Valores Reales de Ventas')
plt.ylabel('Predicciones de Ventas')
plt.legend()
plt.show()
