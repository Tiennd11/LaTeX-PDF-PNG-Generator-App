@echo off
REM System Check Script for LaTeX PDF Generator
REM Verifies all requirements are installed and configured

echo.
echo ========================================
echo  LaTeX PDF Generator - System Check
echo ========================================
echo.

setlocal enabledelayedexpansion

REM Check Python
echo [1] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo   ERROR: Python not found in PATH
    echo   Please install Python 3.7+ from https://www.python.org/
    set ERROR=1
) else (
    for /f "tokens=*" %%i in ('python --version') do set PYTHON_VER=%%i
    echo   OK: !PYTHON_VER!
)

echo.

REM Check pdflatex
echo [2] Checking MiKTeX pdflatex...
pdflatex --version >nul 2>&1
if errorlevel 1 (
    echo   ERROR: pdflatex not found in PATH
    echo   Please install MiKTeX from https://miktex.org/
    set ERROR=1
) else (
    echo   OK: pdflatex found
    echo   Location:
    for /f "tokens=*" %%i in ('where pdflatex') do (
        echo     %%i
    )
)

echo.

REM Check specific MiKTeX path
echo [3] Checking MiKTeX installation path...
if exist "C:\Users\An\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe" (
    echo   OK: Found at default location
    echo     C:\Users\An\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe
) else (
    echo   WARNING: Not at default path
    echo   If MiKTeX is installed elsewhere, edit latex_gui.py line 25
)

echo.

REM Check tkinter
echo [4] Checking tkinter (GUI library)...
python -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo   ERROR: tkinter not found
    echo   tkinter is included with Python. Reinstall Python with tkinter.
    set ERROR=1
) else (
    echo   OK: tkinter available
)

echo.

REM Check PyInstaller (optional)
echo [5] Checking PyInstaller (for building .exe)...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo   NOT INSTALLED (optional - only needed to build .exe)
    echo   To build executable: pip install pyinstaller
) else (
    echo   OK: PyInstaller installed
)

echo.

REM Check output directory
echo [6] Checking output directory...
if not exist "%USERPROFILE%\Desktop" (
    echo   WARNING: Desktop folder not found
) else (
    echo   OK: Desktop found
    echo   Output will be created at: %USERPROFILE%\Desktop\latex_exports\
)

echo.

REM Summary
if defined ERROR (
    echo ========================================
    echo  System Check: FAILED
    echo ========================================
    echo.
    echo Please resolve the errors above before running the application.
    echo.
) else (
    echo ========================================
    echo  System Check: PASSED
    echo ========================================
    echo.
    echo All required components are installed!
    echo You can now run: python latex_gui.py
    echo.
)

REM Offer to run application
echo.
set /p CHOICE="Would you like to start the application now? (y/n): "
if /i "!CHOICE!"=="y" (
    echo.
    echo Starting LaTeX PDF Generator...
    echo.
    python latex_gui.py
) else (
    echo.
    echo To start the application later, run: python latex_gui.py
    echo.
)

pause
