# == Imports ==================================================================

import pathlib

# == INFORMATIONS GÉNÉRALES ===================================================

# Nom de la fenêtre du logiciel
NAME_WINDOW: str = "DreamTrad : Patcheur de Zero Escape - The Nonary Games"

# Indique si le jeu est une version Steam
IS_STEAM_GAME: bool = True
# Nom du dossier du jeu dans Steam (utilisé uniquement si IS_STEAM_GAME = True)
STEAM_FOLDER: str = "Zero Escape The Nonary Games"

# == INTERFACE UTILISATEUR ====================================================

OTHERS_CHECKBOXES: dict[str, tuple[str, bool]] = {
    "launcher": ("Patcher launcher", True),
    "999": ("Patcher 9 Hours, 9 Persons, 9 Doors", True),
    "vlr": ("Patcher Virtue's Last Reward", True)
}
"""Liste des cases à cocher supplémentaires, clé: (texte, valeur par défaut)"""

# == OUTILS / ENVIRONNEMENT ===================================================

# Dossier où se trouvent les outils cmd (repack, etc.)
TOOL_FOLDER = pathlib.Path("tool")
# Dossier où se trouvent les fichiers patch
PATCH_FOLDER = pathlib.Path("patch")

# == VARIABLES INTERNES (à ne pas modifier manuellement) ======================

# Dossier du jeu, défini dynamiquement à l’exécution
GAME_FOLDER: pathlib.Path = pathlib.Path("")

CHECKBOX_VALUES: dict[str, bool] = {}
"""Valeurs cochées des options (remplies par l’application)"""