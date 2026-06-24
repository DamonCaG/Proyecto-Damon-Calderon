import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO C | C2_MC_1
# ─────────────────────────────────────────────────────────
#
# Notas Teóricas — Dra. Irina Sokol
# "En una red de mentes fusionadas, la identidad más
#  fuerte domina. En el modelo matemático, la identidad
#  dominante es siempre la que más 'peso' tiene.
#  En texto, el peso es la longitud: la palabra más larga
#  es la que persiste cuando todo lo demás colapsa."
#
# La función recibe un string con varias palabras separadas
# por espacios. Debes devolver la palabra más larga.
# Si hay empate, devuelve la primera que aparezca.
#
# REGLAS:
# - La función recibe un string s con palabras separadas por espacios
# - Devuelve la palabra más larga (string)
# - Puedes usar .split() para obtener la lista de palabras
# - Usa un loop for para encontrar la más larga
# - En caso de empate, devuelve la primera
#
# Ejemplo:
#   Input:  "hola limewood mundo"
#   Output: "limewood"
#
#   Input:  "yo tu el"
#   Output: "yo"    (empate, primera)
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    palabras = s.split()
    palabra_mas_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga
    
    # TODO: devuelve la palabra más larga del string s

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("hola limewood mundo", "limewood"),
    ("yo tu el", "yo"),
    ("sincronizacion neural cerebral", "sincronizacion"),
    ("abc de fghij", "fghij"),
    ("uno", "uno"),
]

_frag = "RlJBRy1DMjo6Y29sZWN0aXZv"
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo C",
          puzzle="Puzzle 2 — Identidad Dominante")
