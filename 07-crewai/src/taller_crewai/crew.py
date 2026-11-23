import os
from datetime import datetime
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.llm import LLM
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

local_llm = LLM(
    model="ollama/llama3.1",
    base_url="http://localhost:11434"
)

EXECUTION_TIMESTAMP = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
CARPETA_DESTINO = "noticias_generadas"

def get_output_path(filename_prefix: str, extension: str) -> str:
    os.makedirs(CARPETA_DESTINO, exist_ok=True)
    return os.path.join(CARPETA_DESTINO, f"{filename_prefix}_{EXECUTION_TIMESTAMP}.{extension}")

@CrewBase
class TallerCrewai():
    """TallerCrewai crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def investigador_informacion(self) -> Agent:
        return Agent(
            config=self.agents_config['investigador_informacion'],
            verbose=True,
            llm=local_llm,
            tools=[search_tool]
        )

    @agent
    def redactor_noticia(self) -> Agent:
        return Agent(
            config=self.agents_config['redactor_noticia'],
            verbose=True,
            llm=local_llm,
        )

    # @agent
    # def comparador_fuentes(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['comparador_fuentes'],
    #         verbose=True,
    #         llm=local_llm,
    #         tools=[search_tool]
    #     )

    # @agent
    # def web_creador(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['web_creador'],
    #         verbose=True,
    #         llm=llm_llama3,
    #     )

    @task
    def tarea_investigacion(self) -> Task:
        return Task(
            config=self.tasks_config['tarea_investigacion'],
            # Agregamos output_file para que también se guarde la investigación inicial
            output_file=get_output_path("investigacion", "md")
        )

    @task
    def tarea_redaccion(self) -> Task:
        return Task(
            config=self.tasks_config['tarea_redaccion'],
            output_file=get_output_path("noticia", "md")
        )

    # @task
    # def validar_fuentes(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['validar_fuentes'],
    #         output_file=get_output_path("informe_fuentes", "md")
    #     )

    # @task
    # def crear_pagina(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['crear_pagina'],
    #         output_file=get_output_path("pagina_noticia", "html")
    #     )

    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )