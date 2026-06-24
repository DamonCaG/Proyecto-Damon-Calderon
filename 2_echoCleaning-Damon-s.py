import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO C | C2_MC_2
# ─────────────────────────────────────────────────────────
#
# LOG DE SISTEMA — FECHA: 11/08/1992 — 04:23:17
# Estado de la red: CRÍTICO
#
# "Las identidades se repiten en el buffer.
#  Cuando una conciencia es absorbida, su señal queda
#  como eco en la red. Hay que limpiar los duplicados.
#  Solo debe quedar la primera aparición de cada nombre."
#
# La función recibe una lista de strings.
# Debes devolver una lista nueva sin elementos repetidos,
# conservando el orden de primera aparición.
#
# REGLAS:
# - La función recibe una lista s
# - Devuelve una lista sin duplicados (en orden de aparición)
# - Usa un loop for y una lista vacía para construir el resultado
# - Verifica si el elemento ya está en tu lista antes de añadirlo
#
# Ejemplo:
#   Input:  ["Elena", "Mateo", "Elena", "Irina", "Mateo"]
#   Output: ["Elena", "Mateo", "Irina"]
#
#   Input:  ["a", "b", "a", "c", "b"]
#   Output: ["a", "b", "c"]
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    lista_sin_repetidos = []
    for elemento in s:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos
    # TODO: devuelve la lista s sin duplicados, preservando orden

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    (["Elena", "Mateo", "Elena", "Irina", "Mateo"], ["Elena", "Mateo", "Irina"]),
    (["a", "b", "a", "c", "b"], ["a", "b", "c"]),
    (["x"], ["x"]),
    (["z", "z", "z"], ["z"]),
    (["uno", "dos", "tres"], ["uno", "dos", "tres"]),
]

_frag = "RlJBRy1DMzo6Y29sYXBzbw=="
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo C",
          puzzle="Puzzle 3 — Limpieza de Ecos")
