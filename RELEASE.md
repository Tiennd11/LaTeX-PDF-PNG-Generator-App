# Release Preparation Guide

This guide helps prepare the LaTeX PDF Generator for GitHub release.

## Pre-Release Checklist

### 1. Code Quality
- [x] Remove all debug code
- [x] Remove OCR features (too heavy)
- [x] Update version info
- [x] Test all features work

### 2. Documentation
- [x] README.md (GitHub main page)
- [x] INSTALL_GUIDE.md (detailed setup)
- [x] EXAMPLES.md (50+ LaTeX examples)
- [x] QUICKSTART.md (3-step guide)
- [x] LICENSE (MIT)

### 3. Build Files
- [x] Clean build directory
- [x] Rebuild executable
- [x] Test .exe on clean Windows machine
- [x] Verify file size (~10MB)

### 4. Git Files
- [x] .gitignore (Python, build artifacts)
- [ ] Create GitHub repository
- [ ] Initial commit
- [ ] Add release tag

## Creating GitHub Release

### Step 1: Create Repository

```bash
# On GitHub, create new repository:
# Name: latex-pdf-generator
# Description: Lightweight Windows app for generating vector PDFs from LaTeX equations
# Public repository
# Initialize with: Nothing (we have our own files)
```

### Step 2: Push Code

```bash
cd c:\Users\An\Documents\VS-codes\latex_gui_app

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "Initial release: LaTeX PDF Generator v1.0"

# Add remote
git remote add origin https://github.com/yourusername/latex-pdf-generator.git

# Push
git push -u origin main
```

### Step 3: Create Release Package

Files to include in release ZIP:
```
LaTeX-PDF-Generator-v1.0/
├── LaTeX PDF Generator.exe    # Main executable
├── README.md                   # Quick start
├── INSTALL_GUIDE.md           # Detailed setup
├── EXAMPLES.md                # LaTeX examples
├── QUICKSTART.md              # 3-step guide
├── LICENSE                    # MIT license
└── check_system.bat           # System checker
```

### Step 4: Create ZIP

```powershell
# Create release directory
New-Item -ItemType Directory -Force -Path ".\release"

# Copy files
Copy-Item "dist\LaTeX PDF Generator.exe" ".\release\"
Copy-Item "README.md" ".\release\"
Copy-Item "INSTALL_GUIDE.md" ".\release\"
Copy-Item "EXAMPLES.md" ".\release\"
Copy-Item "QUICKSTART.md" ".\release\"
Copy-Item "LICENSE" ".\release\"
Copy-Item "check_system.bat" ".\release\"

# Create ZIP
Compress-Archive -Path ".\release\*" -DestinationPath "LaTeX-PDF-Generator-v1.0.zip"
```

### Step 5: GitHub Release

1. Go to GitHub repository
2. Click "Releases" → "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `LaTeX PDF Generator v1.0.0`
5. Description:
```markdown
## LaTeX PDF Generator v1.0.0

First stable release! 🎉

### Features
- Generate vector PDFs from LaTeX equations
- Export high-resolution PNG (300/600/1200 DPI)
- Tight cropping with varwidth
- 10pt CMU Serif font (lmodern)
- Show in Explorer for easy drag-and-drop
- ~10MB standalone executable

### Requirements
- Windows 10/11 (64-bit)
- MiKTeX (free download)
- Ghostscript (optional, for PNG)

### Download
- **LaTeX-PDF-Generator-v1.0.zip** (recommended)
- Source code available below

### Installation
1. Download and extract ZIP
2. Install MiKTeX from https://miktex.org/
3. Double-click "LaTeX PDF Generator.exe"
4. Done! 🚀

See INSTALL_GUIDE.md for detailed setup instructions.
```

6. Upload `LaTeX-PDF-Generator-v1.0.zip`
7. Click "Publish release"

## Post-Release

### Update README.md

Add badges:
```markdown
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
```

### Share

- Reddit: r/LaTeX, r/math
- Twitter/X with hashtags: #LaTeX #Windows #OpenSource
- Hacker News (if it gains traction)

### Monitor

- Watch for issues
- Respond to user questions
- Plan v1.1 features based on feedback

## Version History

### v1.0.0 (2026-01-28)
- Initial release
- PDF/PNG generation
- Tight cropping
- CMU Serif font
- Show in Explorer
- Error handling
- 50+ examples included
