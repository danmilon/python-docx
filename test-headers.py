from docx import Document
import sys

d = Document(sys.argv[1])

d.sections[0].headers[0].add_paragraph(text='niaou!!')
d.save('/tmp/DAAMN.docx')
