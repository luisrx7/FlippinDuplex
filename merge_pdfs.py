import os
from PyPDF2 import PdfReader, PdfWriter


def add_blank_page_if_needed(writer, num_pages):
    """
    Adds a blank page if the number of pages is odd to ensure consistency.
    """
    if num_pages % 2 != 0:
        writer.add_blank_page()


def merge_pdfs_with_blank_pages(input_folder, output_file):
    # Create output directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Update output path to be in output directory
    output_path = os.path.join(output_dir, output_file)

    writer = PdfWriter()
    pdf_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".pdf")])

    for i, pdf_file in enumerate(pdf_files):
        pdf_path = os.path.join(input_folder, pdf_file)
        reader = PdfReader(pdf_path)
        print(f"Adding {pdf_file} with {len(reader.pages)} pages")

        for page in reader.pages:
            writer.add_page(page)

        # Add blank page if needed for odd pages
        if len(reader.pages) % 2 != 0:
            print(f"Adding blank page after {pdf_file} (odd pages)")
            writer.add_blank_page()

    # Save the merged PDF
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Merged PDF saved as: {output_path} with {len(writer.pages)} total pages")


if __name__ == "__main__":
    input_folder = "input"
    output_file = "merged_output.pdf"
    merge_pdfs_with_blank_pages(input_folder, output_file)
