import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO A | C2_MA_0
# ─────────────────────────────────────────────────────────
#
# El primer archivo del disco llegó corrompido.
# Los datos están escritos al revés — como si alguien
# hubiera intentado ocultarlos invirtiéndolos.
#
# El sistema de recuperación necesita una función que
# tome un string y devuelva el texto en orden inverso.
# ————————————————
# REGLAS:
# - La función recibe un string s
# - Debe devolver ese mismo string al revés
# - No uses s[::-1] directamente — construye el resultado
#   usando un loop for y concatenación de strings
#
# Ejemplo:
#   Input:  "nodamil"
#   Output: "limadón"  → no, más simple:
#
#   Input:  "abcd"
#   Output: "dcba"
#
#   Input:  "Limewood"
#   Output: "doomewiL"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    texto_invertido = "" #texto_invertido se encuentra vacío
    for letra in s:
        texto_invertido = letra + texto_invertido #añade cada nuevo caracter al inicio
    return texto_invertido
    # TODO: devuelve el string s al revés usando un loop

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("Limewood", "doowemiL"),
    ("abcd", "dcba"),
    ("hola", "aloh"),
    ("123", "321"),
    ("racecar", "racecar"),
]

_frag = "RlJBRy1BMTo6bGltcGlv"
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo A",
          puzzle="Puzzle 1 — Texto Invertido")
