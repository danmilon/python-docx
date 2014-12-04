from docx import Document
from docx.oxml.ns import qn

d = Document('/home/danmilon/tmp/docs/smartart.docx')
dgm_relIds = d._document_part.body._element.xpath('.//dgm:relIds')
dgm_relIds = [element.get(qn('r:dm')) for element in dgm_relIds]
gdm_parts = [d._document_part.rels[rel_id].target_part for rel_id in dgm_relIds]


run_elm = gdm_parts[0].data_model.paragraphs[0].runs[0]._r
import pdb; pdb.set_trace()
run_elm.text = 'ff'
