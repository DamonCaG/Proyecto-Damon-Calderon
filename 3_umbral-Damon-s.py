import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO B | C2_MB_3
# ─────────────────────────────────────────────────────────
#
# Bitácora Personal — Dr. Mateo Reyes
# Última entrada registrada — fecha ilegible
#
# "El sistema detecta bucles de retroalimentación.
#  Una señal que al invertirse es idéntica a sí misma
#  indica que la red ha alcanzado equilibrio simétrico.
#  A eso le llamamos 'umbral de fusión'.
#  Verificar si una transmisión es un palíndromo
#  es la prueba diagnóstica clave."
#
# Un palíndromo es una palabra que se lee igual
# de izquierda a derecha que de derecha a izquierda.
#
# La función recibe un string. Devuelve True si es
# un palíndromo, False si no lo es.
#
# REGLAS:
# - La función recibe un string s (solo letras, sin espacios)
# - Devuelve True o False
# - No uses s[::-1] directamente — compara carácter por carácter
#   usando un loop o comparando posiciones
# - El string puede tener mayúsculas y minúsculas — tratar todo
#   como minúscula antes de comparar (usa .lower())
#
# Ejemplo:
#   Input:  "racecar"   → Output: True
#   Input:  "radar"     → Output: True
#   Input:  "Neuron"    → Output: False
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    s = s.lower()
    palabra = ""
    for caracter in s:
        palabra = caracter + palabra
    if palabra == s:
        return True
    else:
        return False
        
    # TODO: devuelve True si s es palíndromo, False si no

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("racecar", True),
    ("radar", True),
    ("Neuron", False),
    ("aba", True),
    ("limewood", False),
    ("Aba", True),
]

_frag = "RlJBRy1CNDo6dW1icmFs"
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo B",
          puzzle="Puzzle 4 — Umbral de Fusión")
