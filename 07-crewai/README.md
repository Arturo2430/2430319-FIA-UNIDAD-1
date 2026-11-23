# 07. Investigación y redacción de noticias con CrewAI

Proyecto de agentes de inteligencia artificial para dividir la elaboración de una noticia en dos tareas: investigar un tema y redactar un artículo a partir de los hallazgos.

## Trabajo realizado

Se configuraron dos agentes con roles distintos. El investigador recopila información con una herramienta de búsqueda y prepara los puntos principales con sus fuentes. El redactor utiliza esa investigación para producir una noticia con titular, subtítulo, entrada, cuerpo y fuentes consultadas. La ejecución es secuencial: primero se realiza la investigación y después la redacción.

Las definiciones de los agentes y las tareas se separaron en archivos YAML, mientras que la coordinación y la generación de archivos se implementaron en Python. El código está configurado para utilizar el modelo local `llama3.1` mediante Ollama y realizar búsquedas con `SerperDevTool`. El tema definido en `main.py` es «La Derecha en América Latina» y se incorpora la fecha de ejecución como parte de las entradas.

## Resultados y evidencias

La carpeta `noticias_generadas/` conserva investigaciones y noticias en Markdown, con marcas de fecha y hora en sus nombres. Esto permite consultar por separado los hallazgos de la primera etapa y el artículo producido en la segunda. Los archivos generados son resultados del sistema y requieren revisión de sus afirmaciones y fuentes antes de reutilizarlos.

El código también contiene propuestas comentadas para verificar fuentes y crear una página web. Esas tareas no forman parte del flujo activo: los agentes implementados son el investigador y el redactor.

## Contenido

- `src/taller_crewai/config/agents.yaml`: roles, objetivos y contexto de los agentes.
- `src/taller_crewai/config/tasks.yaml`: instrucciones y salidas esperadas.
- `src/taller_crewai/crew.py`: agentes, herramienta de búsqueda, modelo y coordinación secuencial.
- `src/taller_crewai/main.py`: punto de entrada, tema y fecha de consulta.
- `noticias_generadas/`: investigaciones y noticias guardadas.
- `generar_noticia.sh`: script auxiliar de ejecución.
- `logs/`: registros conservados del proyecto.
- `pyproject.toml` y `uv.lock`: dependencias y configuración del proyecto.

## Ejecución

El proyecto declara Python >=3.10 y <3.14 y utiliza uv para sus dependencias. Desde esta carpeta:

```bash
uv sync
uv run crewai run
```

Para ejecutar el flujo se necesita Ollama disponible en `http://localhost:11434` con el modelo `llama3.1`, además de la credencial `SERPER_API_KEY` para las búsquedas. Una nueva ejecución genera archivos en `noticias_generadas/`; no es necesario ejecutarla para consultar las evidencias existentes.
