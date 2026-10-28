#!/usr/bin/env python3

import ast
import compileall
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADDONS_DIR = ROOT / "addons"
ERRORS = []
MODULES = []


def error(message):
    ERRORS.append(message)
    print(f"ERREUR: {message}")


if not ADDONS_DIR.is_dir():
    error(f"Répertoire absent : {ADDONS_DIR}")
else:
    for module_dir in sorted(ADDONS_DIR.iterdir()):
        if module_dir.name.startswith(".") or not module_dir.is_dir():
            continue

        init_file = module_dir / "__init__.py"
        manifest_file = module_dir / "__manifest__.py"

        if not init_file.is_file():
            error(f"{module_dir.name}: __init__.py absent")
            continue

        if not manifest_file.is_file():
            error(f"{module_dir.name}: __manifest__.py absent")
            continue

        try:
            manifest = ast.literal_eval(
                manifest_file.read_text(encoding="utf-8")
            )
        except Exception as exc:
            error(f"{module_dir.name}: manifeste invalide: {exc}")
            continue

        if not isinstance(manifest, dict):
            error(f"{module_dir.name}: le manifeste doit être un dictionnaire")
            continue

        if not manifest.get("name"):
            error(f"{module_dir.name}: champ 'name' absent")

        if not manifest.get("version"):
            error(f"{module_dir.name}: champ 'version' absent")

        depends = manifest.get("depends", [])
        if not isinstance(depends, list):
            error(f"{module_dir.name}: 'depends' doit être une liste")

        MODULES.append(module_dir.name)


print(f"Modules détectés : {len(MODULES)}")

for module in MODULES:
    print(f"  - {module}")

print("Vérification de la syntaxe Python...")

if not compileall.compile_dir(
    str(ADDONS_DIR),
    quiet=1,
    force=True,
):
    error("Échec de compilation Python")

if ERRORS:
    print(f"\nValidation échouée : {len(ERRORS)} erreur(s).")
    sys.exit(1)

print("\nValidation terminée avec succès.")
