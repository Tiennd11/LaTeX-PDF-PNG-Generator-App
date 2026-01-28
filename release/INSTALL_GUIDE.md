# Installation & Setup Guide

## Prerequisites Check

Before starting, ensure you have:

- [ ] Windows 7 or later
- [ ] Administrator access (for MiKTeX installation)
- [ ] Internet connection (for MiKTeX package downloads)
- [ ] ~500 MB free disk space

---

## Step 1: Install MiKTeX

MiKTeX is the LaTeX distribution that powers this application.

### Download
1. Visit https://miktex.org/download
2. Download the **Windows MiKTeX Installer** (64-bit recommended)
3. File size: ~200 MB

### Install
1. Double-click the downloaded installer
2. Follow the installation wizard:
   - **Installation scope**: "For administrators only" or "For the current user only"
   - **Installation directory**: Keep default (`C:\Users\[YourUsername]\AppData\Local\Programs\MiKTeX`)
   - **Options**: Check "Check for updates"
3. Click "Finish"

### First-Time Setup
- MiKTeX will show a package installation dialog on first use
- Click "Always install missing packages on-the-fly"
- This allows automatic downloading of required LaTeX packages
- **First compilation may take 3-5 minutes** as packages are cached

### Verify Installation
Open Command Prompt and run:
```cmd
pdflatex --version
```

Expected output: Version information with MiKTeX details

---

## Step 2: Install Python (if needed)

Check if Python is already installed:
```cmd
python --version
```

### If Python 3.7+ is installed, skip to Step 3

### If Python is NOT installed:

1. Visit https://www.python.org/downloads/
2. Download **Python 3.11** (Windows x64 installer)
3. Run installer with these options:
   - ✓ **Check "Add Python to PATH"** (IMPORTANT!)
   - Choose "Install Now"
4. Verify installation:
   ```cmd
   python --version
   ```

---

## Step 3: Set Up LaTeX PDF Generator

### Option A: Direct from Folder (Development)

1. Extract or clone the project:
   ```
   c:\Users\An\Documents\VS-codes\latex_gui_app\
   ```

2. Open Command Prompt in this folder:
   - Hold `Shift` + Right-click in empty space
   - Select "Open PowerShell window here"

3. Run the application:
   ```cmd
   python latex_gui.py
   ```

### Option B: Build Standalone Executable (Recommended)

1. Navigate to the project folder
2. Install PyInstaller (one-time):
   ```cmd
   pip install pyinstaller
   ```

3. Build the executable:
   ```cmd
   pyinstaller --onefile --noconsole --name "LaTeX PDF Generator" latex_gui.py
   ```

4. The executable is created at:
   ```
   dist\LaTeX PDF Generator.exe
   ```

5. You can now:
   - Double-click to run
   - Copy to Desktop, Start Menu, or any location
   - Create shortcuts
   - No Python installation needed on other computers

---

## Step 4: First Run

### Verify Everything Works

1. **Open the Application**
   - Direct: `python latex_gui.py` or double-click `.exe`

2. **Test with Simple Equation**
   - Clear the textbox
   - Enter: `E = mc^2`
   - Keep "Display" mode selected
   - Click "Generate PDF"

3. **Expected Result**
   - Status shows: "Compiling..." → "PDF generated successfully"
   - First time: May take 3-5 seconds (normal, MiKTeX is caching)
   - Green success message in status area

4. **Check Output**
   - Click "Open Output Folder"
   - Verify file exists: `equation_YYYYMMDD_HHMMSS.pdf`

### If It Fails

**Common Issues:**

| Issue | Solution |
|-------|----------|
| "pdflatex not found" | MiKTeX not installed. See Step 1. |
| "Python not found" | Python not in PATH. Reinstall with "Add to PATH" checked. |
| Long compilation | MiKTeX installing packages (first run). Wait 3-5 minutes. |
| Syntax error in equation | Check LaTeX syntax. Test in Overleaf.com first. |

---

## Step 5: Set Up for Production Use

### Create Desktop Shortcut

1. Right-click on `latex_gui.exe` (in `dist` folder or wherever you copied it)
2. Select "Create shortcut"
3. Move shortcut to Desktop
4. Right-click shortcut → "Rename"
5. Change name to: "LaTeX PDF Generator"
6. (Optional) Right-click → Properties → Change Icon

