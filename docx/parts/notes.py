from ..opc.package import XmlPart
from docx.blkcntnr import BlockItemContainer


class NotesPart(XmlPart):
    """"""
    def get_note(self, note_id):
        """"""
        if not hasattr(self, '_notes_map'):
            self._notes_map = dict((n.id, n) for n in self.notes)
        return self._notes_map[note_id]

    @classmethod
    def new(cls):
        """"""
        raise NotImplementedError

    @property
    def notes(self):
        """"""
        return [Note(n, self) for n in self._element.notes_lst]


class Note(BlockItemContainer):
    """"""
    def __init__(self, note_elm, parent):
        super(Note, self).__init__(note_elm, parent)
        self._note_elm = note_elm
        self.id = note_elm.id
        self.type = note_elm.type
