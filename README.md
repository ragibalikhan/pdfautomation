# PDF Automation Project

This project allows you to generate a PDF document with images, titles, information, and optional links. It uses the `reportlab` library for PDF generation.

## Prerequisites

Before running this project, make sure you have the following:

- Python 3.x installed
- `reportlab` library installed (`pip install reportlab`)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/pdfautomation.git
   
2. Change to the project directory:
    ```shell
    cd pdfautomation
    
3. Install the dependencies:
    ```shell 
    pip install -r requirements.txt

##Usage

1. Import the required modules:
    ```shell
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import Paragraph
    
2. Define the generate_pdf function to generate the PDF:
   ```shell
    def generate_pdf(pdf_title, image_titles, image_paths, link_urls, image_dimensions, output_file):
        # ...
3. Implement the logic for generating the PDF inside the generate_pdf function.

4. Define the get_user_input function to get user input:

    ```shell
    def get_user_input():
        # ...
        
5. Implement the logic for getting user input inside the get_user_input function.

6. Wrap the PDF generation logic inside a try-except block to handle exceptions:

    ```shell
    try:
        pdf_title, image_titles, image_paths, link_urls, image_dimensions, output_file = get_user_input()
        generate_pdf(pdf_title, image_titles, image_paths, link_urls, image_dimensions, output_file)
        print("PDF generation successful!")
    except Exception as e:
        print("PDF generation failed:", str(e))
        
7. Run the script:
    ```shell
    python pdf_automation.py
8. Follow the prompts and provide the necessary information.

9. Once the execution completes, the generated PDF will be saved in the specified output file.


## Customization

You can customize the appearance and layout of the PDF by modifying the code inside the generate_pdf function.

The setFont function can be used to set the font and size for text elements.
The setFillColor function sets the fill color for shapes and text.
Adjust the positioning and layout of the elements based on your requirements.

## License

This project is licensed under the [MIT License](LICENSE).
