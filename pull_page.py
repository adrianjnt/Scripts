import os
from PyPDF2 import PdfReader, PdfWriter

def extract_pdf_pages(input_pdf_path, output_directory):
    try:
        # Open the original PDF
        with open(input_pdf_path, "rb") as pdf_file:
            reader = PdfReader(pdf_file)
            total_pages = len(reader.pages)

            # Loop through all pages in the PDF
            for page_number in range(total_pages):
                # Create a PDF writer object
                writer = PdfWriter()

                # Add the specific page to the writer
                writer.add_page(reader.pages[page_number])

                # Create the output file name for each page
                output_pdf = os.path.join(output_directory, f"Page_{page_number + 1}.pdf")

                # Write the new PDF with the selected page
                with open(output_pdf, "wb") as output_file:
                    writer.write(output_file)

            print(f"All {total_pages} pages extracted successfully and saved in {output_directory}.")
    
    except FileNotFoundError:
        print(f"Error: File {input_pdf_path} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Ask user for the directory to save the extracted pages
    output_directory = input("Enter the directory to save the extracted pages: ")

    # Ensure the output directory exists, if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Ask user for the input PDF file name (with directory)
    input_pdf = input("Enter the full path to the input PDF file (including file name): ")

    # Call the function to extract each page and save as individual PDFs
    extract_pdf_pages(input_pdf, output_directory)


