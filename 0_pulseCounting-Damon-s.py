import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO B | C2_MB_0
# ─────────────────────────────────────────────────────────
#
# Notas de Campo — Dr. Mateo Reyes — Físico Cuántico
# Sesión 14 — Laboratorio Norte
#
# "La sincronización neuronal genera pulsos.
#  Cada pulso se representa con el carácter '*' en el log.
#  Para calibrar el equipo debo saber cuántos pulsos
#  ocurrieron en cada transmisión registrada."
#
# La función recibe un string con la transmisión completa.
# Debes contar cuántas veces aparece el carácter '*' en él.
#
# REGLAS:
# - La función recibe un string s
# - Devuelve la cantidad de veces que aparece '*' (int)
# - Usa un loop for para recorrer el string
# - No uses el método .count()
#
# Ejemplo:
#   Input:  "a*b*c*"
#   Output: 3
#
#   Input:  "sin pulsos"
#   Output: 0
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    pulso = "*"
    contador_de_pulsos = 0
    for caracter in s:
        if caracter in pulso:
            contador_de_pulsos = contador_de_pulsos + 1
    return contador_de_pulsos
    # TODO: cuenta cuántas veces aparece '*' en el string s

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("a*b*c*", 3),
    ("sin pulsos", 0),
    ("*", 1),
    ("****", 4),
    ("*neural*sync*test*ok*", 5),
    ("limewood1990", 0),
]

_frag = "RlJBRy1CMTo6bmV1cmFs"
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo B",
          puzzle="Puzzle 1 — Conteo de Pulsos")
