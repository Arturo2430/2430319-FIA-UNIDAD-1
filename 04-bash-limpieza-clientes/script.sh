#!/bin/bash
set -euo pipefail

# Trabajar en la carpeta del script, aunque se invoque desde otro directorio.
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

# -- (1) Exploracion de los datos originales --
wc -l clientes_sucios.csv
head -n 4 clientes_sucios.csv
tail -n 4 clientes_sucios.csv

# Contar las repeticiones sin incluir el encabezado.
tail -n +2 clientes_sucios.csv | sort | uniq -c

# -- (2) Eliminar filas duplicadas y conservar el encabezado al inicio --
{
    head -n 1 clientes_sucios.csv
    tail -n +2 clientes_sucios.csv | sort | uniq
} > clientes_sin_duplicados.csv

# -- (3) Excluir campos vacios, con solo espacios o con el valor NA --
# La guia usa (,,|NA); este patron tambien contempla campos como ", ,".
grep -v -E '(^|,)[[:space:]]*(NA)?[[:space:]]*(,|$)' \
    clientes_sin_duplicados.csv > clientes_completos.csv

# -- (4) Convertir el texto a minusculas --
tr '[:upper:]' '[:lower:]' < clientes_completos.csv > clientes_minusculas.csv

# -- (5) Eliminar espacios alrededor de las comas --
sed -E 's/ *, */,/g' clientes_minusculas.csv > clientes_estandarizados.csv

# -- (6) Consultar clientes mayores de 25 sin modificar el archivo final --
awk -F',' 'NR==1 || $3 > 25' clientes_estandarizados.csv
