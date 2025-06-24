import argparse
import os
import pandas as pd


def cargar_archivo(ruta):
    ext = os.path.splitext(ruta)[1].lower()
    if ext in {'.csv', '.txt'}:
        return pd.read_csv(ruta)
    if ext in {'.xlsx', '.xls'}:
        return pd.read_excel(ruta)
    if ext == '.json':
        return pd.read_json(ruta)
    raise ValueError(f'Tipo de archivo no soportado: {ruta}')


def main():
    parser = argparse.ArgumentParser(description='Convierte varios archivos de datos en un libro de Excel.')
    parser.add_argument('archivos', nargs='+', help='Rutas de archivos de entrada (csv, xlsx, json, txt)')
    parser.add_argument('-o', '--output', default='salida.xlsx', help='Nombre del archivo Excel de salida')
    args = parser.parse_args()

    with pd.ExcelWriter(args.output, engine='openpyxl') as writer:
        for archivo in args.archivos:
            df = cargar_archivo(archivo)
            hoja = os.path.splitext(os.path.basename(archivo))[0][:31]
            df.to_excel(writer, sheet_name=hoja, index=False)
    print(f'Se creó el archivo {args.output}')


if __name__ == '__main__':
    main()
