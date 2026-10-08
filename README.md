# table-automation

Simple Python project to read a PDF file and extract text from it.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py your_file.pdf
```

This script uses `PyMuPDF` to read pages and `EasyOCR` as a fallback for scanned or image-based PDFs.

## Notes

- Best for text-based PDFs and scanned PDFs alike.
- EasyOCR downloads model files on first run, so the first execution may take a little longer.
