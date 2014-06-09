from docx import Document

d = Document('/tmp/zz.docx')

d.sections[0].headers[0].add_paragraph(text='niaou!!')
d.save('/tmp/DAAMN.docx')
