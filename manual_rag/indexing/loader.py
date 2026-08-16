import pymupdf

class Loader:
    def __init__(self):
        pass

    def pdf_loader(self, file_path):
        document = pymupdf.open(file_path)
        texts = [i.get_text() for i in document]
        return '\n '. join(texts)


