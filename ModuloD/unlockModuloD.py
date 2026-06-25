import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# CASO LIMEWOOD | MÓDULO D | UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────

print()
print("  ══════════════════════════════════════════════════════")
print("  CASO LIMEWOOD — MÓDULO D")
print("  Archivos: Dr. Samuel Chen — Computacion")
print("  ══════════════════════════════════════════════════════")
print()
print("  Verificando fragmentos del Módulo D...")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1EMTo6cHJvdG9jb2xv",
    "RlJBRy1EMjo6ZGVzY29uZXhpb24=",
    "RlJBRy1EMzo6cmVzaWR1YWw=",
    "RlJBRy1ENDo6bGVjdG9y",
}

ingresados = set()
for i in range(1, 5):
    frag = input(f"  Fragmento D{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()

if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  ARCHIVO FINAL DEL DR. CHEN — SIN CIFRAR:")
    print()
    print("  'No hubo evacuacion porque no habia nadie que evacuara.'")
    print("  'La red no los mato. Los convirtio en ella misma.'")
    print("  'Y ahora tu has leido todos sus archivos.'")
    print("  'Sus patrones estan en tu memoria.'")
    print("  'Bienvenido a Limewood.'")
    print()
    time.sleep(1.5)
    print("  Calculando clave del Módulo D...")
    time.sleep(1)
    clave = base64.b64decode("bGltZXdvb2RfZXJlc190dQ==").decode()
    print(f"  CLAVE MÓDULO D: {clave}")
    print()
    print("  Esta es la ultima pieza para abrir Final.zip.")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan o son invalidos: {len(faltantes)}")
    print()
    print("  Acceso denegado. Los registros permanecen sellados.")
