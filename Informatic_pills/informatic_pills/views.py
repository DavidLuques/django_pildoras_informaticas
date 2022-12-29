from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render


# loader is loader
class persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
<<<<<<< HEAD
    p1 = persona("david", 'luques')
    p2 = persona('Profeso', 'Juan')
    time = datetime.datetime.now()
    # doc_externo=open("C:/Users/Globons/Desktop/practice/pildoras_informaticas/Informatic_pills/informatic_pills/plantillas/miplantilla.html")
    # plant=Template(doc_externo.read())
    # doc_externo.close()

    doc_externo = loader.get_template('miplantilla.html')

    temasDelCurso = ["plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    # ctx=Context({"nombre_persona":p2.nombre,"apellido_persona":p2.apellido,"actual":time, "temas":temasDelCurso})
    contexto={"nombre_persona": p2.nombre, "apellido_persona": p2.apellido, "actual": time, "temas": temasDelCurso}
   # documento = doc_externo.render(contexto)
    return render(request,'miplantilla.html',contexto )

def cursoC (request):
    fecha_actual = datetime.datetime.now()
    return render(request,'cursoC.html',{"dameFecha":fecha_actual},)

def cursoCeseese (request):
    fecha_actual = datetime.datetime.now()
    return render(request,'cursoCss.html',{"dameFecha":fecha_actual},)


def bye(request):
=======
   p1=persona('david','luques')
   time=datetime.datetime.now()
   doc_externo=open("C:/Users/User/Desktop/django_pildoras_informaticas/Informatic_pills/informatic_pills/plantillas/miplantilla.html")
   plt=Template(doc_externo.read())
   doc_externo.close()
   temasDelCurso=["plantillas","Modelos","Formularios","Vistas","Despliegue"]
   ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"actual":time, "temas":temasDelCurso})
   documento=plt.render(ctx)
   return HttpResponse(documento)

def bye (request):
>>>>>>> d670e55414571e5ac4add661d5a3e2abb4efe5d2
    return HttpResponse('bye everyone')


def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales: %s
    </h1>
    </body>
    </html>
    """ % fecha_actual
    return HttpResponse(documento)


def calculaedad(request, edad, anio):
    edadactual = 18
    periodo = anio - 2019
    edadfutura = edad + periodo
    documento = """
    <html>
    <body>
    <h2>
    En el anio %s tendras %s anios
    """ % (anio, edadfutura)
    return HttpResponse(documento)
