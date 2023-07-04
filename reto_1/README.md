
## Objetivo
determinar el país correspondiente de cada dirección IP.

## Funcionamiento 

* En la carpeta <b>utils</b> agregaras los archivos excel para el funcionamiento correcto

* Los resultados se guardaran en <b>/utils/resultados</b>

* <b>main.py</b> es el archivo principal con el programa.

* <b>GeoLite2-Country.mmd</b> es el archivo que contiene los datos para saber cual IP pertenece a tal pais.

## Dependencias

Para utilizar el programa necesitas tener <b> python 3.8+ </b> e instalar las siguientes librerias con la linea de codigo:

```
pip install -r requeriments
```
contenido:
```bash
> geoip2
> Pandas
```


## Changelog

```bash
> 1.1 : añade una excepcion por si no existe un nombre con IP 
        (para darle mas orden)
        Se hace un filter para que solo se acepten archivos .xlsx en la variable "archivos"

> 1.2 : Se añade la opción 0 para salir del programa
        Se añade una condición si desea continuar o no después de terminar de convertir un archivo.
```