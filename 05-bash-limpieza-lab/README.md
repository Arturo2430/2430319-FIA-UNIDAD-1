# 05. Laboratorio de limpieza de datos con Bash

Práctica de preparación de datos de PIB per cápita y satisfacción de vida mediante herramientas de Bash.

## Trabajo realizado

Se implementó un flujo de preparación de datos con herramientas de Bash a partir de dos fuentes: PIB per cápita e indicadores de bienestar de la OCDE. La exploración inicial utiliza el conteo de líneas y la consulta de encabezados para reconocer la estructura de los archivos antes de transformarlos.

En los datos de la OCDE se selecciona el indicador de satisfacción de vida (`SW_LIFS`) para el total de la población (`TOT`) y se extraen el país y su valor. En el archivo de PIB se toma el país y la sexta columna, se omiten los registros sin valor en esa columna y se eliminan las comas internas de los importes. Después se quitan las comillas del archivo de bienestar y se ordenan ambos conjuntos para unirlos por país mediante `join`.

## Resultado del proceso

El archivo `merged_data.csv` reúne país, satisfacción de vida y PIB per cápita. A partir de esa tabla se extrae el PIB como variable de entrada (`X.csv`) y la satisfacción de vida como variable objetivo (`y.csv`). La actividad deja preparados estos datos para un trabajo posterior de aprendizaje automático; el script no entrena un modelo.

La unión conserva los países cuyo nombre coincide en ambas fuentes. Por ello, diferencias de escritura entre los nombres pueden dejar registros fuera del conjunto combinado.

## Contenido

- `script.sh`: exploración, limpieza, unión de datos y preparación de variables.
- `gdp_per_capita.csv` y `oecd_bli_2015.csv`: datos de entrada.
- `gp_per_capita_limpio.csv` y `oecd_limpio.csv`: datos procesados.
- `merged_data.csv`: conjunto de datos combinado.
- `X.csv` y `y.csv`: variables para el trabajo posterior de aprendizaje automático.

## Ejecución

Desde esta carpeta, en un entorno con Bash, `awk`, `sed`, `sort`, `join`, `cut` y `wc`:

```bash
bash script.sh
```

El script vuelve a generar los archivos de salida.
