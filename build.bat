@echo off
REM Quick build script for LaTeX PDF Generator
REM Creates a standalone .exe using PyInstaller

echo.
echo ========================================
echo  LaTeX PDF Generator - Build Script
echo ========================================
echo.

REM Check if PyInstaller is installed
python -m pip show pyinstaller > nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    python -m pip install pyinstaller
    if errorlevel 1 (
        echo Error: Failed to install PyInstaller
        pause
        exit /b 1
    )
)

echo.
echo Building executable...
echo This may take a minute...
echo.

REM Build the executable
pyinstaller --onefile --noconsole --name "LaTeX PDF Generator" latex_gui.py

if errorlevel 1 (
    echo.
    echo Error: Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Build Complete!
echo ========================================
echo.
echo Executable created at:
echo   dist\LaTeX PDF Generator.exe
echo.
echo You can now:
echo 1. Double-click the .exe to run the application
echo 2. Create a shortcut on your Desktop
echo 3. Pin to Start menu for quick access
echo.
pause
