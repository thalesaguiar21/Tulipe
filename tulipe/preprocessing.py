import os

from pdfminer.high_level import extract_text


def parse(docpath):
    expandedpath = os.path.expanduser(docpath)
    __, doctype = os.path.splitext(expandedpath)
    parser = _get_parser(doctype)
    words = parser(expandedpath)
    return words


def _get_parser(doctype):
    if doctype == '.pdf':
        return _pdf_parser
    else:
        raise ValueError(f'No parser for {doctype} files!')


def _pdf_parser(docpath):
    return extract_text(docpath)
