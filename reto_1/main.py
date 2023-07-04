import os
import pandas as pd
from geoip2 import database

def obtener_pais(ip):
    reader = database.Reader('GeoLite2-Country.mmdb')
    try:
        response = reader.country(ip)
        return response.country.name
    except:
        return 'Desconocido'

#Inicio del programa
def mostrar_archivos():
    carpeta = 'utils'
    #Archivo solo leera los archivos con extension .xlsx
    archivos = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.xlsx')]

    if len(archivos) == 0:
        print("No se encontraron archivos en la carpeta.")
        return

    print("Archivos encontrados en la carpeta:")
    for i, archivo in enumerate(archivos):
        print(f"{i+1}. {archivo}")

    print("0. Salir")
    seleccion = int(input("Seleccione el número del archivo a utilizar: "))
    if seleccion == 0:
        return None
    if seleccion < 1 or seleccion > len(archivos):
        print("Opción inválida.")
        return

    archivo_seleccionado = archivos[seleccion-1]
    ruta_archivo = os.path.join(carpeta, archivo_seleccionado)

    return ruta_archivo

def leer_archivo_ips(ruta_archivo):
    dataframe = pd.read_excel(ruta_archivo)

    if 'IP' not in dataframe.columns:
        dataframe['IP'] = ''  # Agrega una columna 'IP' vacía - 1.1 

    return dataframe

def crear_nuevo_archivo(dataframe):
    carpeta_resultados = 'utils/resultados'
    if not os.path.exists(carpeta_resultados):
        os.makedirs(carpeta_resultados)

    archivo_salida = os.path.join(carpeta_resultados, 'resultados.xlsx')
    dataframe.to_excel(archivo_salida, index=False)
    print(f"El nuevo archivo '{archivo_salida}' ha sido creado exitosamente.")

# Solucion
ruta_archivo = mostrar_archivos()
if ruta_archivo is None:
    exit()

dataframe = leer_archivo_ips(ruta_archivo)
dataframe['País'] = dataframe['IP'].apply(obtener_pais)

crear_nuevo_archivo(dataframe)
