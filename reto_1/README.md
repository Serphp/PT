
## Objetivo
determinar el país correspondiente de cada dirección IP.

## Funcionamiento e Instalación
Para iniciar el script de <b>python</b> debes contar con una versión instalada de [python](https://www.python.org/downloads/) en tu sistema operativo.
```bash
1) pip install -r requirements.txt "(Instalación de librerias por si no las tienes instaladas)"
2) python main.py "(iniciar el script)"
```

* En la carpeta <b>utils</b> se colocan los archivos excel o csv para su analisís.

* Los resultados se guardaran en <b>/utils/resultados</b>

* <b>main.py</b> es el archivo principal con el programa.

* <b>GeoLite2-Country.mmd</b> es el archivo que contiene los datos para saber cual IP pertenece a tal pais.

## librerias utilizadas:
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
> 1.3 : Se añadio doble formato de lectura excel & csv 
        Se verifica el codigo y se acomodan por colunmas y filas.
```
