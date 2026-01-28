# LaTeX PDF Generator

A lightweight Windows desktop application for generating vector PDFs and PNGs from LaTeX math equations. Perfect for importing into graphic design software like Affinity Designer 2, Adobe Illustrator, or any vector graphics editor.

## ✨ Features

- **Clean GUI Interface**: Simple Tkinter-based interface for easy LaTeX input
- **Vector PDF Generation**: Creates crisp, scalable vector PDFs perfect for print and design work
- **PNG Export**: Convert equations to high-resolution PNG images (300/600/1200 DPI)
- **Tight Cropping**: Minimal whitespace with automatic border trimming using varwidth
- **Display Modes**: Choose between inline (`$...$`) or display (`\[...\]`) equation styles
- **CMU Serif Font**: Uses 10pt Computer Modern (lmodern package) for professional typography
- **Quick Access**: "Show in Explorer" button for easy drag-and-drop to other applications
- **Error Handling**: Clear error messages with last 30 lines of pdflatex log on failures
- **Lightweight**: ~10MB standalone executable with no external dependencies (except MiKTeX)

## 📋 Requirements

### Required
- **Windows 10/11** (64-bit)
- **MiKTeX** (LaTeX distribution)
  - Download: https://miktex.org/download
  - Installer will set up default paths automatically

### Optional (for PNG generation)
- **Ghostscript** (for PDF to PNG conversion)
  - Download: https://www.ghostscript.com/releases/gsdnld.html
  - Recommended: Install to `C:\Program Files\gs\`

## 🚀 Quick Start

### Option 1: Use Pre-built Executable (Recommended)

1. Download the latest release ZIP
2. Extract to any folder
3. Double-click `LaTeX PDF Generator.exe`
4. Enter your LaTeX equation (e.g., `\frac{a}{b}`)
5. Click **Generate PDF**
6. PDFs saved to: `%USERPROFILE%\Desktop\latex_exports\`

### Option 2: Run from Python Source

```bash
# Clone or download the repository
git clone https://github.com/yourusername/latex-pdf-generator.git
cd latex-pdf-generator

# Run directly (no pip install needed!)
python latex_gui.py
```

## 📦 Installation Guide

### Step 1: Install MiKTeX

1. **Download** MiKTeX: https://miktex.org/download
2. **Run installer** - use all default settings
3. **Verify** installation:
   ```cmd
   pdflatex --version
   ```
   Should show: `MiKTeX-pdfTeX 4.xx ...`

### Step 2: First Run Setup

On first PDF generation, MiKTeX will prompt to install required packages:
- `standalone` - tight PDF cropping
- `preview` - equation rendering  
- `amsmath`, `amssymb` - math symbols
- `lmodern` - Computer Modern fonts
- `varwidth` - horizontal trimming

**Click "Install" when prompted** - this is automatic!

### Step 3: (Optional) Install Ghostscript

Only needed if you want PNG export:

1. **Download** Ghostscript: https://www.ghostscript.com/releases/gsdnld.html
2. **Install** to default location
3. App will auto-detect it

**Custom path?** Edit line 25 in `latex_gui.py`:
```python
GHOSTSCRIPT_PATH = r"C:\Your\Path\gswin64c.exe"
```

## 🎯 Usage Examples

### Simple Equations

```latex
\frac{a}{b}
```

```latex
x^2 + y^2 = r^2
```

### Quadratic Formula
```latex
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```

### Summation
```latex
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
```

### Matrix
```latex
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
```

### Calculus
```latex
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
```

### Complex Equation (Navier-Stokes)
```latex
\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla) \mathbf{u} = -\frac{1}{\rho} \nabla p + \nu \nabla^2 \mathbf{u} + \mathbf{f}
```

**50+ more examples** → See [EXAMPLES.md](EXAMPLES.md)

## ⚙️ Configuration

### Custom MiKTeX Path

If MiKTeX installed elsewhere, edit line 24 in `latex_gui.py`:

```python
PDFLATEX_PATH = r"C:\Your\Path\pdflatex.exe"
```

To find your path:
```cmd
where pdflatex
```

### Custom Output Directory

Default: `Desktop\latex_exports\`

To change, edit line 26 in `latex_gui.py`:
```python
OUTPUT_DIR = Path.home() / "Documents" / "My_LaTeX_PDFs"
```

### Adjust PDF Border

Edit line ~47 in `latex_gui.py`:
```python
border=1pt        # Try: 0pt, 0.5pt, 1pt, 2pt
```

## 🔧 Building from Source

### Build Standalone .exe

```bash
# Install PyInstaller
pip install pyinstaller

