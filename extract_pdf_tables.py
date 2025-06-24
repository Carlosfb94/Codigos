"""Extract specific tables from a list of PDF files into an Excel sheet.

This script looks for tables whose header matches the required columns and
exports all combined rows to an Excel file. Usage example:

    python extract_pdf_tables.py cot*.pdf -o cotizaciones.xlsx
"""

import argparse
import pdfplumber
import pandas as pd

HEADER = [
    "LINEA",
    "CÓDIGO",
    "PRODUCTO",
    "CANTIDAD",
    "PRECIO UNITARIO",
    "TOTAL",
    "VENCIMIENTO",
    "EAN",
    "LABORATORIO",
]


def process_pdfs(pdf_paths):
    rows = []
    for path in pdf_paths:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                for table in page.extract_tables() or []:
                    if not table:
                        continue
                    header = [
                        (cell or "").strip().upper()
                        for cell in table[0][: len(HEADER)]
                    ]
                    if header == HEADER:
                        for row in table[1:]:
                            cleaned = [
                                (cell or "").strip() for cell in row[: len(HEADER)]
                            ]
                            if any(cleaned):
                                rows.append(cleaned)
    return rows


def main():
    parser = argparse.ArgumentParser(
        description="Extrae tablas de cotizaciones de archivos PDF y las guarda en un Excel"
    )
    parser.add_argument("pdfs", nargs="+", help="Rutas de archivos PDF a procesar")
    parser.add_argument(
        "-o",
        "--output",
        default="cotizaciones.xlsx",
        help="Nombre del archivo Excel de salida",
    )
    args = parser.parse_args()

    data = process_pdfs(args.pdfs)
    df = pd.DataFrame(data, columns=HEADER)
    df.to_excel(args.output, index=False)
    print(f"Datos extraídos a {args.output}")


if __name__ == "__main__":
    main()
