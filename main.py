from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from PIL import Image

def create_invoice_pdf(pdf_path, logo_path, signature_path):
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    # Draw logo
    logo = Image.open(logo_path)
    logo_width, logo_height = logo.size
    logo_aspect = logo_height / float(logo_width)
    c.drawImage(logo_path, x=0.5 * inch, y=height - 1.5 * inch, width=1.5 * inch, height=1.5 * inch * logo_aspect, mask='auto')

    # Draw invoice text
    c.setFont("Helvetica-Bold", 12)
    c.drawString(3 * inch, height - 1 * inch, "Tax Invoice/Bill of Supply/Cash Memo")
    c.setFont("Helvetica", 10)
    c.drawString(3 * inch, height - 1.2 * inch, "(Original for Recipient)")

    # Seller information
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.5 * inch, height - 2 * inch, "Sold By :")
    c.setFont("Helvetica", 10)
    c.drawString(0.5 * inch, height - 2.2 * inch, "VM Silk Exports")
    c.drawString(0.5 * inch, height - 2.4 * inch, " 75, 3rd Cross, Lalbagh Road")
    c.drawString(0.5 * inch, height - 2.6 * inch, "BENGALURU, KARNATAKA, 560027")
    c.drawString(0.5 * inch, height - 2.8 * inch, "IN")
    c.drawString(0.5 * inch, height - 3 * inch, "PAN No: AACFV3325K")
    c.drawString(0.5 * inch, height - 3.2 * inch, "GST Registration No: 29AACFV3325K1ZY")

    # Billing and Shipping Address
    c.setFont("Helvetica-Bold", 10)
    c.drawString(3.5 * inch, height - 2 * inch, "Billing Address :")
    c.setFont("Helvetica", 10)
    c.drawString(3.5 * inch, height - 2.2 * inch, "Chandra Lekha")
    c.drawString(3.5 * inch, height - 2.4 * inch, "Celominds IT Solutions India Pvt Ltd.")
    c.drawString(3.5 * inch, height - 2.6 * inch, "1st Floor, Maruti Platinum")
    c.drawString(3.5 * inch, height - 2.8 * inch, "KS Layout")
    c.drawString(3.5 * inch, height - 3 * inch, "BENGALURU, KARNATAKA, 560078")
    c.drawString(3.5 * inch, height - 3.2 * inch, "IN")
    c.drawString(3.5 * inch, height - 3.4 * inch, "State/UT Code: 29")

    c.setFont("Helvetica-Bold", 10)
    c.drawString(3.5 * inch, height - 3.8 * inch, "Shipping Address :")
    c.setFont("Helvetica", 10)
    c.drawString(3.5 * inch, height - 4 * inch, "Chandra Lekha")
    c.drawString(3.5 * inch, height - 4.2 * inch, "Celominds IT Solutions India Pvt Ltd.")
    c.drawString(3.5 * inch, height - 4.4 * inch, "1st Floor, Maruti Platinum")
    c.drawString(3.5 * inch, height - 4.6 * inch, "KS Layout")
    c.drawString(3.5 * inch, height - 4.8 * inch, "BENGALURU, KARNATAKA, 560078")
    c.drawString(3.5 * inch, height - 5 * inch, "IN")
    c.drawString(3.5 * inch, height - 5.2 * inch, "State/UT Code: 29")

    # Order Information
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.5 * inch, height - 5.5 * inch, "Order Number: 403-3225714-7676307")
    c.drawString(0.5 * inch, height - 5.7 * inch, "Order Date: 25.06.2024")

    # Table Data
    data = [
        ["Sl. No", "Description", "Unit Price", "Qty", "Net Amount", "Tax Rate", "Tax Type", "Tax Amount", "Total Amount"],
        ["1", "VM Silks Men's Shirt", "Rs.338.10", "1", "Rs.338.10", "2.5%", "CGST", "Rs.13.45", "Rs.365.00"],
        ["", "", "", "", "", "2.5%", "SGST", "Rs.13.45", ""],
        ["", "Shipping Charges", "Rs.30.96", "", "Rs.30.96", "2.5%", "CGST", "Rs.0.77", "Rs.32.50"],
        ["", "", "", "", "", "2.5%", "SGST", "Rs.0.77", ""],
        ["2", "VM Men's Shirt", "Rs.338.10", "1", "Rs.338.10", "2.5%", "CGST", "Rs.13.45", "Rs.365.00"],
        ["", "", "", "", "", "2.5%", "SGST", "Rs.13.45", ""],
        ["", "Shipping Charges", "Rs.30.96", "", "Rs.30.96", "2.5%", "CGST", "Rs.0.77", "Rs.32.50"],
        ["", "", "", "", "", "2.5%", "SGST", "Rs.0.77", ""],
        ["", "", "", "", "", "", "", "Total", "Rs.1,195.00"]
    ]

    table = Table(data, colWidths=[0.5 * inch, 1.5 * inch, 0.7 * inch, 0.5 * inch, 1.0 * inch, 0.7 * inch, 0.7 * inch,1.0 * inch, 1.0 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    table.wrapOn(c, width, height)
    table.drawOn(c, 0.3 * inch, height - 8 * inch)

    # Amount in Words
    c.setFont("Helvetica", 10)
    c.drawString(0.5 * inch, height - 8.5 * inch, "Amount in Words:")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1.8 * inch, height - 8.5 * inch, "One Thousand One Hundred And Ninety-five only")

    # Authorized Signature
    c.setFont("Helvetica", 10)
    c.drawString(5.7 * inch, height - 10.2 * inch, "For VM Silk Exports:")
    c.drawString(5.7 * inch, height - 10.4 * inch, "Authorized Signatory")

    # Draw signature
    signature = Image.open(signature_path)
    signature_width, signature_height = signature.size
    signature_aspect = signature_height / float(signature_width)
    c.drawImage(signature_path, x=5.3 * inch, y=height - 10 * inch, width=2 * inch, height=2 * inch * signature_aspect, mask='auto')

    c.save()

# File paths
pdf_path = "C:/Users/NISHA/Desktop/Aurika_Tech/invoice.pdf"
logo_path = "C:/Users/NISHA/Desktop/Aurika_Tech/download.png"
signature_path = "C:/Users/NISHA/Desktop/Aurika_Tech/download.jpeg"

create_invoice_pdf(pdf_path, logo_path, signature_path)