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

Todas las filas encontradas se combinan en un único archivo Excel. Este archivo
se genera al ejecutar el script y no se almacena en el repositorio para evitar
problemas con "binary files not supported" al crear el pull request.

Uso básico:

```bash
python extract_pdf_tables.py cot.872903.junio2025.pdf cot.872913.junio2025.pdf -o cotizaciones.xlsx
```

Para revisar los datos sin necesidad de un visor de Excel, puedes convertir el
archivo a formato CSV con `pandas`:

```bash
python - <<'PY'
import pandas as pd
pd.read_excel('cotizaciones.xlsx').to_csv('cotizaciones.csv', index=False)
PY
```

En este repositorio se incluye `cotizaciones.csv` ya generada a partir de los
PDF de ejemplo para que puedas consultar las primeras filas desde el diff.

## Licencia

MIT
