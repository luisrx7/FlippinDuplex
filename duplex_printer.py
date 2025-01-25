import os
import sys
from PyPDF2 import PdfReader, PdfWriter

def prepare_duplex_pdf(input_pdf_path, output_pdf_path=None):
    try:
        # Determine output base name
        if output_pdf_path is None:
            base_name = os.path.splitext(input_pdf_path)[0]
        else:
            base_name = os.path.splitext(output_pdf_path)[0]

        # Read the PDF
        reader = PdfReader(input_pdf_path)
        total_pages = len(reader.pages)

        # Separate pages into odd and even
        odd_writer = PdfWriter()
        even_writer = PdfWriter()

        # Store even pages in a list to reverse them later
        even_pages = []

        for i in range(total_pages):
            if i % 2 == 0:
                odd_writer.add_page(reader.pages[i])  # Odd page (0-indexed)
            else:
                even_pages.append(reader.pages[i])  # Even page (0-indexed)

        # Add even pages in reverse order
        for page in reversed(even_pages):
            even_writer.add_page(page)

        # Define output file names with order indications
        odd_output_path = f"{base_name}_1st_odd_pages.pdf"
        even_output_path = f"{base_name}_2nd_even_pages_reversed.pdf"

        # Save odd pages file
        with open(odd_output_path, "wb") as odd_out:
            odd_writer.write(odd_out)

        # Save even pages file (already reversed)
        with open(even_output_path, "wb") as even_out:
            even_writer.write(even_out)

        print(f"1st: Print odd pages -> {odd_output_path}")
        print(f"2nd: Print reversed even pages -> {even_output_path}")
        print("Print the 1st file first, flip the paper, and then print the 2nd file.")

    except Exception as e:
        print(f"Error processing the PDF: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python duplex_printer.py input.pdf [output.pdf]")
    else:
        input_pdf = sys.argv[1]
        output_pdf = sys.argv[2] if len(sys.argv) > 2 else None
        prepare_duplex_pdf(input_pdf, output_pdf)
