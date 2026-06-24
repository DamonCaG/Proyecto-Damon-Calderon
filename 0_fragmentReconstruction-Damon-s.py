import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO C | C2_MC_0
# ─────────────────────────────────────────────────────────
#
# Transcripción de Sesión Colectiva — Dra. Irina Sokol
# Matemática — Especialista en Teoría de Redes
# Fecha estimada: mediados de 1992
#
# "Las identidades no se borran. Se fragmentan.
#  Cada fragmento existe como elemento en una lista.
#  Para reconstruir un mensaje completo hay que unir
#  todos los fragmentos, separados por el símbolo '-'."
#
# La función recibe una lista de strings.
# Debe devolver un solo string con todos los elementos
# unidos, separados por '-'.
#
# REGLAS:
# - La función recibe una lista s de strings
# - Devuelve un solo string: elementos unidos por '-'
# - Usa un loop for para construir el resultado
# - No uses el método .join() — hazlo manualmente
#
# Ejemplo:
#   Input:  ["soy", "yo", "todavia"]
#   Output: "soy-yo-todavia"
#
#   Input:  ["A"]
#   Output: "A"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    elementos_unidos = str(s[0])
    for elemento in s[1:]:
        elementos_unidos += "-" + str(elemento)
    return elementos_unidos
        
        
    # TODO: une los elementos de la lista s con '-' entre ellos

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    (["soy", "yo", "todavia"], "soy-yo-todavia"),
    (["A"], "A"),
    (["Lime", "wood"], "Lime-wood"),
    (["uno", "dos", "tres", "cuatro"], "uno-dos-tres-cuatro"),
    (["x", "y", "z"], "x-y-z"),
]

_frag = "RlJBRy1DMTo6ZnVzaW9u"
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo C",
          puzzle="Puzzle 1 — Reconstrucción de Fragmentos")
