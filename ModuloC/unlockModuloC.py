import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO C | UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────

print()
print("  ══════════════════════════════════════════════════════")
print("  CASO LIMEWOOD — MÓDULO C")
print("  Archivos: Dra. Irina Sokol — Matematica de Redes")
print("  ══════════════════════════════════════════════════════")
print()
print("  Verificando fragmentos del Módulo C...")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1DMTo6ZnVzaW9u",
    "RlJBRy1DMjo6Y29sZWN0aXZv",
    "RlJBRy1DMzo6Y29sYXBzbw==",
    "RlJBRy1DNDo6aWRlbnRpZGFk",
}

ingresados = set()
for i in range(1, 5):
    frag = input(f"  Fragmento C{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()

if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  ULTIMO MENSAJE DE LA DRA. SOKOL:")
    print("  'La identidad es solo un patron que se repite.'")
    print("  'Cuando deja de repetirse... sigue siendo alguien?'")
    print()
    time.sleep(1)
    print("  Calculando clave del Módulo C...")
    time.sleep(1)
    clave = base64.b64decode("bGltZXdvb2RfY29sYXBzbw==").decode()
    print(f"  CLAVE MÓDULO C: {clave}")
    print()
    print("  Guarda esta clave. Es una pieza para abrir Final.zip.")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan o son invalidos: {len(faltantes)}")
    print()
    print("  Acceso denegado. Los registros permanecen sellados.")
