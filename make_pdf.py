from pdflatex import PDFLaTeX


def main():
    os.chdir("./build/sphinx/latex")
    pdfl = PDFLaTeX.from_texfile("AideDesignSpecs.tex")
    pdf, log, _ = pdfl.create_pdf(keep_pdf_file=True)
