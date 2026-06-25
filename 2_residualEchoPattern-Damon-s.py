import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO D | C2_MD_2
# ─────────────────────────────────────────────────────────
#
# Analisis de Transmision Residual — Dr. Chen
# Archivo de audio convertido a texto
#
# "Las transmisiones que quedan 'atrapadas' en la red
#  muestran un patron de eco: cada caracter se repite
#  exactamente 3 veces antes de continuar con el siguiente.
#  Para identificar mensajes residuales, el decodificador
#  debe poder generar ese patron a partir de un texto normal."
#
# La funcion recibe un string.
# Debes devolver el string donde cada caracter aparece
# repetido 3 veces.
#
# REGLAS:
# - La funcion recibe un string s
# - Devuelve un string donde cada caracter se repite 3 veces
# - Usa un loop for
# - Puedes usar concatenacion de strings o multiplicacion de string
#
# Ejemplo:
#   Input:  "hola"
#   Output: "hhhooolllaaa"
#
#   Input:  "abc"
#   Output: "aaabbbccc"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    caracteres_repetidos = ""
    for caracter in s:
        caracteres_repetidos += caracter *3
    return caracteres_repetidos
    # TODO: devuelve s con cada caracter repetido 3 veces

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("hola", "hhhooolllaaa"),
    ("abc", "aaabbbccc"),
    ("x", "xxx"),
    ("hi", "hhhiii"),
    ("eco", "eeecccooo"),
]

_frag = "RlJBRy1EMzo6cmVzaWR1YWw="
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo D",
          puzzle="Puzzle 3 — Patron de Eco Residual")
