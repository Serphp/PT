from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import forms

class DatosPersonaForm(forms.Form):
    # Campos del formulario
    nombre = forms.CharField(max_length=50)
    segundo_nombre = forms.CharField(max_length=50, required=False)
    primer_apellido = forms.CharField(max_length=50)
    segundo_apellido = forms.CharField(max_length=50, required=False)
    genero = forms.ChoiceField(choices=[('Hombre', 'Hombre'), ('Femenino', 'Femenino')])
    pais_nacimiento = forms.ChoiceField(choices=[('Panamá', 'Panamá'), ('Otros países', 'Otros países')])
    pais_residencia = forms.ChoiceField(choices=[('Panamá', 'Panamá'), ('Otros países', 'Otros países')])
    profesion = forms.ChoiceField(choices=[('Abogado', 'Abogado'), ('Ingeniería', 'Ingeniería'), ('Médico', 'Médico'), ('Contador', 'Contador'), ('Otras profesiones', 'Otras profesiones')])
    edad = forms.ChoiceField(choices=[('Menos 25', 'Menos 25'), ('Entre 25 y 55', 'Entre 25 y 55'), ('Mayor de 55', 'Mayor de 55')])
    ingresos = forms.ChoiceField(choices=[('Menos de 20K anual', 'Menos de 20K anual'), ('Entre 20k y 75k', 'Entre 20k y 75k'), ('Mayor de 75k', 'Mayor de 75k')])
    pep = forms.ChoiceField(choices=[('Si', 'Si'), ('No', 'No')])


def index(request):
    # Si el formulario se envió, procesa los datos
    if request.method == 'POST':
        form = DatosPersonaForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            puntaje_riesgo, umbral_riesgo = calcular_puntaje_riesgo(datos)
            return redirect('mostrar_resultado', puntaje_riesgo=puntaje_riesgo, umbral_riesgo=umbral_riesgo)
    else:
        form = DatosPersonaForm()

    return render(request, 'index.html', {'form': form})

def calcular_puntaje_riesgo(datos):
    puntaje = 0
    umbral_riesgo = 'Bajo'
    peso = 0.10
    peso2 = 0.20

    # Calcular puntaje en base al país de nacimiento
    if datos['pais_nacimiento'] == 'Panamá':
        puntaje += 100
    else:
        puntaje += 200
    
    
    # Calcular puntaje en base al país de residencia
    if datos['pais_residencia'] == 'Panamá':
        puntaje += 100
    else:
        puntaje += 200

    # Calcular puntaje en base a la profesión
    if datos['profesion'] == 'Abogado':
        puntaje += 100
    elif datos['profesion'] == 'Ingeniería':
        puntaje += 200
    elif datos['profesion'] == 'Médico':
        puntaje += 300
    elif datos['profesion'] == 'Contador':
        puntaje += 400
    else:
        puntaje += 500

    # Calcular puntaje en base a la edad
    if datos['edad'] == 'Menos 25':
        puntaje += 100
    elif datos['edad'] == 'Entre 25 y 55':
        puntaje += 200
    elif datos['edad'] == 'Mayor de 55':
        puntaje += 300

    # Calcular puntaje en base al nivel de ingresos
    if datos['ingresos'] == 'Menos de 20K anual':
        puntaje += 100
    elif datos['ingresos'] == 'Entre 20k y 75k':
        puntaje += 200
    elif datos['ingresos'] == 'Mayor de 75k':
        puntaje += 300

    # Calcular puntaje en base a si es PEP
    if datos['pep'] == 'Si':
        puntaje += 100
        umbral_riesgo = 'Alto'  # Si es PEP, el nivel de riesgo es siempre alto
    else:
        umbral_riesgo = 'Bajo'  # Inicialmente, asumimos nivel de riesgo bajo
        puntaje += 200
    
    return puntaje, umbral_riesgo
    # retorna el puntaje total y umbral_riesgo

def mostrar_resultado(request, puntaje_riesgo, umbral_riesgo):
    porcentaje = puntaje_riesgo / 500 * 100

    # Calcular umbral de riesgo
    if puntaje_riesgo >= 1400:
        umbral_riesgo = 'Alto'
    elif puntaje_riesgo >= 1200:
        umbral_riesgo = 'Medio'
    else:
        umbral_riesgo = 'Bajo'
    #Renderiza los resultados en la plantilla mostrar_resultado.html
    return render(request, 'mostrar_resultado.html', {'puntaje_riesgo': puntaje_riesgo, 'porcentaje': porcentaje, 'umbral_riesgo': umbral_riesgo})