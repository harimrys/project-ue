# Desempleo y educación en la Unión Europea

## Descripción del Proyecto

Este proyecto tiene como objetivo principal investigar la relación entre el nivel educativo y la tasa de desempleo en la Unión Europea. Nuestra hipótesis central es que existe una relación inversa entre el nivel educativo y el desempleo: a mayor nivel educativo, menor es la tasa de desempleo.

El estudio es parte de la creación de una empresa educativa ficticia que busca entender la situación actual de la educación y el desempleo en Europa, con el fin de identificar un público objetivo para sus servicios.

Este proyecto es una actividad de clase para los estudiantes de Ironhack. Estamos trabajando en él como parte de nuestro aprendizaje en el curso de Data Analytics.

## Motivación

Queremos comprender cómo se relacionan el nivel educativo y el desempleo en la población joven europea (15-29 años) para tomar decisiones estratégicas en el desarrollo de nuestra empresa educativa. Este análisis es fundamental para evaluar el mercado laboral en función de los niveles educativos y para identificar posibles oportunidades de negocio.

Nuestras hipótesis principales son:
- Las mujeres tienden a alcanzar un nivel educativo mayor que los hombres, pero aún así sufren mayores tasas de desempleo.
- La mayoría de los jóvenes europeos alcanzan un nivel educativo medio (superior a la ESO, pero inferior a los estudios universitarios).
- En los países del norte de Europa, se observa una relación clara entre un mayor nivel educativo y una menor tasa de desempleo.

## Bases de Datos Utilizadas

- **Youth unemployment by sex, age and educational attainment level**  
- **Young people by educational attainment level, sex and age**

### Características de las bases de datos

- **Rango de edad:** 15-29 años
- **Años de estudio:** 2014-2023
- **Variables:** País, nivel educativo, tasa de desempleo, género
- **Exclusiones:** Algunos países de Europa fueron excluidos por falta de datos completos o fiables.
- **Notas adicionales:**  
  - La tasa de nivel educativo proporcionada no era la tasa real, ya que solo representaba el porcentaje de personas que habían completado cierto nivel de estudios. Por ejemplo, el 13% de mujeres en España que solo terminaron la ESO. Por ello, creamos una nueva columna con una media ponderada, asignando un valor del 1 al 5 a cada nivel educativo, para utilizarla en nuestro análisis.

## Metodología

1. **Preprocesamiento de datos:**
   - Eliminamos las columnas irrelevantes.
   - Renombramos y estandarizamos los nombres de países, niveles educativos y géneros para que coincidan en ambas bases de datos.
   - Eliminamos duplicados y tratamos los valores nulos.

2. **Fusión de bases de datos:**
   - Se combinaron las bases de datos utilizando las columnas comunes de sexo, edad, país y nivel educativo.

3. **Herramientas utilizadas:**
   - **Lenguaje:** Python
   - **Librerías:** 
     - Limpieza de datos: `pandas`, `numpy`
     - Visualización: `seaborn`, `matplotlib.pyplot`

## Análisis Realizado

- Se crearon gráficos para analizar los dos aspectos (nivel educativo y desempleo) tanto por separado como en conjunto, con especial atención a la diferenciación por género.
- En los gráficos que diferenciaron por género, se excluyeron las filas que contenían el total de ambos géneros para obtener una mejor representación individual.

## Resultados y Conclusiones

1. **Nivel Educativo:**  
   - En general, el nivel educativo promedio de los jóvenes europeos se sitúa alrededor de un 3 en una escala del 1 al 5, lo que indica que la mayoría supera el nivel más bajo (la ESO en el caso de España), pero no alcanzan los estudios superiores (universidad o máster). Para la mejor comprensión de este dato hay que tener presente el rango de edad seleccionado.

2. **Relación entre educación y desempleo:**  
   - En algunos países del norte de Europa, como se predijo, a mayor nivel educativo, menor es la tasa de desempleo. Sin embargo, en otros países como Grecia, Italia y España, aunque los jóvenes alcanzan niveles educativos altos, las tasas de desempleo siguen siendo elevadas.

3. **Género:**  
   - Como indicaba nuestra hipótesis, las mujeres alcanzan niveles educativos más altos que los hombres, pero a pesar de ello, sufren una mayor tasa de desempleo.

## Estructura del Proyecto

- `data/`: Contiene las bases de datos originales extraídas de Eurostat.
- `main.ipynb`: Archivo principal donde se realiza la fusión de bases de datos y el análisis de los datos.
- `functions.py`: Contiene funciones auxiliares utilizadas en el análisis.
- `eda.ipynb`: Exploración inicial de los datos (Exploratory Data Analysis).
- `functions_eda.py`: Funciones utilizadas para el análisis exploratorio.
- `combined_data.csv`: Base de datos final, fusionada y limpia. 

## Créditos
Este proyecto ha sido realizado por:
- **Cristina Ramírez Díaz**
- **Haridian Morays**

