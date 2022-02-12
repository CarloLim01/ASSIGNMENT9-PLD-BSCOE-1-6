#PDF Resume Creator
	#Create a python program that will create your personal resume in PDF format
	#All personal details are stored in a JSON file
	#Your program should read the JSON file and write the details in the PDF
	#The output file should be: LASTNAME_FIRSTNAME.pdf

#Note:
	#Search for available PDF library that you can use
	#Search how data is structured using JSON format
	#Search how to read JSON file
	#You will create the JSON file manually
	#Your code should be in github before Feb12

from tokenize import Name
from fpdf import FPDF
import json

Name = "ALBERT CARLO P. LIM"
Address = "#392 Anonas Bacood Sta. Mesa Manila"
Contact = "+639527461283"
Email = "aclim123@gmail.com"

class PDF(FPDF):   
    def header(self):
        self.image("Picture.jpg",15, 15, 50, 0)
        
        self.set_font('Times', 'B', 30)
        w = self.get_string_width(Name) + 6
        self.set_x((255 - w) / 2)
        self.ln(7)
        self.cell(0, 20, f"{Name}" , align = 'R', ln=1)
        self.set_font('Times', 'B', 15)
        self.cell(0, 6, f"{Address}" , align = 'R', ln=1)
        self.cell(0, 6, f"{Contact}" , align = 'R', ln=1)
        self.cell(0, 6, f"{Email}" , align = 'R', ln=1)
        self.ln(10)

pdf = PDF('P', 'mm', "A4")

pdf.add_page()

fh = open('Resume.json', 'r') 
jh = fh.read()
info = json.loads(jh)

for information in info:
    pdf.ln(5)
    pdf.set_font('Times', 'BI', 18)
    pdf.cell(0, 10, f"{information['Header1']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['Objectives']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Objectives1']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Objectives2']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Objectives3']}", align='L', ln=1)
    pdf.ln(5)

    pdf.set_font('Times', 'BI', 18)
    pdf.cell(0, 10, f"{information['Header2']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 5, "    Tertiary             :  ", align='L')
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 5, f"{information['Tertiary']}", align='R', ln=1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['Tertiary Address']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['Tertiary Year']}", align='R', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 5, "    Secondary        :  ", align='L')
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 5, f"{information['Secondary']}", align='R', ln=1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['Secondary Address']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['Secondary Year']}", align='R', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 5, "    Primary             :  ", align='L')
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 5, f"{information['Primary']}", align='R', ln=1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['Primary Address']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['Primary Year']}", align='R', ln=1)
    pdf.ln(5)