# Build (creates ~10MB exe)
pyinstaller --onefile --noconsole --name "LaTeX PDF Generator" latex_gui.py

# Output: dist\LaTeX PDF Generator.exe
```

### Quick Build Scripts

```cmd
REM Windows batch files included:
build.bat          - Build .exe with PyInstaller
run.bat            - Run from Python source
check_system.bat   - Verify MiKTeX installation
```

## 📂 Project Structure

```
latex-pdf-generator/
├── latex_gui.py                    # Main application (480 lines)
├── README.md                       # This file
├── LICENSE                         # MIT License
├── .gitignore                      # Git ignore rules
├── INSTALL_GUIDE.md               # Detailed setup guide
├── EXAMPLES.md                    # 50+ LaTeX examples
├── QUICKSTART.md                  # 3-step quick start
├── build.bat                      # Build script
├── run.bat                        # Run script
├── check_system.bat               # System checker
└── dist/
    └── LaTeX PDF Generator.exe    # Compiled executable
```

## 🐛 Troubleshooting

### ❌ "MiKTeX pdflatex not found"

**Solution 1**: Install MiKTeX
- Download: https://miktex.org/download
- Use default installation path

**Solution 2**: Update path in code
```python
# Edit line 24 in latex_gui.py
PDFLATEX_PATH = r"C:\Your\MiKTeX\Path\pdflatex.exe"
```

### ❌ "Package XXX not found"

**Solution**: Allow auto-install
- On first run, MiKTeX will prompt to install packages
- Click **"Install"** - it's automatic
- Or manually: `mpm --install=package-name`

### ❌ "Ghostscript not found" (PNG only)

**Solution**: Install Ghostscript
- Download: https://www.ghostscript.com/
- Or update path in `latex_gui.py` line 25

### ❌ PDF has too much whitespace

Already optimized! But if you need tighter:
```python
# Edit line ~47 in latex_gui.py
border=0.5pt  # Reduce from 1pt to 0.5pt
```

### ❌ Compilation timeout (>30s)

For very complex equations, increase timeout:
```python
# Edit line ~80 in latex_gui.py
timeout=60  # Increase from 30 to 60 seconds
```

### ❌ \frac looks wrong

Use **Display mode** (`\[...\]`) instead of Inline mode for fractions!

## 🎨 Workflow: LaTeX → Affinity Designer

1. **Write equation** in LaTeX PDF Generator
2. Click **"Generate PDF"**
3. Click **"Show in Explorer"** (file will be highlighted)
4. **Drag PDF** from Explorer into Affinity Designer 2
5. PDF imports as perfect vector graphics!
6. Resize, recolor, export - no quality loss 🎉

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

Free to use, modify, distribute - even commercially!

## 🙏 Acknowledgments

- **MiKTeX** - Excellent LaTeX distribution for Windows
- **Ghostscript** - Reliable PDF/PNG conversion
- **Python Tkinter** - Simple yet powerful GUI framework
- Inspired by KLaTeX, designed for modern Windows + design workflows

## 📧 Support

Having issues?

1. Check [INSTALL_GUIDE.md](INSTALL_GUIDE.md) for detailed setup
2. See [Troubleshooting](#-troubleshooting) section above
3. Browse [Issues](../../issues) for similar problems
4. Open new [Issue](../../issues/new) with details

## 🌟 Star This Repo!

If this tool helped you, please star ⭐ the repository!

It helps others discover this project.

---

**Built with ❤️ for the LaTeX & Design community**

*Generate beautiful math equations for your design projects!*
