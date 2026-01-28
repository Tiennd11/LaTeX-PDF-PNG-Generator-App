@echo off
REM Quick start script for LaTeX PDF Generator
REM Runs the application directly with Python

echo Starting LaTeX PDF Generator...
python latex_gui.py

if errorlevel 1 (
    echo.
    echo Error: Failed to start application
    echo Make sure Python 3.7+ is installed and in your PATH
    pause
)
