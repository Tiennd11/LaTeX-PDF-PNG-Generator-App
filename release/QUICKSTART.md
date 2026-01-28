# Quick Start Guide

## Step 1: Install Requirements

### Install MiKTeX
1. Download from https://miktex.org/
2. Install with default settings
3. Wait for initial package installation to complete

### Install Python Packages
```bash
pip install pyinstaller
```

## Step 2: Run the Application

### Option A: Direct Python (Development)
```bash
python latex_gui.py
```

### Option B: Batch Script
Double-click `run.bat` to launch the application.

## Step 3: Build Executable (Optional)

### Automated Build
Double-click `build.bat` to create a standalone `.exe`

### Manual Build
```bash
pyinstaller --onefile --noconsole --name "LaTeX PDF Generator" latex_gui.py
```

The executable will be in the `dist` folder.

## Usage Example

1. Open the application (either via Python or the .exe)
2. Enter LaTeX equation in the textbox:
   ```
   E = mc^2
   ```
3. Select display mode (Inline or Display)
4. Click "Generate PDF"
5. Click "Open PDF" to preview
6. In Affinity Designer 2: **File → Place…** and select the PDF
7. The equation appears as a vector graphic in your design

## Output Location

All PDFs are saved to: `C:\Users\An\Desktop\latex_exports\`

Generated files look like: `equation_20260128_143025.pdf`

## Troubleshooting

**Application won't start:**
- Ensure Python 3.7+ is installed
- Run `python --version` in command prompt

**"pdflatex not found" error:**
- Verify MiKTeX is installed
- Check path: `C:\Users\An\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe`

**PDF generation fails:**
- Check LaTeX syntax in the status area
- Common: Use `\\` for backslashes, `\frac{a}{b}` for fractions

**First equation takes a while:**
- Normal! MiKTeX caches packages on first use (3-5 seconds)
- Subsequent equations are faster (1-2 seconds)

## Tips

- Keep LaTeX equations simple for faster compilation
- Test equations in Overleaf first: https://www.overleaf.com/
- Use Display mode for centered, prominent equations
- Use Inline mode for equations that blend with text

---

**All set! Start generating beautiful vector equations!**
