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

def mostrar_archivos():
    carpeta = 'utils'
    archivos = [archivo for archivo in os.listdir(carpeta) if archivo.endswith(('.xlsx', '.csv'))]

    if len(archivos) == 0:
        print("No se encontraron archivos .xlsx o .csv en la carpeta.")
        return

    print("Archivos .xlsx o .csv encontrados en la carpeta:")
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
    if ruta_archivo.endswith('.xlsx'):
        dataframe = pd.read_excel(ruta_archivo)
    elif ruta_archivo.endswith('.csv'):
        dataframe = pd.read_csv(ruta_archivo, delimiter=';')
    else:
        raise ValueError("Formato de archivo no válido.")

    # if 'IP' not in dataframe.columns:
    #     dataframe['IP'] = ''  # Agrega una columna 'IP' vacía

    return dataframe

def crear_nuevo_archivo(dataframe, contador):
    carpeta_resultados = 'utils/resultados'
    if not os.path.exists(carpeta_resultados):
        os.makedirs(carpeta_resultados)

    archivo_salida = os.path.join(carpeta_resultados, f'resultados{contador}.xlsx')
    dataframe.to_excel(archivo_salida, index=False)
    print(f"El nuevo archivo '{archivo_salida}' ha sido creado exitosamente.")

def mostrar_opcion_continuar():
    opcion = input("¿Desea continuar? (S/N): ")
    return opcion.upper() == "S"

# Programa principal
contador = 1

while True:
    ruta_archivo = mostrar_archivos()
    if ruta_archivo is None:
        break

    try:
        dataframe = leer_archivo_ips(ruta_archivo)
    except ValueError as e:
        print(str(e))
        continue

    dataframe['País'] = dataframe['GDPR IP'].apply(obtener_pais)

    crear_nuevo_archivo(dataframe, contador)
    contador += 1

    if not mostrar_opcion_continuar():
        break
