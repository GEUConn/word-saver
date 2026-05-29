@echo off
cd /d "%~dp0"
python -m pip install pyinstaller --quiet
pyinstaller --onefile --windowed --name WordSaver --icon icon.ico --uac-admin --hidden-import plyer.platforms.win.notification --hidden-import pystray._win32 --collect-data eng_to_ipa word_saver.py
if exist "dist\WordSaver.exe" (
    copy "dist\WordSaver.exe" "%~dp0WordSaver.exe" >nul
    echo Done! WordSaver.exe is ready.
) else (
    echo Build failed.
)
pause
