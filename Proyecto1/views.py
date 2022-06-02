from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

def saludo(request):
  return HttpResponse("Hola mundo")

def otro_saludo(request):
  return HttpResponse("argentina 3 - italia 0 - vamoooo")

def DiaDeHoy(request):
  dia = datetime.datetime.now()

  DocumentoDeTexto = f'hoy es dia: <br> {dia}'
  return HttpResponse(DocumentoDeTexto)




def probandoTemplate(self): #Funcion para llamar al HTML

  nombre = 'maX'
  apellido = 'veGa'
  ListaDeNotas = [2, 5, 6, 9]

  diccionario = {"nombre": nombre, "apellido": apellido, "ListaDeNotas": ListaDeNotas}

  #miHtml = open("templates1.html")
    
  #plantilla = Template(miHtml.read())
  #miHtml.close()

  plantilla = loader.get_template('templates1.html')
  documento = plantilla.render(diccionario)

  return HttpResponse(documento)

