# encoding: utf-8

"""
"""

from docx.oxml.xmlchemy import BaseOxmlElement, ZeroOrMore, ZeroOrOne
from docx.oxml.ns import qn
from docx.oxml.text import CT_R as WORD_CT_R
from docx.oxml.text import _RunContentAppender
from docx.oxml.text import CT_P as WORD_CT_P


class CT_DataModel(BaseOxmlElement):
    """"""

    @property
    def p_lst(self):
        return self.xpath('.//w:p')


class CT_P(WORD_CT_P):
    """"""


class CT_R(BaseOxmlElement):
    """"""
