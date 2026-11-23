#!/bin/bash

# -- (1) Analisis Exploratorio --
#Comandos para determinar las lineas de codigo
wc -l gdp_per_capita.csv
wc -l oecd_bli_2015.csv

#Comandos para ver los headers
head -n 1 gdp_per_capita.csv
head -n 1 oecd_bli_2015.csv

# -- (2) Filtrado de Satisfacción de Vida (OECD) --
# Sin Columna Inicial
# awk -F',' '$3 == "\"SW_LIFS\"" && $7 == "\"TOT\"" {print $2 "," $15}' oecd_bli_2015.csv > oecd_limpio.csv

# Con Columna inicial
awk -F',' 'NR == 1 || $3 == "\"SW_LIFS\"" && $7 == "\"TOT\"" {print $2 "," $15}' oecd_bli_2015.csv > oecd_limpio.csv

# -- (3) Normalización del PIB (FMI) --
# Comando con sed y awk
# sed -E 's/,//g' gdp_per_capita.csv | awk -F'\t' '$6 != "" {print $1 "," $6}' > gp_per_capita_limpio.csv

# Comando Solo con awk
awk -F'\t' '$6 != "" {gsub(",", "", $6); print $1 "," $6}' gdp_per_capita.csv > gp_per_capita_limpio.csv

# -- (4) Fusión de Datasets --
# Eliminación de comillas dobles
sed -i 's/"//g' oecd_limpio.csv

# Hacer el join de los dos datasets
join -t "," <(sort oecd_limpio.csv) <(sort gp_per_capita_limpio.csv) > merged_data.csv

# Agregar encabezados
sed -i '/^Country/d' merged_data.csv
sed -i '1i Pais,Satisfaccion_Vida,PIB_Capita' merged_data.csv

# -- (5) Preparacion para ML --
tail -n +2 merged_data.csv | cut -d',' -f3 > X.csv
tail -n +2 merged_data.csv | cut -d',' -f2 > y.csv