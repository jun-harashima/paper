import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from pott.files.file import File


class Pdf(File):

    DIR_NAME = os.environ['HOME'] + '/.pott/pdf'

    def __init__(self, file_name):
        self.set_file_name(file_name)

    def dir_name(self):
        return self.DIR_NAME

    def save(self, content):
        with open(self.DIR_NAME + '/' + self.file_name, 'wb') as file:
            file.write(content)

    def extract_text(self):
        with open(self.DIR_NAME + '/' + self.file_name, 'rb') as file:
            manager = PDFResourceManager()
            stringio = StringIO()
            laparams = LAParams()
            device = TextConverter(manager, stringio, codec='utf-8',
                                   laparams=laparams)
            interpreter = PDFPageInterpreter(manager, device)
            for page in PDFPage.get_pages(file):
                interpreter.process_page(page)
            return stringio.getvalue()