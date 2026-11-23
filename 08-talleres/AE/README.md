# Taller de algoritmos evolutivos

Práctica de algoritmos evolutivos aplicada a un laberinto.

## Desarrollo de la práctica

El notebook representa el laberinto como una matriz de paredes y espacios transitables. Cada individuo es una secuencia de movimientos, y una población reúne varias rutas candidatas generadas al azar. Para evaluar cada ruta se simula el recorrido, se cuentan los intentos de atravesar paredes y se mide el avance hacia la salida.

La evolución utiliza selección por torneo, cruce de un punto, mutación y elitismo. Estos pasos se repiten hasta alcanzar la meta o el límite de generaciones. El fitness premia el progreso y la llegada a la salida, penaliza los movimientos inválidos y favorece recorridos más cortos cuando se consigue resolver el laberinto.

## Análisis de la solución

Se incluyen visualizaciones del mejor recorrido y de la evolución del fitness máximo y promedio. Una semilla aleatoria permite repetir el experimento. BFS se usa para calcular distancias que orientan la evaluación; la generación de candidatos sigue a cargo del algoritmo genético.

El laberinto funciona como ejemplo didáctico para observar selección, cruce y mutación. El taller no plantea que un algoritmo genético sea el método más eficiente para encontrar rutas en un laberinto conocido.

## Contenido

- `taller_algoritmos_evolutivos_laberinto.ipynb`: notebook del taller.

Abre el notebook en Jupyter o Visual Studio Code para revisar y ejecutar la práctica.
