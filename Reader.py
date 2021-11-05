from abc import ABC
from Reader.DOCXReader import DOCXReader
from Reader.PDFReader import PDFReader


def readInputs(folder):
    pdf_data = PDFReader.getPDFList(folder)
    docx_data = DOCXReader.getDOCXList(folder)
    return pdf_data + docx_data


class FileObj(ABC):
    def __init__(self):
        pass

    def getType(self):
        pass

    def getTitle(self):
        pass

    def getAuthor(self):
        pass

    def getDate(self):
        pass

    def getContent(self):
        pass


class Reader(ABC):
    def __init__(self):
        pass
