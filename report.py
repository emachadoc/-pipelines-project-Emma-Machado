from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

ancho, alto=A4

c=canvas.Canvas("Report.pdf", pagesize=A4)

text=c.beginText(50, alto-50)

text.setFont('Times-Roman', 12)
 

text.textLine('Text Analytics')
text.textLine('')
text.textLine('From the tests it is deduced that Text Analytics works better predicting positive results')  # las dos frases aparecen en dos lineas diferentes
text.textLine('than negative ones, as the score turns very high if any "good" word is detected, although')
text.textLine('the review being negative.')

c.drawText(text)

c.showPage()                 
c.save()