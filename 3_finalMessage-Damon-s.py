import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO D | C2_MD_3
# ─────────────────────────────────────────────────────────
#
# Ultimo Archivo del Disco — Dr. Samuel Chen
# Mensaje cifrado con desplazamiento de 3 posiciones
#
# "Si estas leyendo esto, encontraste el archivo final.
#  Este mensaje fue cifrado con un desplazamiento simple:
#  cada letra fue avanzada 3 posiciones en el alfabeto.
#  Para leerlo, hay que retroceder 3 posiciones.
#
#  'a' cifrada se convirtio en 'd'
#  'd' cifrada se convirtio en 'g'
#  El cifrado solo afecta letras minusculas.
#  Espacios y otros caracteres NO cambian."
#
# La funcion recibe un string cifrado (solo minusculas y espacios).
# Debes devolver el string descifrado: cada letra retrocede
# 3 posiciones en el alfabeto. La 'a' retrocede 3 y llega a 'x'.
#
# REGLAS:
# - La funcion recibe un string s
# - Solo letras minusculas (a-z) son afectadas
# - Los espacios y otros caracteres se mantienen igual
# - Usa ord() para obtener el codigo ASCII y chr() para convertir
# - ord('a') == 97, ord('z') == 122
# - Para manejar el ciclo (a->x): usa el operador modulo (%)
#
# Ejemplo:
#   Input:  "khoor"
#   Output: "hello"    (k->h, h->e, o->l, o->l, r->o)
#
#   Input:  "olphzrrg"
#   Output: "limewood"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    resultado = ""
    for caracter in s:
        if caracter == " ":
            resultado += caracter
        elif caracter == caracter.lower():
            posición_inicial = ord(caracter) - ord('a')
            posición_nueva = (posición_inicial - 3) %26
            letra_original = chr(posición_nueva + ord('a'))
            resultado += letra_original
        else:
            resultado += caracter
    return resultado
    # TODO: descifra s retrocediendo 3 posiciones cada letra minuscula

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("khoor", "hello"),
    ("olphzrrg", "limewood"),
    ("hola", "elix"),
    ("abc", "xyz"),
    ("khoor zruog", "hello world"),
]

_frag = "RlJBRy1ENDo6bGVjdG9y"
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo D",
          puzzle="Puzzle 4 — El Mensaje Final")
