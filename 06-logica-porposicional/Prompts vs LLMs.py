from inspect import signature

def neg(p: bool) -> bool:
    """
    Operador Unario: Negacion (notp)
    Devuelve el valor de verdad opuesto a p.
    """
    return not p


def y(p: bool, q: bool) -> bool:
    """
    Operador Binario: Conjuncion (p ^ q)
    Devuelve True unicamente si ambos operadores son True
    """
    return p and q


def o(p: bool, q: bool) -> bool:
    """
    Operador Binario: Disyuncion Inclusiva (p v q)
    Devuelve True si al menos uno de los operandos es True[cite: 2]
    """
    return p or q

print("Operadores base (neg, y, o) cargadores en memoria.")

# ===================================================================
# PASO 2: INFRAESTRUCTURA DE EVALUACION SEMANTICA (logEqv)
# ====================================================================

# 1. Obtener la aridad del predicado
def aridad(fun) -> int:
    """ Obtiene la cantidad de parametros de una funacion """
    return len(signature(fun).parameters)

# 2. Generar arbol de casos de prueba
def casosPrueba(n: int, res=None) -> list:
    """ Generar recursivamente la matriz de 2^n combinaciones booleanas"""
    if res is None:
        res = []
    if n == 0:
        return [res]
    # Map anade True y Flase al inicio de cada lista en las combinacion previas
    res1 = list(map(lambda t: [True] + t, res))
    res2 = list(map(lambda t: [False] + t, res))
    return casosPrueba(n - 1, res1 + res2)

# 3. Construir el vector de resultados
def vectorResultados(Pred) -> list:
    """ Genera el vector de resultados de la funcion fun """
    ar = aridad(Pred)
    Lvals = casosPrueba(ar)
    return list(map(lambda t: Pred(*t), Lvals))

# 4. Verificador de Equivalencia Logica
def logEqv(Pred1, Pred2) -> bool:
    """ Compara si dos vectores de resultados son identicos (P equiv Q) """
    return vectorResultados(Pred1) == vectorResultados(Pred2)

print("Motor de inferencia (logEqv) y automatizacion de tablas de verdad listo.")


# =======================================================================
# PASO 3: FORMALIZACION DE PROMPTS EN PYTHON (LAMBDA FUNCIONES)
# =======================================================================

# ----
# PROMPT 1: EL USUARIO PROMEDIO (Aambiguedad)
# Ptompt: "Da acceso si es admin o la contrasena es correcta y no esta suspendida"
# Analisis del motor del LLM:
# Al no existir una estructura clara, la maquina aplica precedencia matematica

prompt_ambiguo= lambda p, q, r: o(p, y(q, neg(r)))

#
# PROMPT 2: EL INGENIERO ESTRUCTURADO

prompt_estructurado = lambda p, q, r: y(o(p, q), neg(r))


# =======================================================================
# PASO 4: SIMULACION DEL ATAQUE AL AGENTE
# =======================================================================

# Definimos el entorno de ataque: p=True, q=False, r=True
entorno_ataque = (True, False, True)

# Evaluamos las decisioenes del agente
decision_ambigua = prompt_ambiguo(*entorno_ataque)
decision_estructurada = prompt_estructurado(*entorno_ataque)

print ("SIMULACION DE ATAQUE DE SEGURIDAD")
print ("Escenario actual:")
print("- Es Administrador       : True")
print("- Contrasena Correcta    : False")
print("- Cuenta Suspendida      : True\n")

print(f"Decision del LLM (Prompt Ambiguo):")
print(f"-> {'ACCESO CONCEDIDO (Sistema Vulnerado)' if decision_ambigua else 'ACCESO DENEGADO (Sistema Seguro)'}\n")

print(f"Decision del LLM (Prompt Estructurado):")
print(f"-> {'ACCESO CONCEDIDO (Sistema Vulnerado)' if decision_estructurada else 'ACCESO DENEGADO (Sistema Seguro)'}")

# =======================================================================
# PASO 4: LA DEMOSTRACION MATEMATICA DEFINITIVA (logEqv) 
# =======================================================================

print("--- AUDITORIA MATEMATICA DEL MOTOR DE IA ---")

# Validamos si P = Q
equivalencia = logEqv(prompt_ambiguo, prompt_estructurado)

print(f"")