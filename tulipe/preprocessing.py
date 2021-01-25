import os

from PyPDF2 import PdfFileReader


def parse(docpath):
    expandedpath = os.path.expanduser(docpath)
    __, doctype = os.path.splitext(expandedpath)
    parser = _get_parser(doctype)
    with open(expandedpath, 'rb') as doc:
        words = parser(doc)
        return words


def _get_parser(doctype):
    if doctype == '.pdf':
        return _pdf_parser
    else:
        raise ValueError(f'No parser for {doctype} files!')


def _pdf_parser(doc):
    pdf = PdfFileReader(doc)
    doc_content = [pdf.getPage(i).extractText() for i in range(pdf.numPages)]
    return '\n\n'.join(doc_content).split(' ')
