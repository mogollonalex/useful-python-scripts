# Debemos instalar las siguientes librerías
# pip install fpdf

from email.mime import image
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image("miqr.png",x=10,y=10,w=40)
pdf.output("miqr.pdf", "F")
