import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO B | C2_MB_2
# ─────────────────────────────────────────────────────────
#
# Protocolo de Calibración — Laboratorio Norte — 1991
#
# "Cada código de calibración es una mezcla de letras
#  y números. El valor de calibración se obtiene sumando
#  todos los dígitos numéricos presentes en el código.
#  Las letras se ignoran."
#
# La función recibe un string que mezcla letras y números.
# Debes sumar todos los dígitos (0-9) que encuentres en él.
#
# REGLAS:
# - La función recibe un string s
# - Devuelve la suma de todos los dígitos que contiene (int)
# - Usa un loop for para recorrer el string
# - Para verificar si un carácter es dígito: c.isdigit()
# - Para convertir un carácter a número: int(c)
#
# Ejemplo:
#   Input:  "a1b2c3"
#   Output: 6        (1 + 2 + 3)
#
#   Input:  "R4Y35"
#   Output: 12       (4 + 3 + 5)
#
#   Input:  "sinNumeros"
#   Output: 0
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    numeros = "0123456789"
    sumatoria = 0
    for caracteres in s:
        if caracteres in numeros:
            sumatoria += int(caracteres)
    return sumatoria
    # TODO: suma y devuelve todos los dígitos del string s


# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("a1b2c3", 6),
    ("R4Y35", 12),
    ("sinNumeros", 0),
    ("999", 27),
    ("L1m3w00d", 4),
    ("00000", 0),
]

_frag = "RlJBRy1CMzo6ZnJlY3VlbmNpYQ=="
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo B",
          puzzle="Puzzle 3 — Valor de Calibración")
