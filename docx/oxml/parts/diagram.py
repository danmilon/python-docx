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
        return self.xpath('.//a:p')


class CT_P(WORD_CT_P):
    """"""

    pPr = ZeroOrOne('a:pPr')
    r = ZeroOrMore('a:r')


class CT_R(BaseOxmlElement):
    """"""

    rPr = ZeroOrOne('a:rPr')
    t = ZeroOrMore('a:t')
    br = ZeroOrMore('a:br')
    cr = ZeroOrMore('a:cr')
    tab = ZeroOrMore('a:tab')

    @property
    def text(self):
        text = ''
        for child in self:
            if child.tag == qn('a:t'):
                t_text = child.text
                text += t_text if t_text is not None else ''
            elif child.tag == qn('a:tab'):
                text += '\t'
            elif child.tag in (qn('a:br'), qn('a:cr')):
                text += '\n'
        return text

    @text.setter
    def text(self, text):
        self.clear_content()
        _RunContentAppender.append_to_run_from_text(self, text)

    def clear_content(self):
        for elm in self.xpath('./w:t'):
            elm.getparent().remove(elm)
