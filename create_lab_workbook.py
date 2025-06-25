import pandas as pd

EXCEL_INPUT = 'SKU - Producto - Precio .xlsx'
CSV_LABS = 'cotizaciones.csv'
OUTPUT = 'productos_por_laboratorio.xlsx'

# Cargar el archivo con SKU, producto y precio
base = pd.read_excel(EXCEL_INPUT)
base.columns = ['SKU', 'PRODUCTO', 'PRECIO UNITARIO']

# Cargar archivo con los laboratorios
labs_df = pd.read_csv(CSV_LABS)

# Mapear laboratorio por SKU y luego por nombre de producto
map_by_sku = labs_df.drop_duplicates('CÓDIGO').set_index('CÓDIGO')['LABORATORIO']
map_by_product = (
    labs_df.dropna(subset=['LABORATORIO'])
    .drop_duplicates('PRODUCTO')
    .set_index('PRODUCTO')['LABORATORIO']
)

base['LABORATORIO'] = base['SKU'].map(map_by_sku)
base['LABORATORIO'] = base['LABORATORIO'].fillna(base['PRODUCTO'].map(map_by_product))

# Crear tablas dinámicas para SKU y precios
sku_pivot = base.pivot_table(
    index='PRODUCTO', columns='LABORATORIO', values='SKU', aggfunc='first'
)
precio_pivot = base.pivot_table(
    index='PRODUCTO', columns='LABORATORIO', values='PRECIO UNITARIO', aggfunc='first'
)

with pd.ExcelWriter(OUTPUT, engine='openpyxl') as writer:
    # Hoja con SKU por laboratorio
    sku_pivot.to_excel(writer, sheet_name='SKUs por Lab')
    # Hoja con precios por laboratorio
    precio_pivot.to_excel(writer, sheet_name='Precios por Lab')
    # Una hoja por laboratorio con productos de ese laboratorio
    for lab, group in base.dropna(subset=['LABORATORIO']).groupby('LABORATORIO'):
        group[['PRODUCTO', 'SKU', 'PRECIO UNITARIO']].to_excel(
            writer, sheet_name=lab[:31], index=False
        )

print(f'Se creó {OUTPUT}')
