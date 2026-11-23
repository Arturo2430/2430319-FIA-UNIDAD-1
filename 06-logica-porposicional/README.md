# 06. Lógica proposicional

Ejercicios en Python sobre valores booleanos y operadores de lógica proposicional. Incluye también materiales de un taller de ingeniería de prompts e ingeniería de LLMs.

## Trabajo realizado

Se implementaron operadores lógicos con funciones de Python y se probaron con combinaciones de valores booleanos. Los ejemplos incluyen negación, conjunción, disyunción, disyunción exclusiva, implicación y bicondicional, además de una composición para NAND. El objetivo es observar cómo las reglas lógicas se traducen a decisiones en código.

Los materiales también comparan dos formas de expresar una regla de acceso: `admin OR (contraseña_correcta AND NOT suspendida)` y `(admin OR contraseña_correcta) AND NOT suspendida`. Al cambiar la agrupación, una cuenta administradora suspendida puede recibir decisiones distintas. El ejemplo ilustra por qué es necesario formular condiciones y prioridades con claridad al diseñar instrucciones para un sistema.

## Alcance de los ejemplos

La comparación de prompts se representa mediante expresiones booleanas en Python; no es una medición de respuestas de un LLM conectado. El archivo `logica_proposicional_code.py` incluye una función de verificación de equivalencia que todavía devuelve `True` de forma fija, por lo que ese resultado no demuestra por sí solo una equivalencia lógica.

## Contenido

- `logica_proposicional_code.py`: ejemplos de negación, conjunción, disyunción, XOR, implicación y equivalencia.
- `Prompts vs LLMs.py`: código del taller de prompts y LLMs.
- `Taller Practico - Ingenieria de Prompts vs Ingeniera de LLMs.ipynb`: notebook del taller.

Para ejecutar los ejemplos de lógica desde esta carpeta:

```bash
python3 logica_proposicional_code.py
```

El notebook se puede abrir en Jupyter o Visual Studio Code.
