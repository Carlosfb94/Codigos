# Convertir archivos a Excel

Este repositorio contiene varios scripts de Python para transformar archivos en hojas de cálculo.

## Requisitos

- Python 3.8 o superior
- Las dependencias listadas en `requirements.txt`

Instale las dependencias con:

```bash
pip install -r requirements.txt
```

## Uso

Ejecute el script `convert_to_excel.py` indicando los archivos de entrada y el nombre del archivo Excel de salida:

```bash
python convert_to_excel.py archivo1.csv archivo2.json -o salida.xlsx
```

Cada archivo de entrada se guardará en una hoja diferente del libro `salida.xlsx`.

## Extraer tablas de cotizaciones desde PDF

El script `extract_pdf_tables.py` busca en uno o varios archivos PDF las tablas
que contengan exactamente los encabezados:

```
LINEA  CÓDIGO  PRODUCTO  CANTIDAD  PRECIO UNITARIO  TOTAL  VENCIMIENTO  EAN  LABORATORIO
```

Todas las filas encontradas se combinan en un único archivo Excel.

Uso básico:

```bash
python extract_pdf_tables.py cot.872903.junio2025.pdf cot.872913.junio2025.pdf -o cotizaciones.xlsx
```

El archivo `cotizaciones.xlsx` se creará en el directorio actual. Dado que las
extensiones de Excel están ignoradas mediante `.gitignore`, el archivo no se
sube al repositorio. Compártalo por otros medios si es necesario.

## Licencia

MIT
