import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO D | C2_MD_1
# ─────────────────────────────────────────────────────────
#
# Protocolo de Emergencia — Dr. Samuel Chen
# Sistema de Deteccion de Anomalias
#
# "Cree una lista de palabras prohibidas en la red.
#  Si alguna transmision contiene una de esas palabras,
#  el sistema debe bloquearla inmediatamente.
#  El modulo de deteccion necesita verificar si una
#  palabra esta dentro de la lista."
#
# La lista de palabras bloqueadas es:
# ["desconectar", "salida", "individuo", "yo", "separar"]
#
# La funcion recibe un string (una sola palabra).
# Devuelve True si esa palabra esta en la lista bloqueada,
# False si no lo esta.
#
# REGLAS:
# - La funcion recibe un string s
# - Devuelve True o False
# - Usa la lista definida arriba y un loop for o el operador 'in'
# - La comparacion es en minusculas (convierte s a minusculas)
#
# Ejemplo:
#   Input:  "yo"          → Output: True
#   Input:  "nosotros"    → Output: False
#   Input:  "Salida"      → Output: True  (sin importar mayus)
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

PALABRAS_BLOQUEADAS = ["desconectar", "salida", "individuo", "yo", "separar"]
def solution(s):
    palabras = s.split()
    for palabra in palabras:
        if palabra.lower() in PALABRAS_BLOQUEADAS:
            return True
        elif palabra in PALABRAS_BLOQUEADAS:
            return True
    return False
            
    # TODO: devuelve True si s (en minusculas) esta en PALABRAS_BLOQUEADAS


# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("yo", True),
    ("nosotros", False),
    ("Salida", True),
    ("desconectar", True),
    ("limewood", False),
    ("Individuo", True),
]

_frag = "RlJBRy1EMjo6ZGVzY29uZXhpb24="
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo D",
          puzzle="Puzzle 2 — Lista Negra")
