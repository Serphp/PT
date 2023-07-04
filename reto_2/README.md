
## Objetivo
Calcular el perfil de riesgo de una persona.

| Nivel de riesgo | Limites         |
|-----------------|---------------|
| Bajo            | Menos de 1200 |
| Medio           | Entre 1201 a 1400 |
| Alto            | Mayor a 1401 |

## Instalación
```
py -m pip install Django
o
python -m pip install Django
```

## Inicia el servidor 
```
python manage.py runserver
```

## Características 

* Formulario de campo que contiene
    * Nombre
    * Segundo nombre
    * Apellido
    * Segundo apellido
    * Genero
    * País de nacimiento
    * País de residencia
    * Profesión
    * Edad
    * Ingresos
    * PEP (Persona Expuesta Políticamente)
* Botón de calcular
* Resultado del perfil de riesgo
* Botón de regresar
* <b> Condicion </b> si PEP es cierto, su nivel de riesgo se vuelve automáticamente Alto.

## Problemas
Para extraer el calculo de riesgo utilizando la formula: <br>
```
Cálculo de riesgo: (País de nacimiento x peso) + (País de residencia * peso) + (Profesión * peso) + edad * peso, + nivel de ingresos + (PEP * peso) 
```
Presente un problema en el que no sabia exactamente como presentar el calculo de forma precisa.
Ejemplo utilizando la "pais_residencia" en python 

```python
peso = 0.10
    if datos['pais_residencia'] == 'Panamá':
        puntaje += int(100 * peso)
    else:
        puntaje += int(200 * peso)
```
no sabia como exactamente presentar el desarrollo eficiente porque al multiplicar los (200 puntos * 10%) que seria el 0.10 vendría siendo *40* en total.
Si hacia la misma multiplicación utilizando el *10%* y *20%* la función de puntaje de riesgo para sacar el calculo umbral de riesgo no superarían de *500 puntos*. 

[Calculo de riesgo Incluyendo Peso](https://github.com/Serphp/PT/blob/master/reto_2/frontpr/views_cr.py)
