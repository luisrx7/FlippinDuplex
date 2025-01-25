import os
import sys
import tempfile
from PyPDF2 import PdfReader, PdfWriter
from merge_pdfs import merge_pdfs_with_blank_pages

def ensure_output_dir(output_dir):
    """Create output directory if it doesn't exist"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def process_directory(input_dir, output_dir):
    """Process all PDF files in the input directory"""
    ensure_output_dir(output_dir)
    processed = 0

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(input_dir, filename)
            output_base = os.path.join(output_dir, os.path.splitext(filename)[0])
            prepare_duplex_pdf(input_path, output_base)
            processed += 1

    print(f"Processed {processed} PDF files")

def process_directory_with_merge(input_dir, output_dir):
    """Merge PDFs in directory then process for duplex printing"""
    # Create temporary file for merged PDF
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
        temp_merged = tmp_file.name

    try:
        # Merge PDFs first
        merge_pdfs_with_blank_pages(input_dir, temp_merged)

        # Process the merged PDF
        output_base = os.path.join(output_dir, "merged")
        prepare_duplex_pdf(temp_merged, output_base)

    finally:
        # Clean up temp file
        if os.path.exists(temp_merged):
            os.unlink(temp_merged)

def prepare_duplex_pdf(input_pdf_path, output_pdf_path=None):
    try:
        # Determine output base name
        if output_pdf_path is None:
            base_name = os.path.splitext(input_pdf_path)[0]
        else:
            base_name = output_pdf_path

        # Read the PDF
        reader = PdfReader(input_pdf_path)
        total_pages = len(reader.pages)

        # Separate pages into even and odd
        even_writer = PdfWriter()
        odd_writer = PdfWriter()

        for i in range(total_pages):
            if i % 2 == 0:
                odd_writer.add_page(reader.pages[i])
            else:
                even_writer.add_page(reader.pages[i])

        # Define output file names with order indications
        even_output_path = f"{base_name}_1st_even_pages.pdf"
        odd_output_path = f"{base_name}_2nd_odd_pages.pdf"

        # Save even pages file first
        with open(even_output_path, "wb") as even_out:
            even_writer.write(even_out)

        # Save odd pages file
        with open(odd_output_path, "wb") as odd_out:
            odd_writer.write(odd_out)

        print(f"1st: Print even pages -> {even_output_path}")
        print(f"2nd: Print odd pages -> {odd_output_path}")
        print("Print the 1st file first, then flip the paper stack and print the 2nd file.")

    except Exception as e:
        print(f"Error processing the PDF: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python duplex_printer.py input.pdf|input_dir [output_dir] [--merge]")
        print("Options:")
        print("  --merge    Merge all PDFs in directory before processing")
        sys.exit(1)

    input_path = sys.argv[1]
    args = sys.argv[2:]

    # Parse optional arguments
    output_path = None
    merge_first = False

    for arg in args:
        if arg == '--merge':
            merge_first = True
        else:
            output_path = arg

    if os.path.isdir(input_path):
        output_dir = output_path or os.path.join(os.path.dirname(input_path), 'output')
        if merge_first:
            process_directory_with_merge(input_path, output_dir)
        else:
            process_directory(input_path, output_dir)
    else:
        prepare_duplex_pdf(input_path, output_path)
