import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO A | C02_MA_3
# ─────────────────────────────────────────────────────────
#
# Protocolo de Identificación — Limewood, 1991
#
# "Para registrar a cada residente en la base de datos
#  neural, los nombres deben estar en formato título:
#  la primera letra de cada palabra en mayúscula,
#  el resto en minúscula.
#  Los registros corruptos usan todo minúsculas."
#
# Necesitas una función que reciba un string con palabras
# en minúscula y devuelva cada palabra con su primera
# letra en mayúscula.
# ———————————————————————————————
# REGLAS:
# - La función recibe un string s con palabras separadas por espacios
# - Devuelve el string con cada palabra capitalizada
# - Usa un loop for y la lista de palabras
# - Puedes usar .split() para separar y " ".join() para unir
# - Puedes usar .upper() en un solo carácter y .lower() en el resto
#
# Ejemplo:
#   Input:  "elena voss"
#   Output: "Elena Voss"
#
#   Input:  "limewood proyecto neural"
#   Output: "Limewood Proyecto Neural"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    texto_capitalizado = ""
    for x in range(len(s)): #recorre todo el texto/string y toma sus caracteres como si fueran números por su longitud
        caracter = s[x]
        if x == 0 or s[x - 1] == " ": #juzga si el caracter es el primero o si está luego de un espacio
            caracter = caracter.upper()
        else:
            caracter = caracter.lower()
        texto_capitalizado += caracter
    return texto_capitalizado
    # TODO: capitaliza la primera letra de cada palabra

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("elena voss", "Elena Voss"),
    ("limewood proyecto neural", "Limewood Proyecto Neural"),
    ("hola mundo", "Hola Mundo"),
    ("abc", "Abc"),
    ("un dos tres cuatro", "Un Dos Tres Cuatro"),
]

_frag = "RlJBRy1BNDo6cmVnaXN0cm8="
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo A",
          puzzle="Puzzle 4 — Registro de Identidades")
