# encoding: utf-8

"""
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from ..opc.package import XmlPart
from ..shared import lazyproperty
from docx.blkcntnr import BlockItemContainer


class DiagramPart(XmlPart):
    """
    """

    @lazyproperty
    def data_model(self):
        """
        """
        return _DataModel(self._element, self)


class _DataModel(BlockItemContainer):
    def __init__(self, data_model_elm, parent):
        super(_DataModel, self).__init__(data_model_elm, parent)
