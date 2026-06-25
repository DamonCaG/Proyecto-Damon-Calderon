import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO D | C2_MD_0
# ─────────────────────────────────────────────────────────
#
# Diario Personal — Dr. Samuel Chen — Computacion
# Entrada: sin fecha (estimada como la ultima)
#
# "Estoy documentando todo. Cada palabra importa.
#  El protocolo de emergencia requiere que el sistema
#  verifique la longitud de cada transmision contando
#  sus palabras. Si la transmision tiene mas de cierto
#  numero de palabras, activa el protocolo de cierre."
#
# La funcion recibe un string con varias palabras.
# Debes contar cuantas palabras contiene.
# (Una palabra es cualquier secuencia separada por espacios)
#
# REGLAS:
# - La funcion recibe un string s
# - Devuelve el numero de palabras (int)
# - Puedes usar .split() para obtener la lista de palabras
# - Luego cuenta los elementos con un loop o len()
#
# Ejemplo:
#   Input:  "el disco duro guarda secretos"
#   Output: 5
#
#   Input:  "hola"
#   Output: 1
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    palabras = s.split()
    return len(palabras)
    # TODO: devuelve el numero de palabras en el string s

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("el disco duro guarda secretos", 5),
    ("hola", 1),
    ("uno dos tres", 3),
    ("Limewood fue un error", 4),
    ("a b c d e f", 6),
]

_frag = "RlJBRy1EMTo6cHJvdG9jb2xv"
run_tests(solution, tests, _frag,
          module="CASO LIMEWOOD / Módulo D",
          puzzle="Puzzle 1 — Protocolo de Verificacion")
