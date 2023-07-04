from io import BytesIO
import os
from aiohttp import request
import geoip2
import pandas as pd
import openpyxl as xls
from django.http import HttpResponse

from django.shortcuts import redirect, render
from geoip2 import database


def index(request):
    return render(request, 'index.html')

# def dpais(request):
#     return render(request, 'determinarpais.html' )

#Afortunadamente la plataforma utilizada para realizar las sesiones virtuales guardó la dirección IP 
#asignada a cada participante. Tu tarea será construir un script in Python para determinar el país 
#correspondiente a cada dirección IP.

def dpais(request):
    return render(request, 'determinarpais.html' )


def procesar_archivo(request):
    if request.method == 'POST' and request.FILES['archivo']:
        archivo = request.FILES['archivo']

        # Leer el archivo XLSX y obtener las direcciones IP
        data_frame = pd.read_excel(archivo)
        direcciones_ip = data_frame['Direccion IP']

        # Obtener el país correspondiente a cada dirección IP
        paises = []
        for ip in direcciones_ip:
            # Lógica para determinar el país desde la dirección IP
            pais = obtener_pais_desde_ip(ip)
            paises.append(pais)

        # Crear un nuevo DataFrame con las direcciones IP y los países
        resultado = pd.DataFrame({'Dirección IP': direcciones_ip, 'País': paises})

        # Convertir el DataFrame en un archivo XLSX en memoria
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            resultado.to_excel(writer, index=False)

        buffer.seek(0)

        # Almacenar los resultados en la sesión para mostrarlos en el nuevo HTML
        request.session['resultados'] = resultado.to_dict(orient='records')

        return redirect('mostrar_resultado')

    return render(request, 'procesar_archivo.html')

def mostrar_resultado(request):
    resultados = request.session.get('resultados', None)
    return render(request, 'mostrar_resultado.html', {'resultados': resultados})

def descargar_resultado(request):
    # Obtener el contenido del archivo resultado.xlsx
    with open('resultado.xlsx', 'rb') as file:
        response = HttpResponse(file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=resultado.xlsx'
        return response

def obtener_pais_desde_ip(ip):
    # Aquí debes implementar la lógica para determinar el país correspondiente a la dirección IP
    # Utiliza la biblioteca geoip2 o cualquier otra fuente de datos confiable para obtener esta información
    # En este ejemplo, simplemente se devuelve "Desconocido"
    database_path = 'utils/GeoLite2-Country.mmdb'

    try:
        # Crear un lector para la base de datos
        reader = geoip2.database.Reader(database_path)

        # Obtener la información de geolocalización para la dirección IP
        response = reader.country(ip)

        # Obtener el nombre del país desde la respuesta
        pais = response.country.name

        # Cerrar el lector de la base de datos
        reader.close()

        return pais
    except Exception as e:
        # Manejar cualquier error que ocurra durante la determinación del país
        # En este ejemplo, simplemente se devuelve "Desconocido"
        return "Desconocido"

def mostrar_direcciones(request):
    # Leer el archivo XLSX
    data_frame = pd.read_excel('participantes.xlsx')

    # Extraer la columna "Dirección IP" y el país
    direcciones_ip = data_frame['Dirección IP']
    paises = data_frame['País']

    # Crear una lista de tuplas (dirección IP, país)
    direcciones_con_pais = list(zip(direcciones_ip, paises))

    return render(request, 'index.html', {'direcciones': direcciones_con_pais})

def procesar_datos(request):
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario
        datos_procesar = request.POST.get('datos_procesar')

        # Realizar el procesamiento de los datos
        # ...

        # Redirigir a la página principal o mostrar un mensaje de éxito
        return redirect('mostrar_direcciones')

    # Si el método de solicitud no es POST, redirigir a la página principal
    return redirect('mostrar_direcciones')

def descargar_excel(request):
    # Lógica para crear un nuevo archivo Excel con las direcciones IP y los países
    # ...

    # Guardar el nuevo archivo Excel en una ubicación temporal
    nuevo_archivo_excel = 'ruta_del_nuevo_archivo.xlsx'

    # Descargar el archivo Excel
    with open(nuevo_archivo_excel, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=nuevo_archivo.xlsx'

    # Eliminar el archivo temporal
    os.remove(nuevo_archivo_excel)

    return response