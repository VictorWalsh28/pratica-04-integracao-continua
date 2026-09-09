from pathlib import Path
import sys

code = Path("devsecops_demo/app.py").read_text(encoding="utf-8")

patterns = [
    'f"WHERE username =',
    "f'WHERE username =",
]

if any(pattern in code for pattern in patterns):
    print("Vulnerabilidade detectada: consulta SQL construída com interpolação direta.")
    print("Arquivo: devsecops_demo/app.py")
    print("Regra: python-sql-injection-string-format")
    sys.exit(1)

print("Relatório SAST validado: nenhuma concatenação insegura detectada.")
