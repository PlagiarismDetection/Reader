import docx
import glob
from abc import ABC


class DOCX(ABC):
    def __init__(self, metadata, content):
        self.content_type = 'docx'
        self.title = metadata.title
        self.author = metadata.author
        self.creation_date = metadata.created
        self.content = content

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getContent(self):
        return self.content


class DOCXReader:
    @staticmethod
    def getDocxText(obj):
        docx_paras = obj.paragraphs
        full = []
        for para in docx_paras:
            full.append(para.text)
        return '\n'.join(full)

    @classmethod
    def getData(cls, folder):
        fileList = glob.glob('{}/*.docx'.format(folder))
        return (map(lambda filename: docx.Document(filename), fileList))

    @classmethod
    def getDOCXList(cls, folder):
        dataList = cls.getData(folder)
        docxList = []
        for data in dataList:
            pdf = DOCX(data.core_properties, cls.getDocxText(data))
            docxList.append(pdf)
        return docxList
