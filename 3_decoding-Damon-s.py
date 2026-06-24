import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO C | C2_MC_3
# ─────────────────────────────────────────────────────────
#
# Mensaje final — Dra. Irina Sokol
# (transmitido en frecuencia de baja prioridad)
#
# "Si alguien lee esto, el mensaje fue codificado
#  reemplazando todas las letras 'e' por el símbolo '#'.
#  Para leerlo correctamente hay que revertir ese cambio:
#  reemplazar cada '#' de vuelta por una 'e'."
#
# La función recibe un string donde '#' representa 'e'.
# Debes reemplazar cada '#' por la letra 'e'.
#
# REGLAS:
# - La función recibe un string s
# - Devuelve el string con cada '#' reemplazado por 'e'
# - Usa un loop for para construir el resultado carácter por carácter
# - No uses el método .replace()
#
# Ejemplo:
#   Input:  "lim#wood #s r#al"
#   Output: "limewood es real"
#
#   Input:  "###"
#   Output: "eee"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    palabras_con_e = ""
    for caracter in s:
        if caracter == "#":
            palabras_con_e += "e"
        else:
            palabras_con_e += caracter
    return palabras_con_e
    # TODO: devuelve s con cada '#' reemplazado por 'e'

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("lim#wood #s r#al", "limewood es real"),
    ("###", "eee"),
    ("sinCambios", "sinCambios"),
    ("#l#na", "elena"),
    ("t#st d# r#d", "test de red"),
]

_frag = "RlJBRy1DNDo6aWRlbnRpZGFk"
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo C",
          puzzle="Puzzle 4 — Decodificacion del Mensaje")
