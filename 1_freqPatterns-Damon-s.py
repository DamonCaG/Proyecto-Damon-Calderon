import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO A | C2_MA_1
# ─────────────────────────────────────────────────────────
#
# Diario de la Dra. Elena Voss — Psicóloga Jefe
# Entrada 001 — 14 de marzo, 1990
#
# "El protocolo de sincronización requiere que contemos
#  los patrones de resonancia en cada transmisión.
#  El primer filtro: contar vocales. Las vocales son
#  los portadores primarios de frecuencia en el lenguaje."
#
# Necesitas una función que cuente cuántas vocales
# (a, e, i, o, u — mayúsculas o minúsculas) hay en un string.
# ———————————————————
# REGLAS:
# - La función recibe un string s
# - Devuelve un número entero (int) con la cantidad de vocales
# - Considera tanto mayúsculas como minúsculas
# - Usa un loop for para recorrer el string
#
# Ejemplo:
#   Input:  "Limewood"
#   Output: 3        (i, e, o, o)
#
#   Input:  "hello"
#   Output: 2        (e, o)
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    vocales = "aeiouAEIOU"
    contador_de_vocales = 0
    for caracter in s:
        if caracter in vocales:
            contador_de_vocales = contador_de_vocales + 1
    return contador_de_vocales
    # TODO: cuenta y devuelve el número de vocales en s


# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("Limewood", 4),
    ("hello", 2),
    ("python", 1),
    ("aeiou", 5),
    ("bcdfg", 0),
    ("Elena Voss", 4),
]

_frag = "RlJBRy1BMjo6dmFjaW8="
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo A",
          puzzle="Puzzle 2 — Patrones de Frecuencia")
