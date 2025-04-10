import pandas as pd
import geopandas as gpd

def limpiar_y_convertir(input_csv, output_excel):
    """
    Función para limpiar un archivo CSV y convertirlo a Excel con reemplazos específicos.
    
    Args:
        input_csv (str): Ruta del archivo CSV de entrada
        output_excel (str): Ruta del archivo Excel de salida
    """
    
    # Leer el archivo CSV
    try:
        # Usamos engine='python' para manejar formatos no estándar
        df = pd.read_csv(input_csv, delimiter=',', engine='python')
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return
    
    # Reemplazar '.' por ' ' en la columna Direccion
    df['Direccion'] = df['Direccion'].str.replace('.', ' ').str.replace(r'([a-zA-Z])(\d)', r'\1 \2', regex=True).str.replace(r'(\d)([a-zA-Z])', r'\1 \2', regex=True).replace(r'\s+', ' ', regex=True).str.strip()

    
    # Reemplazar '.' por ' ' en la columna Comuna
    df['Comuna'] = df['Comuna'].replace(r'\s+', ' ', regex=True).str.strip()
    
    # Reemplazar '.' por ',' en las columnas lat y lng
    #df['lat'] = df['lat'].astype(str).str.replace('.', ',').astype(float)
    #df['lng'] = df['lng'].astype(str).str.replace('.', ',').astype(float)
    df['lat'] = df['lat'].astype(float).round(6)
    df['lng'] = df['lng'].astype(float).round(6)
    
    df
    # Guardar como archivo Excel
    try:
        df.to_excel(output_excel, index=False)
        print(f"Archivo convertido y guardado exitosamente en: {output_excel}")
    except Exception as e:
        print(f"Error al guardar el archivo Excel: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Usamos las rutas que definiste al principio
    archivo_csv = "E:/_testExcelSql/clientes_xy.csv"
    archivo_excel = "E:/_testExcelSql/clientes_xy.xlsx"
    
    limpiar_y_convertir(archivo_csv, archivo_excel)
    #jnjnjn