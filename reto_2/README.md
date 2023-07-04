
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

## Logica para calcular el perfil de riesgo
(País de nacimiento * peso) +  <br>
(País de residencia * peso) + <br>
(Profesión * peso) + <br>
(edad * peso ) + <br>
(nivel de ingresos) + <br>
(PEP * peso) <br>

* Condicion si es PEP su nivel de riesgo se vuelve automaticamente Alto.

