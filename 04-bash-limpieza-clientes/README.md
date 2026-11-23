# 04. Limpieza de datos de clientes con Bash

Archivos CSV de una práctica de limpieza y estandarización de datos de clientes.

## Trabajo realizado

Se trabajó con un archivo de clientes que contiene nombres, edades, salarios y departamentos. Los datos de entrada presentan filas repetidas, valores `NA`, campos con espacios y diferencias en el uso de mayúsculas y minúsculas. Primero se explora el archivo mediante conteos y vistas parciales; después se ordenan las filas y se eliminan los duplicados exactos, conservando el encabezado.

La limpieza continúa descartando registros incompletos, incluidos los campos que contienen solo espacios. A continuación se convierte el texto a minúsculas y se eliminan los espacios alrededor de las comas. Cada transformación se guarda en un CSV separado para poder revisar el proceso paso a paso. La consulta final con `awk` muestra los clientes mayores de 25 años sin crear otro conjunto de datos.

## Resultado del proceso

Con el archivo `clientes_sucios.csv` actual, el script produce tres registros completos y sin filas duplicadas: los identificadores 1, 3 y 7. Los archivos de salida se regeneran al ejecutarlo; por ello, los CSV conservados de la práctica pueden diferir del resultado de una nueva ejecución. La eliminación de duplicados compara filas completas y no identifica personas repetidas con datos escritos de forma distinta.

## Contenido

- `script.sh`: comandos de exploración y limpieza de clientes.
- `clientes,sucio.csv` y `clientes_sucios.csv`: archivos de datos sucios.
- `clientes_minusculas.csv`: datos convertidos a minúsculas.
- `clientes_sin_duplicados.csv`: datos sin registros duplicados.
- `clientes_completos.csv`: datos de registros completos.
- `clientes_estandarizados.csv`: datos estandarizados.

## Ejecución

Desde esta carpeta, ejecuta:

```bash
bash script.sh
```

Requiere Bash y las herramientas `wc`, `head`, `tail`, `sort`, `uniq`, `grep`, `tr`, `sed` y `awk`.

El script lee `clientes_sucios.csv` y vuelve a generar los cuatro archivos de las etapas de limpieza. Conserva el encabezado, elimina filas duplicadas y registros con campos vacíos, con solo espacios o con el valor `NA`, convierte el texto a minúsculas y elimina espacios alrededor de las comas. Al final muestra los clientes mayores de 25 años.

`clientes,sucio.csv` contiene una captura de terminal y no se utiliza como entrada. Los comandos corresponden a la práctica de clientes de `comandos.md`; la limpieza de PIB y satisfacción de vida está en la actividad 05.
