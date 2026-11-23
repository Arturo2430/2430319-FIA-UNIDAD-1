# Taller de lógica difusa

Material de la práctica de lógica difusa.

## Desarrollo de la práctica

Primero se ejemplifican las operaciones de unión, intersección y complemento mediante grados de pertenencia, usando el máximo, el mínimo y la resta respecto de uno. Esto introduce la diferencia entre manejar valores graduales y limitarse a decisiones de verdadero o falso.

Después se construye un sistema de inferencia difusa para sugerir una propina. Las entradas son la calidad de la comida y del servicio, evaluadas de 0 a 10; la salida es una propina de 0 a 25 %. Se definen categorías lingüísticas para las entradas y funciones triangulares para las propinas baja, media y alta, conectadas mediante reglas SI-ENTONCES.

## Resultados que muestra el código

El ejemplo principal utiliza comida de 6.5 y servicio de 9.8. Además, se evalúan cuatro combinaciones adicionales para comparar la respuesta del sistema. El programa imprime las propinas calculadas y genera una gráfica de la salida, que guarda como `propina.png` al ejecutarse.

La práctica usa NumPy, scikit-fuzzy y Matplotlib. Tanto el notebook como el script permiten revisar las reglas y modificar las entradas para explorar cómo cambia la recomendación.

## Contenido

- `fuzzy_logic_taller.ipynb`: notebook del taller.
- `fuzzy_logic_taller.py`: versión en Python.

Consulta el notebook o el script para revisar las dependencias y los ejercicios.
