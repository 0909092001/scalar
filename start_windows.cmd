@echo off
REM AI System Workshop - Windows one-click starter

echo ==========================================
echo   AI System Workshop - Starting Jupyter
echo ==========================================
echo.

REM Go to the folder where this file exists
cd /d "%~dp0"

REM Create a local virtual environment if not present
if not exist ".venv" (
  echo Creating virtual environment (.venv)...
  python -m venv .venv
)

REM Activate venv
call .venv\Scripts\activate

echo Installing dependencies (first time may take a minute)...
pip install -q --upgrade pip
pip install -q pandas numpy scikit-learn matplotlib seaborn jupyter

echo.
echo Launching Jupyter Notebook...
python -m jupyter notebook

pause
