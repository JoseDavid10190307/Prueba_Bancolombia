# Documentación del Proyecto: Análisis de Ventas de Limonada

## 1. Introducción
Este proyecto tiene como objetivo analizar las ventas de limonada utilizando un dataset con información sobre temperatura, precipitaciones, número de volantes distribuidos y ventas diarias. El proyecto incluye análisis estadístico básico, un modelo predictivo de ventas basado en regresión lineal y un análisis temporal para identificar patrones en las ventas a lo largo del tiempo.

## 2. Estructura del Proyecto
- **Analisis.py** Este script realiza un análisis estadístico básico sobre las variables numéricas del dataset (Temperature, Rainfall, Flyers, Sales). A continuación se describen los pasos realizados en el script:
    -Carga del dataset: Se utiliza pandas para cargar los datos desde el archivo Lemonade.txt.
    -Medidas Estadísticas Básicas: Se calculan media, mediana, varianza, desviación estándar, y percentiles de las columnas numéricas.
    -Medidas de Forma: Se calculan la asimetría (skewness) y la curtosis para cada variable numérica.
    -Detección de Outliers: Se identifican valores atípicos utilizando el método del rango intercuartílico (IQR).
Ejecución: python Analisis.py

- **Modelo_Predictivo.py** Este script construye un modelo de regresión lineal para predecir las ventas diarias (Sales) en función de las variables climáticas y publicitarias (Temperature, Rainfall, Flyers). El modelo se evalúa usando métricas como el coeficiente de determinación (R²) y el error cuadrático medio (MSE). También se visualizan las relaciones entre las variables predictoras y las ventas.
Pasos:
    -División de los datos: Se separan los datos en conjuntos de entrenamiento (80%) y prueba (20%).
    -Entrenamiento del modelo: Se entrena un modelo de regresión lineal con scikit-learn.
    -Evaluación del modelo: Se reportan el R² y el MSE.
    -Visualización: Se generan gráficos para analizar la relación entre la temperatura y las ventas, así como la precisión de las predicciones.
Ejecución: python Modelo_Predictivo.py

- **Analisis_Temporal.py** Este script se encarga del análisis temporal de las ventas a lo largo del tiempo. Las fechas en el dataset son convertidas a un formato apropiado y se realizan análisis por día de la semana, mes y a lo largo del año.
Pasos:
    -Conversión de fechas: Se convierte la columna Date al formato datetime para facilitar el análisis temporal.
    -Ventas por día de la semana: Se calcula el promedio de ventas para cada día de la semana y se visualiza en un gráfico de barras.
    -Temperatura y ventas por mes: Se calculan y grafican los promedios mensuales de temperatura y ventas.
    -Ventas a lo largo del tiempo: Se visualizan las ventas totales diarias en un gráfico de líneas.
Ejecución: python Analisis_Temporal.py

## 3. Requisitos
- **Este proyecto requiere las siguientes dependencias de Python:**
    -pandas
    -numpy
    -scipy
    -scikit-learn
    -matplotlib
    -seaborn
Puedes instalarlas utilizando pip: pip install pandas numpy scipy scikit-learn matplotlib seaborn

## 4. Cómo Ejecutar el Proyecto
- **Instalar las dependencias:** Asegúrate de que las bibliotecas mencionadas estén instaladas.
- **Ajustar las rutas:** En cada archivo Python, asegúrate de que la ruta al archivo Lemonade.txt sea correcta.
- **Ejecutar los scripts:** Corre cada uno de los scripts de análisis, modelo predictivo y análisis temporal desde la terminal.

## 5. Visualización de Resultados
Se generaron gráficos para analizar la relación entre diversas variables del dataset y las ventas de limonada. A continuación, se describen los principales gráficos:
  - **Relación entre Temperatura y Ventas:** Un gráfico que muestra la correlación entre la temperatura (Temperature) y las ventas (Sales), destacando cómo las variaciones en la temperatura afectan los resultados de ventas.
  - **Predicciones vs Valores Reales:** Un gráfico de dispersión que compara las predicciones generadas por el modelo de regresión lineal con los valores reales de ventas. Esto permite evaluar el rendimiento del modelo y la precisión de sus predicciones.
  - **Ventas Promedio por Día de la Semana:** Un gráfico de barras que presenta el promedio de ventas por cada día de la semana, permitiendo identificar patrones de comportamiento en las ventas a lo largo de la semana.
  - **Temperatura y Ventas Promedio por Mes:** Un gráfico que combina las temperaturas promedio con las ventas promedio en cada mes, mostrando tendencias estacionales y cómo la variación de la temperatura influye en las ventas mensuales.
  - **Ventas a lo Largo del Tiempo:** Un gráfico de líneas que visualiza las ventas de limonada a lo largo del tiempo, proporcionando una perspectiva clara de la evolución de las ventas durante el período analizado.

## 6. Conclusión y Futuras Mejoras
- **Conclusión:** El análisis reveló una fuerte correlación entre la temperatura y las ventas. Los días con temperaturas más altas tienden a generar mayores ventas, mientras que la lluvia y los flyers tienen un impacto menor. El modelo predictivo de regresión lineal mostró un buen rendimiento, pero podrían probarse algoritmos más avanzados en el futuro.
- **Futuras mejoras:** Se sugiere incluir más variables como ubicación de las ventas o promociones para mejorar la precisión del modelo y realizar un análisis de regresión no lineal para capturar relaciones más complejas.

## 7. Referencias
- **Datos descargados de:** Lemonade.txt
- **Biblioteca utilizadas:** Pandas, NumPy, Scikit-learn, Matplotlib, Plotly
