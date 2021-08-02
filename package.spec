# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


datas = [
  ('./requires', '.')
]

a = Analysis(['src\\__main__.py'],
             pathex=['F:\\dev\\code\\mine\\bmfont'],
             binaries=[],
             datas=datas,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='BMFontToolbox',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          clean=True,
          upx=True,
          console=False,
          icon='src/static/app.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='BMFontToolbox')
