import os
import pandas as pd

def generar_excel_prueba():
    # 1. Creamos un diccionario con información simple
    datos = {
        'ID_Ticket': [1, 2],
        'Asunto': ['Prueba de carga', 'Hola Mundo'],
        'Estado': ['Pendiente', 'Nuevo']
    }

    df = pd.DataFrame(datos)

    # 3. Definimos el nombre del archivo
    nombre_archivo = 'Back/data/output/tickets_prueba.xlsx'

    print(f"Generando el archivo {nombre_archivo}...")

    try:
        # 4. Guardamos el archivo en formato Excel
        # Usamos engine='openpyxl' que es el estándar actual
        df.to_excel(nombre_archivo, index=False, engine='openpyxl')
        
        if os.path.exists(nombre_archivo):
            print("¡Éxito! El archivo Excel ha sido creado correctamente.")
            print(f"Ruta completa: {os.path.abspath(nombre_archivo)}")
        else:
            print("El archivo no se encontró tras el guardado.")

    except Exception as e:
        print(f"Ocurrió un error al generar el Excel: {e}")