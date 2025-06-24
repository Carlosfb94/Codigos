# Convertir archivos a Excel

Este repositorio contiene un script de Python que permite extraer datos de distintos archivos y agruparlos en un libro de Excel.

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

## Licencia

MIT
