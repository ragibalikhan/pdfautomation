from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph


def generate_pdf(pdf_title, image_titles, image_paths, link_urls, image_dimensions, output_file):
    c = canvas.Canvas(output_file, pagesize=letter)

    c.setFont("Helvetica", 16)
    c.setFillColor(colors.HexColor("#ADD8E6"))
    c.drawString(50, 750, f"{pdf_title}")

    for i in range(len(image_paths)):
        image_path = image_paths[i]
        if image_path:
            # Get the image dimensions
            width, height = image_dimensions[i]

            # Adjust the image size to fit on the right side
            c.drawImage(image_path, 50, 600 - i * 200, width=width, height=height)

            # Calculate the positions for title, information, and link
            image_x = 50
            image_y = 600 - i * 200
            title_x = image_x + width + 20
            title_y = image_y + height / 2 + 20
            info_x = title_x
            info_y = title_y - 20
            link_x = info_x
            link_y = info_y - 20

            # Set the title color
            c.setFillColor(colors.HexColor("#ADD8E6"))

            # Draw the title
            c.setFont("Helvetica-Bold", 14)
            c.drawString(title_x, title_y, f"{image_titles[i]}")

            # Set the information style (bold)
            info_style = ParagraphStyle('info_style')
            info_style.fontName = 'Helvetica-Bold'
            info_style.fontSize = 12
            info_style.leading = 14

            user_input = input(f"Enter information about {image_titles[i]}: ")

            # Draw the information
            info = Paragraph(f"Information: {user_input}", info_style)
            info.wrap(300, 100)
            info.drawOn(c, info_x, info_y)

            if i < len(link_urls):
                link_url = link_urls[i]
                if link_url:
                    # Set the link style (underlined)
                    link_style = ParagraphStyle('link_style')
                    link_style.fontName = 'Helvetica'
                    link_style.fontSize = 12
                    link_style.leading = 14
                    link_style.textColor = colors.blue
                    link_style.underline = 1

                    # Draw the link
                    link = Paragraph(f"Link: <u>{link_url}</u>", link_style)
                    link.wrap(300, 100)
                    link.drawOn(c, link_x, link_y)

    c.save()


def get_user_input():
    pdf_title = input("Enter the PDF title: ")
    image_titles = []
    image_paths = []
    link_urls = []
    image_dimensions = []

    for i in range(3):
        image_title = input(f"Enter the title of image {i+1}: ")
        image_titles.append(image_title)

        image_path = input(f"Enter the path of image {i+1} (leave blank to skip): ")
        image_paths.append(image_path)

        link_url = input(f"Enter the URL for link {i+1} (leave blank to skip): ")
        link_urls.append(link_url)

        width = int(input(f"Enter the width of image {i+1} (in pixels): "))
        height = int(input(f"Enter the height of image {i+1} (in pixels): "))
        image_dimensions.append((width, height))

    output_file = input("Enter the output file name (e.g., output.pdf): ")
    return pdf_title, image_titles, image_paths, link_urls, image_dimensions, output_file


try:
    pdf_title, image_titles, image_paths, link_urls, image_dimensions, output_file = get_user_input()
    generate_pdf(pdf_title, image_titles, image_paths, link_urls, image_dimensions, output_file)
    print("PDF generation successful!")
except Exception as e:
    print("PDF generation failed:", str(e))