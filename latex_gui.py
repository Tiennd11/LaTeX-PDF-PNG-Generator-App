"""
Lightweight LaTeX to PDF Generator
Generates vector PDFs and PNGs from LaTeX math equations
Perfect for importing into Affinity Designer 2 and other design tools
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import os
import sys
import tempfile
import subprocess
import shutil
from datetime import datetime
from pathlib import Path
import threading


class LatexPDFGenerator:
    """Handles LaTeX compilation to PDF using MiKTeX pdflatex"""
    
    PDFLATEX_PATH = r"C:\Users\An\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"
    GHOSTSCRIPT_PATH = r"C:\Program Files\gs\gs10.06.0\bin\gswin64c.exe"
    OUTPUT_DIR = Path.home() / "Desktop" / "latex_exports"
    
    def __init__(self):
        self.check_pdflatex()
        self.ensure_output_dir()
    
    def check_pdflatex(self):
        """Verify pdflatex is available"""
        if not os.path.exists(self.PDFLATEX_PATH):
            raise FileNotFoundError(
                f"pdflatex not found at:\n{self.PDFLATEX_PATH}\n\n"
                "Please install MiKTeX from: https://miktex.org/"
            )
    
    def ensure_output_dir(self):
        """Create output directory if it doesn't exist"""
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    def generate_pdf(self, latex_code: str, mode: str) -> tuple[str, bool, str]:
        """
        Generate PDF from LaTeX code
        
        Args:
            latex_code: The LaTeX math code
            mode: 'inline' for $...$ or 'display' for \[...\]
        
        Returns:
            Tuple of (pdf_path, success, message)
        """
        # Wrap the equation based on mode (user input already has correct backslashes)
        # Use displaystyle for tight bounding box
        if mode == "inline":
            wrapped_eq = "$\\displaystyle " + latex_code + "$"
        else:  # display
            wrapped_eq = "$\\displaystyle " + latex_code + "$"
        
        # Create LaTeX document with 10pt CMU Serif font
        # varwidth for tight horizontal cropping, border=1pt for minimal padding
        tex_content = ("\\documentclass[10pt,preview,border=1pt,varwidth]{standalone}\n"
                       "\\usepackage{amsmath,amssymb}\n"
                       "\\usepackage{lmodern}\n"  # Latin Modern (CMU) serif font
                       "\\begin{document}\n"
                       + wrapped_eq + "\n"
                       "\\end{document}\n")
        
        # Create temp directory
        temp_dir = tempfile.mkdtemp(prefix="latex_")
        
        try:
            # Write tex file
            tex_file = os.path.join(temp_dir, "document.tex")
            with open(tex_file, 'w') as f:
                f.write(tex_content)
            
            # Generate output filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_pdf = self.OUTPUT_DIR / f"equation_{timestamp}.pdf"
            
            # Run pdflatex
            result = subprocess.run(
                [
                    self.PDFLATEX_PATH,
                    "-interaction=nonstopmode",
                    "-output-directory", temp_dir,
                    "-job-name", "document",
                    tex_file
                ],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Check if PDF was generated
            temp_pdf = os.path.join(temp_dir, "document.pdf")
            if os.path.exists(temp_pdf):
                # Move PDF to output directory
                shutil.move(temp_pdf, str(output_pdf))
                return str(output_pdf), True, f"PDF generated successfully:\n{output_pdf.name}"
            else:
                # Extract last 30 lines of log for error display
                log_file = os.path.join(temp_dir, "document.log")
                error_msg = "PDF generation failed."
                
                if os.path.exists(log_file):
                    with open(log_file, 'r', errors='ignore') as f:
                        log_lines = f.readlines()
                    
                    # Get last 30 lines
                    relevant_lines = log_lines[-30:] if len(log_lines) > 30 else log_lines
                    error_msg += "\n\nLast 30 lines of pdflatex log:\n" + "".join(relevant_lines)
                else:
                    error_msg += "\n\nstdout:\n" + result.stdout
                    error_msg += "\n\nstderr:\n" + result.stderr
                
                return "", False, error_msg
        
        except subprocess.TimeoutExpired:
            return "", False, "Error: pdflatex compilation timed out (>30s)"
        except Exception as e:
            return "", False, f"Error: {str(e)}"
        finally:
            # Clean up temp directory
            try:
                shutil.rmtree(temp_dir, ignore_errors=True)
            except:
                pass
    
    def pdf_to_png(self, pdf_path: str, dpi: int = 600) -> tuple[str, bool, str]:
        """
        Convert PDF to PNG using Ghostscript
        
        Args:
            pdf_path: Path to the PDF file
            dpi: Resolution for PNG (default 600)
        
        Returns:
            Tuple of (png_path, success, message)
        """
        try:
            # Check if Ghostscript exists
            if not os.path.exists(self.GHOSTSCRIPT_PATH):
                return "", False, f"Ghostscript not found at:\n{self.GHOSTSCRIPT_PATH}\n\nPlease install Ghostscript from: https://ghostscript.com/"
            
            # Generate PNG filename (same as PDF but .png)
            png_path = pdf_path.replace(".pdf", ".png")
            
            # Run Ghostscript to convert PDF to PNG
            result = subprocess.run(
                [
                    self.GHOSTSCRIPT_PATH,
                    "-dSAFER",
                    "-dBATCH",
                    "-dNOPAUSE",
                    "-sDEVICE=pngalpha",  # Transparent background
                    f"-r{dpi}",
                    f"-sOutputFile={png_path}",
                    pdf_path
                ],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if os.path.exists(png_path):
                return png_path, True, f"PNG generated successfully:\n{Path(png_path).name}"
            else:
                return "", False, f"PNG generation failed.\n\nGhostscript output:\n{result.stdout}\n{result.stderr}"
        
        except subprocess.TimeoutExpired:
            return "", False, "Error: PNG conversion timed out (>30s)"
        except Exception as e:
            return "", False, f"Error: {str(e)}"


class LatexGUI:
    """Main GUI application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("LaTeX PDF Generator")
        self.root.geometry("900x850")
        self.root.resizable(True, True)
        
        # Initialize generator
        try:
            self.generator = LatexPDFGenerator()
            self.generator_ready = True
        except FileNotFoundError as e:
            self.generator_ready = False
            self.generator_error = str(e)
            messagebox.showerror("Initialization Error", str(e))
        
        self.current_pdf_path = None
        self.setup_ui()
    
    def setup_ui(self):
        """Create UI elements"""
        # Title
        title_frame = ttk.Frame(self.root)
        title_frame.pack(fill=tk.X, padx=10, pady=(10, 5))
        
        title_label = ttk.Label(
            title_frame,
            text="LaTeX Math Equation to PDF",
            font=("Arial", 12, "bold")
        )
        title_label.pack(side=tk.LEFT)
        
        # Mode selection
        mode_frame = ttk.LabelFrame(self.root, text="Display Mode", padding=10)
        mode_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.mode_var = tk.StringVar(value="display")
        
        ttk.Label(mode_frame, text="Equation Type:").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Radiobutton(
            mode_frame, text="Inline ($...$)", variable=self.mode_var, value="inline"
        ).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(
            mode_frame, text="Display (\\[...\\])", variable=self.mode_var, value="display"
        ).pack(side=tk.LEFT, padx=5)
        
        # LaTeX input
        input_frame = ttk.LabelFrame(self.root, text="LaTeX Code", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.latex_input = scrolledtext.ScrolledText(
            input_frame,
            height=18,
            width=110,
            wrap=tk.WORD,
            font=("Consolas", 10)
        )
        self.latex_input.pack(fill=tk.BOTH, expand=True)
        
        # Placeholder text (shorter example)
        self.latex_input.insert(tk.END, r"\frac{a}{b}")
        
        # Button frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Row 1: Generate buttons
        ttk.Button(
            button_frame,
            text="Generate PDF",
            command=self.generate_pdf
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Generate PNG",
            command=self.generate_png
        ).pack(side=tk.LEFT, padx=5)
        
        # DPI dropdown for PNG
        ttk.Label(button_frame, text="DPI:").pack(side=tk.LEFT, padx=(10, 5))
        self.dpi_var = tk.StringVar(value="600")
        dpi_combo = ttk.Combobox(
            button_frame,
            textvariable=self.dpi_var,
            values=["300", "600", "1200"],
            width=6,
            state="readonly"
        )
        dpi_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Open PDF",
            command=self.open_pdf,
            state=tk.DISABLED
        ).pack(side=tk.LEFT, padx=5)
        self.open_pdf_btn = button_frame.winfo_children()[-1]
        
        ttk.Button(
            button_frame,
            text="Show in Explorer",
            command=self.show_in_explorer,
            state=tk.DISABLED
        ).pack(side=tk.LEFT, padx=5)
        self.show_in_explorer_btn = button_frame.winfo_children()[-1]
        
        ttk.Button(
            button_frame,
            text="Open Output Folder",
            command=self.open_output_folder
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Copy Output Path",
            command=self.copy_output_path,
            state=tk.DISABLED
        ).pack(side=tk.LEFT, padx=5)
        self.copy_path_btn = button_frame.winfo_children()[-1]
        
        # Status area
        status_frame = ttk.LabelFrame(self.root, text="Status", padding=10)
        status_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        self.status_text = scrolledtext.ScrolledText(
            status_frame,
            height=8,
            width=80,
            wrap=tk.WORD,
            font=("Consolas", 9),
            state=tk.DISABLED
        )
        self.status_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for colors
        self.status_text.tag_config("success", foreground="green")
        self.status_text.tag_config("error", foreground="red")
        self.status_text.tag_config("info", foreground="blue")
    
    def log_status(self, message: str, tag: str = "info"):
        """Log a message to the status area"""
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, message + "\n", tag)
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)
    
    def clear_status(self):
        """Clear the status area"""
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.config(state=tk.DISABLED)
    
    def generate_pdf(self):
        """Generate PDF from LaTeX code"""
        if not self.generator_ready:
            self.clear_status()
            self.log_status(self.generator_error, "error")
            return
        
        latex_code = self.latex_input.get(1.0, tk.END).strip()
        
        if not latex_code:
            self.clear_status()
            self.log_status("Error: Please enter LaTeX code", "error")
            return
        
        mode = self.mode_var.get()
        
        # Disable button and show generating message
        self.root.config(cursor="wait")
        self.root.update()
        
        # Run in thread to prevent UI freezing
        def compile_thread():
            self.clear_status()
            self.log_status("Compiling...", "info")
            
            pdf_path, success, message = self.generator.generate_pdf(latex_code, mode)
            
            if success:
                self.current_pdf_path = pdf_path
                self.log_status(message, "success")
                self.open_pdf_btn.config(state=tk.NORMAL)
                self.show_in_explorer_btn.config(state=tk.NORMAL)
                self.copy_path_btn.config(state=tk.NORMAL)
            else:
                self.current_pdf_path = None
                self.open_pdf_btn.config(state=tk.DISABLED)
                self.show_in_explorer_btn.config(state=tk.DISABLED)
                self.copy_path_btn.config(state=tk.DISABLED)
                self.log_status(message, "error")
            
            self.root.config(cursor="")
        
        thread = threading.Thread(target=compile_thread, daemon=True)
        thread.start()
    
    def open_pdf(self):
        """Open the generated PDF"""
        if self.current_pdf_path and os.path.exists(self.current_pdf_path):
            os.startfile(self.current_pdf_path)
            self.log_status(f"Opened: {os.path.basename(self.current_pdf_path)}", "info")
        else:
            messagebox.showwarning("Warning", "No PDF generated yet. Generate a PDF first.")
    
    def open_output_folder(self):
        """Open the output folder in Explorer"""
        if self.generator_ready:
            os.startfile(str(self.generator.OUTPUT_DIR))
            self.log_status(f"Opened: {self.generator.OUTPUT_DIR}", "info")
    
    def show_in_explorer(self):
        """Open Explorer and select the current PDF file"""
        if self.current_pdf_path and os.path.exists(self.current_pdf_path):
            # Use /select parameter to highlight the file in Explorer
            subprocess.Popen(f'explorer /select,"{self.current_pdf_path}"')
            self.log_status(f"Selected in Explorer: {os.path.basename(self.current_pdf_path)}", "info")
        else:
            messagebox.showwarning("Warning", "No PDF generated yet. Generate a PDF first.")
    
    def copy_output_path(self):
        """Copy the current PDF path to clipboard"""
        if self.current_pdf_path:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.current_pdf_path)
            self.log_status(f"Copied to clipboard: {self.current_pdf_path}", "success")
        else:
            messagebox.showwarning("Warning", "No PDF path to copy.")
    
    def generate_png(self):
        """Generate PNG from LaTeX code (via PDF intermediate)"""
        if not self.generator_ready:
            self.clear_status()
            self.log_status(self.generator_error, "error")
            return
        
        latex_code = self.latex_input.get(1.0, tk.END).strip()
        
        if not latex_code:
            self.clear_status()
            self.log_status("Error: Please enter LaTeX code", "error")
            return
        
        mode = self.mode_var.get()
        dpi = int(self.dpi_var.get())
        
        # Disable button and show generating message
        self.root.config(cursor="wait")
        self.root.update()
        
        # Run in thread to prevent UI freezing
        def compile_thread():
            self.clear_status()
            self.log_status("Generating PDF...", "info")
            
            # First generate PDF
            pdf_path, success, message = self.generator.generate_pdf(latex_code, mode)
            
            if success:
                self.log_status("PDF OK. Converting to PNG...", "info")
                # Convert PDF to PNG
                png_path, png_success, png_message = self.generator.pdf_to_png(pdf_path, dpi)
                
                if png_success:
                    self.log_status(png_message, "success")
                else:
                    self.log_status(png_message, "error")
            else:
                self.log_status(message, "error")
            
            self.root.config(cursor="")
        
        thread = threading.Thread(target=compile_thread, daemon=True)
        thread.start()


def main():
    root = tk.Tk()
    app = LatexGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

