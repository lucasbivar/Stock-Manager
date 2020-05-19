def generate_coupon(text_lines, final_lines, client, print=False):
    from datetime import datetime
    dt = datetime.now()
    date = dt.strftime('%H:%M  %d/%m/%Y')
    date_for_file = dt.strftime('%d-%m-%Y')
    footer = 'Thank you and welcome back!'
    fileName = rf'coupons\Purchase-{client}-{date_for_file}.pdf'
    documentTitle = f'Purchase-{client}-{date_for_file}'
    title = 'Stock Manager'
    subTitle = 'Non-tax coupon'

    from reportlab.pdfgen import canvas
    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)
    pdf.drawCentredString(300, 770, title)
    pdf.drawCentredString(300, 745, date)
    pdf.drawCentredString(300, 720, subTitle)
    pdf.line(30, 710, 550, 710)
    from reportlab.lib import colors
    text = pdf.beginText(40, 680)
    text.setFillColor(colors.black)
    line_x = 690
    for line in text_lines:
        pdf.drawString(100, line_x, line[0])
        pdf.drawString(150, line_x, line[1])
        pdf.drawString(275, line_x, line[2])
        pdf.drawString(350, line_x, line[3])
        pdf.drawString(430, line_x, line[4])
        line_x -= 15
    pdf.line(30, line_x, 550, line_x)
    line_x -= 15
    for line in final_lines:
        pdf.drawString(100, line_x, line[0])
        pdf.drawString(215, line_x, line[1])
        pdf.drawString(280, line_x, line[2])
        pdf.drawString(350, line_x, line[3])
        pdf.drawString(430, line_x, line[4])
        line_x -= 15
    pdf.line(30, line_x, 550, line_x)
    line_x -= 15
    pdf.drawCentredString(300, line_x, footer)
    pdf.save()
    if print:
        return fileName
