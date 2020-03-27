import PyPDF2

#Creates watermark on top of a pdf file

template = PyPDF2.PdfFileReader(open("original.pdf", "rb"))
watermark = PyPDF2.PdfFileReader(open("watermark.pdf", "rb"))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))

	with open("watermark_output.pdf", "wb") as file:
		output.write(file)
