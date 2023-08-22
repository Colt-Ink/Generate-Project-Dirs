@echo off

REM --- set scripts directory
set "scripts=E:\MEGA\MEGA\Scripts\Create Job Folders - Win"

REM --- set virtual environment directory
set "venv=%scripts%\env"

REM --- check if venv exists, if not create it
IF NOT EXIST "%venv%" (
    echo Creating virtual environment...
    python -m venv "%venv%"
)

REM --- activate venv
call "%venv%\Scripts\activate.bat"

REM --- install/upgrade pip to ensure the latest version is used
python -m pip install --upgrade pip

REM --- install requirements
echo Installing requirements...
python -m pip install -r "%scripts%\requirements.txt"

REM --- run Python script
echo Running script...
python "%scripts%\createNewJobFolders.py" "%cd%"

REM --- deactivate venv
call deactivate

pause