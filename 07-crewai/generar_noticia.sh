#!/bin/bash

# Añadir las rutas necesarias para que cron encuentre uv, crewai, python, etc.
export PATH="/home/arturo/.local/bin:$PATH"

# Entrar a la carpeta del proyecto
cd /home/arturo/UPV/Fundamentos-IA/CrewAI/taller_crewai || exit 1

# Log de ejecución
echo "El script se ejecuto a las $(date)" >> logs/logfile.txt

# Ejecutar crewai
/home/arturo/.local/bin/crewai run >> logs/logfile.txt 2>&1