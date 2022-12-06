from django.http import HttpResponse
import datetime
from django.template import Template,Context

class persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo(request):
   p1=persona('david','luques')
   time=datetime.datetime.now()
   doc_externo=open("C:/Users/Globons/Desktop/practice/pildoras_informaticas/Informatic_pills/informatic_pills/plantillas/miplantilla.html")
   plt=Template(doc_externo.read())
   doc_externo.close()
   temasDelCurso=["plantillas","Modelos","Formularios","Vistas","Despliegue"]
   ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"actual":time, "temas":temasDelCurso})
   documento=plt.render(ctx)
   return HttpResponse(documento)

def bye (request):
    return HttpResponse('bye everyone')

def damefecha(request):
    fecha_actual=datetime.datetime.now()

    documento= """<html>
    <body>
    <h1>
    Fecha y hora actuales: %s
    </h1>
    </body>
    </html>
    """ % fecha_actual
    return HttpResponse(documento)

def calculaedad(request,edad,anio):
    edadactual=18
    periodo=anio-2019
    edadfutura=edad+periodo
    documento="""
    <html>
    <body>
    <h2>
    En el anio %s tendras %s anios
    """%(anio,edadfutura)
    return HttpResponse(documento)
