import pymupdf as fitz


def merge_pdf(input_paths, output_path):
    if not input_paths:
        raise ValueError("No input PDF files provided.")

    merged_pdf = fitz.open()

    try:
        for input_path in input_paths:
            with fitz.open(input_path) as pdf:
                merged_pdf.insert_pdf(pdf)

        merged_pdf.save(output_path)
    finally:
        merged_pdf.close()


def read_pdf(pdf_path):
    text = []

    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text.append(page.get_text("text"))

    return "\n\n".join(text)