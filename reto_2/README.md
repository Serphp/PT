
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

## Caracteristicas 

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
* <b> Condicion </b> si PEP es cierto, su nivel de riesgo se vuelve automaticamente Alto.

