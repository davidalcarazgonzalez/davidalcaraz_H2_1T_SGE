import pandas as pd

def exportar_a_excel(encuestas):
    """
    Exporta los datos de las encuestas a un archivo Excel.
    """
    try:
        # Convertir los datos en un DataFrame
        df = pd.DataFrame(encuestas)

        # Exportar a un archivo Excel
        df.to_excel('encuestas.xlsx', index=False, engine='openpyxl')
        return "Datos exportados a Excel con éxito."

    except Exception as e:
        return f"Hubo un problema al exportar los datos: {e}"

def exportar_a_excel_con_filtros(encuestas):
    """
    Exporta los datos filtrados de las encuestas a un archivo Excel.
    """
    try:
        # Convertir los datos filtrados en un DataFrame
        df = pd.DataFrame(encuestas)

        # Exportar los datos filtrados a un archivo Excel
        df.to_excel('encuestas_filtradas.xlsx', index=False, engine='openpyxl')
        return "Datos filtrados exportados a Excel con éxito."

    except Exception as e:
        return f"Hubo un problema al exportar los datos filtrados: {e}"
