import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO B | C2_MB_1
# ─────────────────────────────────────────────────────────
#
# Log de Lecturas — Equipo Neural — Dr. Reyes
# "Solo las lecturas mayores a 50 Hz son relevantes.
#  Todo lo demás es ruido de fondo. El sistema anterior
#  guardaba todo sin filtrar — por eso los datos
#  se corrompieron al fusionarse."
#
# La función recibe una lista de números enteros.
# Debe devolver una lista NUEVA con solo los números
# que sean MAYORES a 50.
#
# REGLAS:
# - La función recibe una lista de enteros llamada s
# - Devuelve una lista con solo los elementos > 50
# - Usa un loop for y una lista vacía para construir el resultado
# - El orden original debe mantenerse
#
# Ejemplo:
#   Input:  [10, 55, 30, 80, 50, 99]
#   Output: [55, 80, 99]
#
#   Input:  [1, 2, 3]
#   Output: []
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    lista_nueva = []
    for numero in s:
        if numero > 50:
            lista_nueva.append(numero)
    return lista_nueva
    # TODO: devuelve lista con solo los elementos mayores a 50

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ([10, 55, 30, 80, 50, 99], [55, 80, 99]),
    ([1, 2, 3], []),
    ([51, 52, 53], [51, 52, 53]),
    ([50, 50, 50], []),
    ([100], [100]),
    ([48, 72, 13, 91, 50, 67], [72, 91, 67]),
]

_frag = "RlJBRy1CMjo6c2luY3Jvbmlh"
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo B",
          puzzle="Puzzle 2 — Filtro de Señales")
