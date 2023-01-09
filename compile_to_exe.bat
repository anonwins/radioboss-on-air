rem dependencies: pyinstaller, pyinstaller-versionfile

@echo off

cd /D "%~dp0"

create-version-file version.yml --outfile version.txt

pyinstaller --onefile -i "on-air.ico" --add-binary "inpoutx64.dll;." "radioboss-on-air.py" --version-file "version.txt"