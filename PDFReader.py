from tika import parser
from abc import ABC
import glob


class PDF(ABC):
    def __init__(self, metadata, content):
        self.content_type = metadata['Content-Type'] if 'Content-Type' in metadata.keys() else ''
        self.title = metadata['resourceName'] if 'resourceName' in metadata.keys(
        ) else ''
        self.author = metadata['Author'] if 'Author' in metadata.keys() else ''
        self.creation_date = metadata['Creation-Date'] if 'Creation-Date' in metadata.keys() else ''
        self.page = metadata['xmpTPg:NPages'] if 'xmpTPg:NPages' in metadata.keys(
        ) else ''
        self.content = content

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getContent(self):
        return self.content


class PDFReader(Reader):
    @staticmethod
    def getData(folder):
        fileList = glob.glob('{}/*.pdf'.format(folder))
        return list(map(lambda file: parser.from_file(file), fileList))

    @classmethod
    def getPDFList(cls, folder):
        fileList = glob.glob('{}/*.pdf'.format(folder))
        dataList = cls.getData(folder)
        pdfList = []
        for data in dataList:
            pdf = PDF(data['metadata'], data['content'])
            pdfList.append(pdf)
        return pdfList

    @staticmethod
    def clean(lst):
        try:
            for pdf in lst:
                del pdf
        except:
            print('Type Error')
