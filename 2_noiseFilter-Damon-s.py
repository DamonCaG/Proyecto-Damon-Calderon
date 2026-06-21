import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO A | C2_MA_2
# ─────────────────────────────────────────────────────────
#
# Fragmento de log — Sistema de Transmisión Neural
# Fecha: 02/09/1991
#
# "Las transmisiones llegan con ruido insertado entre
#  los caracteres. El ruido se manifiesta como espacios
#  vacíos. Para leer el mensaje real, hay que eliminar
#  todos los espacios del texto recibido."
#
# Necesitas una función que reciba un string y devuelva
# el mismo string SIN ningún espacio (' ').
#
# REGLAS:
# - La función recibe un string s
# - Devuelve el string sin espacios
# - Usa un loop for para construir el resultado
# - No uses el método .replace() — hazlo manualmente
#
# Ejemplo:
# Input:  "L i m e w o o d"
# Output: "Limewood"
#
# Input:  "h o l a   m u n d o"
# Output: "holamundo"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    mensaje_limpio = ""
    for caracter in s:
        if caracter != " ": #comprueba que el caracter sea distinto a un espacio
            mensaje_limpio += caracter #añade los caracteres distintos a un espacio
    return mensaje_limpio
    # TODO: devuelve s sin ningún espacio, usando un loop

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("L i m e w o o d", "Limewood"),
    ("h o l a", "hola"),
    ("sin espacios", "sinespacios"),
    ("   ", ""),
    ("abc", "abc"),
    ("E l e n a   V o s s", "ElenaVoss"),
]

_frag = "RlJBRy1BMzo6c2lsZW5jaW8="
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo A",
          puzzle="Puzzle 3 — Filtro de Ruido")
