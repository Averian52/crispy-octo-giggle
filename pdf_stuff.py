from pdfrw import PdfReader as PDFReader2, PdfWriter as PDFWriter2
from PyPDF2 import PdfReader, PdfWriter
import pikepdf
import tabula
import os

class PDF:
    def __init__(self, filepath, outputname):
        self.filepath = filepath
        self.outputname = filepath
        
    def pdf_read(self):
        return
        
    def page_split(self, parts):
        pages = PDFReader2(self.filepath).pages
        for part in parts:
            outdata = PDFWriter2(f'{self.outputname}pages{part[0]}_{part[1]}.pdf')
            for pagenum in range(*part):
                outdata.addpage(pages[pagenum-1])
            outdata.write()
    
    def remove_links(self):
        reader = PdfReader(self.filepath)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(self.outputname, "wb") as fh:
            writer.remove_links()
            writer.write(fh)
    
    def remove_images(self):
        reader = PdfReader(self.filepath)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.remove_images()
        with open(self.outputname, "wb") as f:
            writer.write(f)
    
    def lossless_compression(self):
        reader = PdfReader(self.filepath)
        writer = PdfWriter()
        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)
        with open(self.outputname, "wb") as f:
            writer.write(f)
    
    def other_compression(self):
        reader = PdfReader(self.filepath)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.add_metadata(reader.metadata)
        with open(self.outputname, "wb") as fp:
            writer.write(fp)
    
    def remove_security(self):
        pdf = pikepdf.open(self.filepath, allow_overwriting_input=True)
        pdf.save(self.filepath)
    
    def convert_to_csv(self):
        # convert PDF into CSV
        filename, file_extension = os.path.splitext(self.filepath)
        new_file_path = filename + ".csv"
        tabula.convert_into(self.filepath, new_file_path, output_format="csv", pages='all')
        return
    
    def filepath_change(self):
        self.outputname = os.path.dirname(self.filepath) + self.outputname
        
        
class PDFReader:
    def __init__(self, filepath, choice):
        self.filepath = filepath
        if choice == 1:
            self.pdfreader = PdfReader(filepath)
            self.pdfwriter = PdfWriter()
        elif choice == 2:
            self.pdfreader = PDFReader2(filepath)
            self.pdfwriter = PDFWriter2()
        elif choice == 3:
            self.pdfreader = pikepdf.open(filepath)
            self.pdfwriter = pikepdf.Pdf.new()   
        else:
            print("Invalid option")
            pass
        
                  

            
            
            
            