@echo off

REM --- set scripts directory
set "scripts=G:\My Drive\_Utility\Other\GenerateProjectDirs"

REM --- set counter file
set "counterFile=%scripts%\counter.txt"

REM --- get counter value
set /p counter=<"%counterFile%"

REM --- set virtual environment directory
set "venv=%scripts%\env"

REM --- check if venv exists, if not create it
IF NOT EXIST "%venv%" (
    echo Creating virtual environment...
    python -m venv "%venv%"
)

REM --- activate venv
call "%venv%\Scripts\activate.bat"

REM --- check if counter is 30 or blank, then update pip and install requirements
if "%counter%"=="30" (
    REM --- reset counter
    echo 0 > "%counterFile%"
    REM --- install/upgrade pip to ensure the latest version is used
    python -m pip install --upgrade pip

    REM --- install requirements
    echo Installing requirements...
    python -m pip install -r "%scripts%\requirements.txt"
) else if "%counter%"=="" (
    REM --- if counterFile empty, set counter to 1 and update pip and install requirements
    echo 1 > "%counterFile%"
    python -m pip install --upgrade pip
    echo Installing requirements...
    python -m pip install -r "%scripts%\requirements.txt"
) else (
    REM --- increment counter and do nothing else
    echo %counter% + 1| set /a result=%counter% + 1 > "%counterFile%"
)

REM --- run Python script
echo Running script...
python "%scripts%\createNewJobFolders.py" "%~1"

REM --- deactivate venv
call deactivate

pause