# GitHub Setup Guide

Complete guide to publishing LaTeX PDF Generator on GitHub.

## Quick Summary

✅ **Ready to publish!**

Package created: `LaTeX-PDF-Generator-v1.0.zip` (10.16 MB)

Contains:
- LaTeX PDF Generator.exe (10.39 MB)
- README.md (GitHub homepage)
- INSTALL_GUIDE.md (detailed setup)
- EXAMPLES.md (50+ LaTeX samples)
- QUICKSTART.md (3-step guide)
- LICENSE (MIT)
- check_system.bat (system checker)

## Steps to Publish

### 1️⃣ Create GitHub Repository

Go to: https://github.com/new

Settings:
```
Repository name: latex-pdf-generator
Description: Lightweight Windows app for generating vector PDFs from LaTeX equations. Perfect for Affinity Designer 2 and other design tools.
✅ Public
❌ Add README (we have our own)
❌ Add .gitignore (we have our own)
❌ Add license (we have our own)
```

Click **"Create repository"**

### 2️⃣ Initialize Git (First Time)

```powershell
cd c:\Users\An\Documents\VS-codes\latex_gui_app

# Configure git (if first time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize repository
git init

# Add all files
git add .

# First commit
git commit -m "Initial release: LaTeX PDF Generator v1.0

Features:
- Generate vector PDFs from LaTeX equations
- Export high-resolution PNG (300/600/1200 DPI)
- Tight cropping with varwidth
- 10pt CMU Serif font (lmodern)
- Show in Explorer for easy drag-and-drop
- Comprehensive documentation
- 50+ LaTeX examples included"

# Add remote (replace 'yourusername' with your GitHub username)
git remote add origin https://github.com/yourusername/latex-pdf-generator.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3️⃣ Create GitHub Release

1. Go to your repository on GitHub
2. Click **"Releases"** (right sidebar)
3. Click **"Create a new release"**

Fill in:
```
Tag version: v1.0.0
Release title: LaTeX PDF Generator v1.0.0
```

Description (copy-paste):
```markdown
## 🎉 First Stable Release!

A lightweight Windows desktop application for generating vector PDFs and PNGs from LaTeX math equations.

### ✨ Features

- **Vector PDF Generation** - Crisp, scalable PDFs perfect for design work
- **PNG Export** - High-resolution images at 300/600/1200 DPI
- **Tight Cropping** - Minimal whitespace with automatic trimming
- **CMU Serif Font** - Professional 10pt Computer Modern typography
- **Quick Access** - "Show in Explorer" button for easy drag-and-drop
- **Error Handling** - Clear messages with pdflatex log excerpts
- **Lightweight** - Only ~10MB standalone executable

### 📋 Requirements

- Windows 10/11 (64-bit)
- MiKTeX (free download: https://miktex.org/)
- Ghostscript (optional, for PNG export: https://www.ghostscript.com/)

### 🚀 Quick Start

1. **Download** `LaTeX-PDF-Generator-v1.0.zip` below
2. **Extract** to any folder
3. **Install MiKTeX** from https://miktex.org/download
4. **Double-click** `LaTeX PDF Generator.exe`
5. **Enter** your LaTeX equation
6. **Click** "Generate PDF"
7. **Done!** PDF saved to `Desktop\latex_exports\`

### 📚 Documentation

- **README.md** - Main documentation
- **INSTALL_GUIDE.md** - Detailed installation guide
- **QUICKSTART.md** - 3-step quick start
- **EXAMPLES.md** - 50+ LaTeX equation examples
- **check_system.bat** - System requirements checker

### 🎯 Perfect For

- Affinity Designer 2 users
- Adobe Illustrator workflows
- Graphic designers needing math equations
- LaTeX users wanting vector graphics
- Academic publications and presentations

### 🐛 Known Issues

None! This is a stable release.

### 📝 Notes

- First run may prompt to install LaTeX packages - just click "Install"
- PNG generation requires Ghostscript (optional)
- Output folder created automatically on Desktop

### 🔗 Links

- [Installation Guide](INSTALL_GUIDE.md)
- [LaTeX Examples](EXAMPLES.md)
- [Report Issues](../../issues)
- [MiKTeX Download](https://miktex.org/download)
- [Ghostscript Download](https://www.ghostscript.com/releases/gsdnld.html)

---

**Download the ZIP file below to get started!** ⬇️
```

4. **Upload file**: Drag `LaTeX-PDF-Generator-v1.0.zip` to upload area
5. Click **"Publish release"**

### 4️⃣ Update Repository Description

On your repo homepage:
1. Click **⚙️ (Settings icon)** near "About"
2. Add:
   - Description: `Lightweight Windows app for generating vector PDFs from LaTeX equations. Perfect for Affinity Designer and graphic design workflows.`
   - Website: (leave empty or add your site)
   - Topics: `latex`, `pdf`, `windows`, `gui`, `affinity-designer`, `design-tools`, `math-equations`, `vector-graphics`, `tkinter`, `python`
   - ✅ Releases
3. **Save changes**

## Alternative: Upload via Git GUI

If command line is difficult, use **GitHub Desktop**:

1. Download: https://desktop.github.com/
2. Install and sign in
3. File → Add Local Repository → Select `latex_gui_app` folder
4. Click "Publish repository"
5. Fill in name and description
6. Click "Publish"

Then follow step 3️⃣ above to create release.

## Files Already Prepared ✅

```
✅ README.md              - GitHub main page
✅ LICENSE                - MIT license
✅ .gitignore             - Ignore build artifacts
✅ INSTALL_GUIDE.md       - Detailed setup
✅ EXAMPLES.md            - 50+ equations
✅ QUICKSTART.md          - Quick start
✅ latex_gui.py           - Source code (clean)
✅ build.bat              - Build script
✅ run.bat                - Run script
✅ check_system.bat       - System check
✅ dist/LaTeX PDF Generator.exe - Executable
✅ LaTeX-PDF-Generator-v1.0.zip - Release package
```

## Post-Publication Checklist

After publishing:

- [ ] Test download link works
- [ ] Verify ZIP extracts correctly
- [ ] Check README renders properly on GitHub
- [ ] Add topics/tags to repository
- [ ] Share on social media (optional)
- [ ] Monitor for issues/questions

## Sharing Your Release

Once published, share on:

### Reddit
- r/LaTeX - "Made a lightweight LaTeX PDF generator for Windows"
- r/AffinityDesigner - "Tool for importing LaTeX equations into Affinity Designer 2"
- r/software - "LaTeX PDF Generator - Free Windows app"

### Twitter/X
```
🚀 Just released LaTeX PDF Generator v1.0!

✨ Generate vector PDFs from LaTeX equations
🎨 Perfect for Affinity Designer & design work
💻 Free & open source (MIT)
📦 Only ~10MB

Download: [your-github-link]

#LaTeX #Windows #OpenSource #GraphicDesign
```

## Need Help?

Issues with Git/GitHub?
1. Check: https://docs.github.com/en/get-started
2. Try GitHub Desktop: https://desktop.github.com/
3. Ask on: https://stackoverflow.com/

---

**🎉 Congratulations! Your project is ready for the world!**
