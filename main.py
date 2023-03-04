from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

nome = str(input('Nome do arquivo: '))
cnv = canvas.Canvas(f"{nome}.pdf", pagesize=A4)
cnv.drawString(100, 100, 'Texto')
cnv.save()