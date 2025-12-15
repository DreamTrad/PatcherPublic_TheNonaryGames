# -*- mode: python ; coding: utf-8 -*-


import os
import shutil
import sys

sys.path.append(os.path.abspath("."))

from patcher import config

exe_name = getattr(config, "EXE_NAME", "Patcheur Auto")

dist_dir = "dist"

def copy_folder(src: str, dst: str) -> None:
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

if os.path.exists("dist"):
    copy_folder("tool", os.path.join(dist_dir, "tool"))
    copy_folder("patch", os.path.join(dist_dir, "patch"))

block_cipher = None


a = Analysis(
    ['patcher\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=exe_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='resources/dreamtrad-logo.png',
)
