# encoding: utf-8

"""
Custom element classes related to the header part
"""

from docx.oxml.shared import qn
from docx.oxml.xmlchemy import BaseOxmlElement, ZeroOrMore


class HeaderOrFooter(BaseOxmlElement):
    """"""

    p = ZeroOrMore('w:p', successors=('w:sectPr',))
    tbl = ZeroOrMore('w:tbl', successors=('w:sectPr',))

    @property
    def pPr(self):
        return self.find(qn('w:pPr'))


class CT_Footer(HeaderOrFooter):
    """"""


class CT_Header(HeaderOrFooter):
    """
    A ``<w:hdr>`` element, representing a header definition
    """