### Create Start Menu Entry

**For Windows 10/11:**

1. Open Start Menu
2. Right-click empty space
3. Select "All apps" → Navigate to the application folder
4. Right-click the application
5. "Pin to Start"

**Manual Method:**

1. Create shortcut (see above)
2. Press `Win + R`, type: `shell:startup`
3. Copy shortcut to startup folder

### Set Up Output Folder Shortcut

1. Open: `C:\Users\An\Desktop\latex_exports\`
2. Right-click → "Create shortcut"
3. Place on Desktop for quick access
4. Rename to "LaTeX Exports"

---

## Configuration (Optional)

### Change Output Directory

Edit `latex_gui.py` line 28:

```python
OUTPUT_DIR = Path.home() / "Desktop" / "latex_exports"
# Change to:
OUTPUT_DIR = Path(r"C:\MyCustomFolder\LaTeX_PDFs")
```

Then rebuild if using `.exe`:
```cmd
pyinstaller --onefile --noconsole --name "LaTeX PDF Generator" latex_gui.py
```

### Change MiKTeX Path

If MiKTeX installed to different location, edit line 25:

```python
PDFLATEX_PATH = r"C:\Users\An\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"
# Change to your actual path
```

Find pdflatex location:
```cmd
where pdflatex
```

### Add Custom LaTeX Packages

Edit line 56:

```python
\\usepackage{{amsmath,amssymb}}
# Change to:
\\usepackage{{amsmath,amssymb,physics,siunitx,babel}}
```

---

## Troubleshooting Installation

### Problem: "pdflatex not found" on Startup

**Step 1:** Verify MiKTeX location
```cmd
dir "C:\Users\An\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"
```

**Step 2:** Find actual path
```cmd
where pdflatex
```

**Step 3:** Update `latex_gui.py` line 25 with correct path

**Step 4:** Rebuild executable

### Problem: PyInstaller Build Fails

**Check for syntax errors:**
```cmd
python -m py_compile latex_gui.py
```

**Clean and rebuild:**
```cmd
rmdir /s build dist
pyinstaller --onefile --noconsole --name "LaTeX PDF Generator" latex_gui.py
```

### Problem: MiKTeX Installation Stuck

**Solution:**
1. Open MiKTeX Console:
   ```cmd
   miktex-console
   ```
2. Go to **Updates** tab
3. Check for updates and install
4. Go to **Packages** tab
5. Verify amsmath and amssymb are installed

### Problem: Application Freezes During First Compilation

**This is normal!** 
- MiKTeX is installing packages (~30 seconds)
- Check status window for progress
- Don't force close; let it complete

---

## Verification Checklist

After installation, verify:

- [ ] MiKTeX installed and `pdflatex --version` works
- [ ] Python 3.7+ installed
- [ ] Application launches without errors
- [ ] Can generate simple equation (`E = mc^2`)
- [ ] PDF appears in `C:\Users\An\Desktop\latex_exports\`
- [ ] Can open PDF in default viewer
- [ ] Can import PDF into Affinity Designer 2

---

## Next Steps

1. **Read QUICKSTART.md** for basic usage
2. **Check EXAMPLES.md** for 50+ copy-paste equations
3. **See README.md** for full features and tips
4. **Start designing** with Affinity Designer 2!

---

## Support Resources

- **LaTeX Help**: https://www.overleaf.com/learn
- **MiKTeX Docs**: https://miktex.org/howto/miktex-portable
- **Affinity Designer**: https://affinity.serif.com/en-us/documentation/
- **Test Equations**: https://www.overleaf.com/latex/learn/free-online-introduction-to-latex-part-1

---

## Quick Commands Reference

```cmd
# Verify Python
python --version

# Verify MiKTeX
pdflatex --version

# Run application directly
python latex_gui.py

# Build executable (requires PyInstaller)
pip install pyinstaller
pyinstaller --onefile --noconsole --name "LaTeX PDF Generator" latex_gui.py

# Find pdflatex path
where pdflatex

# Compile Python file (syntax check)
python -m py_compile latex_gui.py

# Open MiKTeX Console
miktex-console
```

---

**You're all set! Start creating beautiful vector equations!**
