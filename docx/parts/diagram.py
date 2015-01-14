# encoding: utf-8

"""
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from lxml import etree
from ..opc.package import XmlPart
from ..oxml import parse_xml
from ..oxml.ns import qn, nsmap
from ..shared import lazyproperty
from docx.blkcntnr import BlockItemContainer


def new_root_with_ns(ns, short, root):
    # add new ns
    nsmap = root.nsmap
    nsmap[short] = ns
    new_root = etree.Element(root.tag, root.attrib, nsmap=nsmap)

    # copy rest
    new_root.tail = root.tail

    # copy all children
    new_root[:] = root[:]

    return new_root


class DiagramPart(XmlPart):
    """
    """

    convertable_tags = {qn('a:' + t): qn('w:' + t) for t in [
        'p', 'r', 't', 'pPr', 'br', 'cr', 'tab'
    ]}

    @classmethod
    def convert_to_wml(cls, root):
        for element in root:
            if element.tag in cls.convertable_tags:
                new_tag = cls.convertable_tags[element.tag]
                element.tag = new_tag

            cls.convert_to_wml(element)

    @classmethod
    def convert_to_dml(cls, root):
        for element in root:
            if element.tag in cls.convertable_tags.values():
                element.tag = qn('a:' + element.tag[element.tag.rindex('}') + 1])

            cls.convert_to_dml(element)

    def before_marshal(self):
        self.convert_to_dml(self._element)

    @classmethod
    def load(cls, partname, content_type, blob, package):
        str_blob = blob.decode()
        blob = str_blob.replace('<dgm:dataModel', '<dgm:dataModel xmlns:w="%s"' % nsmap['w'], count=1).encode()
        element = parse_xml(blob)
        cls.convert_to_wml(element)
        return cls(partname, content_type, element, package)

    @lazyproperty
    def data_model(self):
        """
        """
        return _DataModel(self._element, self)


class _DataModel(BlockItemContainer):
    def __init__(self, data_model_elm, parent):
        super(_DataModel, self).__init__(data_model_elm, parent)
