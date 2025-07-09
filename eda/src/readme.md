README - EDA sobre Restaurantes en Madrid

📄 Descripción

Este proyecto realiza un Análisis Exploratorio de Datos (EDA) sobre los restaurantes en Madrid, utilizando datos de:
- restaurantes de Madrid con su geolocalización,
- población en Madrid,
- renta neta media por persona por distrito de Madrid,
- restaurantes de estrellas michelín en el mundo.

🔍 Objetivo

Explorar la distribución de restaurantes según la población y la renta en los diferentes distritos de Madrid.
Por ultimo analizamos la relación calidad/cantidad de restaurantes españoles en el mundo.

📁 Estructura de archivos

Tenemos los siguientes archivos de base:
- **Madrid_rentapercapita.json**: Dataset con renta neta media por persona en los distritos de Madrid,
- **export.geojson**: Archivo con geometrías de los distritos de Madrid,
- **michelin_my_maps.csv**: Archivo con geometrías de los restaurantes Michelín en el Mundo,
- **Poblacion_Madrid.csv**: Documento con el censo por distrito y por año de la ciudad de Madrid

📆 Requisitos

Python >= 3.8

pandas

geopandas

matplotlib

seaborn

numpy

💡 Pasos principales del análisis

Carga de datos socioeconómicos y geoespaciales.

Limpieza y estandarización de nombres de distritos.

Unificación de datasets (renta + geometría).

Visualización en mapas y en graficos de barras.

Análisis descriptivo de la distribución de renta.

📊 Hallazgos clave

Se observan grandes diferencias de renta entre distritos de la periferia sur y el centro de la ciudad.

Los distritos con mayor renta concentran también restaurantes más caros.