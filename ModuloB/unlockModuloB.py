import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO B | UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────

print()
print("  ══════════════════════════════════════════════════════")
print("  CASO LIMEWOOD — MÓDULO B")
print("  Archivos: Dr. Mateo Reyes — Físico Cuántico")
print("  ══════════════════════════════════════════════════════")
print()
print("  Verificando fragmentos del Módulo B...")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1CMTo6bmV1cmFs",
    "RlJBRy1CMjo6c2luY3Jvbmlh",
    "RlJBRy1CMzo6ZnJlY3VlbmNpYQ==",
    "RlJBRy1CNDo6dW1icmFs",
}

ingresados = set()
for i in range(1, 5):
    frag = input(f"  Fragmento B{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()

if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  ULTIMA ENTRADA DEL DR. REYES:")
    print("  'El umbral fue cruzado a las 03:17.'")
    print("  'Nadie lo cruzo solo.'")
    print()
    time.sleep(1)
    print("  Calculando clave del Módulo B...")
    time.sleep(1)
    clave = base64.b64decode("bGltZXdvb2RfZXhwZXJpbWVudG8=").decode()
    print(f"  CLAVE MÓDULO B: {clave}")
    print()
    print("  Guarda esta clave. Es una pieza para abrir Final.zip.")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan o son invalidos: {len(faltantes)}")
    print()
    print("  Acceso denegado. Los registros permanecen sellados.")
