@echo off
set current_path="%cd%"
set CMD_PATH=
for %%P in (%0) do set CMD_PATH=%%~dpP
cd /d "%CMD_PATH%"

java -jar packagetool.jar mergeIcon --icon %1

pause