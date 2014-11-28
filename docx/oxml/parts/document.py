# encoding: utf-8

"""
Custom element classes that correspond to the document part, e.g.
<w:document>.
"""

from ..table import CT_Tbl
from ..xmlchemy import BaseOxmlElement, ZeroOrOne, ZeroOrMore
from docx.oxml.shared import qn


class CT_Document(BaseOxmlElement):
    """
    ``<w:document>`` element, the root element of a document.xml file.
    """
    body = ZeroOrOne('w:body')

    @property
    def sectPr_lst(self):
        """
        Return a list containing a reference to each ``<w:sectPr>`` element
        in the document, in the order encountered.
        """
        return self.xpath('.//w:sectPr')


class CT_Body(BaseOxmlElement):
    """
    ``<w:body>``, the container element for the main document story in
    ``document.xml``.
    """
    p = ZeroOrMore('w:p', successors=('w:sectPr',))
    tbl = ZeroOrMore('w:tbl', successors=('w:sectPr',))
    sectPr = ZeroOrOne('w:sectPr', successors=())

    def add_section_break(self):
        """
        Return the current ``<w:sectPr>`` element after adding a clone of it
        in a new ``<w:p>`` element appended to the block content elements.
        Note that the "current" ``<w:sectPr>`` will always be the sentinel
        sectPr in this case since we're always working at the end of the
        block content.
        """
        sentinel_sectPr = self.get_or_add_sectPr()
        cloned_sectPr = sentinel_sectPr.clone()
        p = self.add_p()
        p.set_sectPr(cloned_sectPr)
        return sentinel_sectPr

    def _new_tbl(self):
        return CT_Tbl.new()

    def clear_content(self):
        """
        Remove all content child elements from this <w:body> element. Leave
        the <w:sectPr> element if it is present.
        """
        if self.sectPr is not None:
            content_elms = self[:-1]
        else:
            content_elms = self[:]
        for content_elm in content_elms:
            self.remove(content_elm)

    @property
    def p_lst(self):
        """
        List of <w:p> child elements.
        """
        return self.findall(qn('w:p'))

    @property
    def tbl_lst(self):
        """
        List of <w:tbl> child elements.
        """
        return self.findall(qn('w:tbl'))

    def _append_blocklevelelt(self, block_level_elt):
        """
        Return *block_level_elt* after appending it to end of
        EG_BlockLevelElts sequence.
        """
        sentinel_sectPr = self._sentinel_sectPr
        if sentinel_sectPr is not None:
            sentinel_sectPr.addprevious(block_level_elt)
        else:
            self.append(block_level_elt)
        return block_level_elt

    @property
    def _sentinel_sectPr(self):
        """
        Return ``<w:sectPr>`` element appearing as last child, or None if not
        found. Note that the ``<w:sectPr>`` element can also occur earlier in
        the body; here we're only interested in one occuring as the last
        child.
        """
        if len(self) == 0:
            sentinel_sectPr = None
        elif self[-1].tag != qn('w:sectPr'):
            sentinel_sectPr = None
        else:
            sentinel_sectPr = self[-1]
        return sentinel_sectPr
