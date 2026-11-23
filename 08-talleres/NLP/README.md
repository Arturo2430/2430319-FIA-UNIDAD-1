# Taller de procesamiento del lenguaje natural: análisis de sentimientos

Implementación del analizador de sentimientos mostrado en las capturas de la práctica. El programa recibe una frase en español y la clasifica como positiva, negativa o neutral mediante un vocabulario y reglas sencillas.

## Trabajo realizado

Se definieron dos conjuntos de palabras: uno con términos positivos como «feliz», «excelente» y «genial», y otro con términos negativos como «triste», «horrible» y «aburrido». Primero se convierte la entrada a minúsculas y se separa en palabras o tokens, descartando los signos de puntuación y conservando las letras acentuadas.

Después se recorre la lista de tokens y se calcula un puntaje. Cada palabra positiva suma un punto y cada palabra negativa resta uno. Cuando aparece un conector de contraste —«pero», «aunque» o «sin embargo»—, las palabras de sentimiento posteriores valen el doble. El conector «sin embargo» se reconoce como una secuencia de dos tokens. Los conectores modifican el peso de las palabras siguientes; no invierten automáticamente su polaridad.

El resultado depende del signo del puntaje: mayor que cero significa positivo, menor que cero significa negativo y cero significa neutral. Finalmente se implementó una interfaz de consola que permite analizar varias frases y termina cuando se escribe `salir`.

## Ejemplos de funcionamiento

| Texto | Puntaje | Clasificación |
| --- | --- | --- |
| Estoy feliz, todo es excelente. | 2 | Positivo |
| Fue horrible y aburrido. | -2 | Negativo |
| Es bueno, pero aburrido. | -1 | Negativo |
| Fue horrible, sin embargo es divertido. | 1 | Positivo |
| Estoy feliz aunque triste. | -1 | Negativo |
| Es bueno y malo. | 0 | Neutral |
| La mesa está junto a la ventana. | 0 | Neutral |

Por ejemplo, en «Es bueno, pero aburrido», `bueno` suma 1 y `aburrido` resta 2 porque está después de `pero`. El total es -1. Si no aparece ninguna palabra del vocabulario, el resultado también es neutral.

## Ejecución

Desde esta carpeta:

```bash
python3 pln.py
```

Solo requiere Python 3 y su biblioteca estándar. No necesita instalar paquetes, descargar datos ni conectarse a un servicio de IA. El archivo `pln.py` contiene el vocabulario, las funciones `tokenizar` y `analizar_sentimiento`, y el programa interactivo.
