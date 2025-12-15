"""
File        : tool.py
Author      : Silous
Created on  : 2025-10-08
Description : call tool to repack the game.
"""

# == Imports ==================================================================

from logging import Logger
from pathlib import Path
import subprocess

# -------------------- Import Lib User -------------------

from patcher import config
from patcher.utils import xdelta
from patcher.utils.logger import get_logger


# == Global Variables =========================================================

_logger: Logger = get_logger(__name__)


# == Functions ================================================================

def repack() -> None:
    """whole patching process."""
    _call_repack()


def _call_repack() -> None:
    xdelta.apply_xdelta_patch(
        target_file=str(Path(config.GAME_FOLDER) / "Launcher.exe"),
        patch_file=str(config.PATCH_FOLDER / "Launcher.exe.xdelta"),
    )
    xdelta.apply_xdelta_patch(
        target_file=str(Path(config.GAME_FOLDER) / "ze1_data.bin"),
        patch_file=str(config.PATCH_FOLDER / "ze1_data.bin.xdelta"),
    )
    xdelta.apply_xdelta_patch(
        target_file=str(Path(config.GAME_FOLDER) / "ze1.exe"),
        patch_file=str(config.PATCH_FOLDER / "ze1.exe.xdelta"),
    )
    xdelta.apply_xdelta_patch(
        target_file=str(Path(config.GAME_FOLDER) / "ze2_data_en_us.bin"),
        patch_file=str(config.PATCH_FOLDER / "ze2_data_en_us.bin.xdelta"),
    )