import os
from pdflatex import PDFLaTeX

def main():
    os.chdir("./_build/latex")
    pdfl = PDFLaTeX.from_texfile("AguaClaraTextbook.tex")
    pdf, log, _ = pdfl.create_pdf(keep_pdf_file=True)

if __name__ == "__main__":
    main()
