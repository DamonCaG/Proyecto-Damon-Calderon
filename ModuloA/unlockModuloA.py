import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO A | UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────
#
# "Los archivos de la Dra. Voss están sellados.
#  Cuatro fragmentos. Cuatro piezas de su mente.
#  Introdúcelas para reconstruir su acceso."
#

print()
print("  ══════════════════════════════════════════════════════")
print("  CASO LIMEWOOD — MÓDULO A")
print("  Archivos: Dra. Elena Voss — Psicóloga Jefe")
print("  ══════════════════════════════════════════════════════")
print()
print("  Verificando fragmentos del Módulo A...")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1BMTo6bGltcGlv",
    "RlJBRy1BMjo6dmFjaW8=",
    "RlJBRy1BMzo6c2lsZW5jaW8=",
    "RlJBRy1BNDo6cmVnaXN0cm8=",
}

ingresados = set()
for i in range(1, 5):
    frag = input(f"  Fragmento A{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()

if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  ...")
    time.sleep(0.5)
    print("  Reconstruyendo perfil neural de la Dra. Voss...")
    time.sleep(1.2)
    print()
    print("  ENTRADA DE DIARIO — ÚLTIMA FECHA REGISTRADA:")
    print("  'Ya no sé dónde termino yo y dónde empiezan ellos.'")
    print("  '¿Importa eso todavía?'")
    print()
    time.sleep(1)
    print("  Calculando clave del Módulo A...")
    time.sleep(1)
    clave = base64.b64decode("bGltZXdvb2RfZnVuZGFjaW9u").decode()
    print(f"  CLAVE MÓDULO A: {clave}")
    print()
    print("  Guarda esta clave. Es una pieza para abrir Final.zip.")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan o son inválidos: {len(faltantes)}")
    print()
    print("  Acceso denegado. Los registros permanecen sellados.")
