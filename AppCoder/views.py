from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Adopcion
from django.core import serializers
from AppCoder.forms import AdopcionFormulario
from django.views.generic import ListView
from django.views.generic.edit import   CreateView, UpdateView,  DeleteView
from django.views.generic.detail import DetailView
#PROVISORIOS
from AppCoder.models import Provisorios
from AppCoder.forms import ProvisoriosFormulario
#ENCONTRADOS
from AppCoder.models import Encontrados
from AppCoder.forms import EncontradosFormulario
from AppCoder.forms import * 


def inicio(request):
    return render(request,'AppCoder/inicio.html')


def adopcionApi(request):
    Adopcion_todos =Adopcion.objects.all()
    return HttpResponse(serializers.serialize('json', Adopcion_todos))


def buscaradopcion(request):
    return render( request, 'AppCoder/busquedaAdopcion.html')

def buscar(request):
    codigo = request.GET['nombre_de_Mascota']
    mascotas_todas = Adopcion.objects.filter(nombre_de_Mascota=codigo)
    #return HttpResponse (f'Esta es la linea {codigo} que tiene estos destinos:')
    return render(request, 'AppCoder/resultadosAdopcion.html', {"Adopcion":codigo, "nombre_de_Mascota":mascotas_todas})


def Adopciones (request):
    if request.method == "POST":
            miFormulario = AdopcionFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                  #informacion = {"curso":"12313", "camada": 1223, "numero_dia":1}
                Adop = Adopcion(nombre_de_Mascota=informacion["nombre_de_Mascota"], edad=informacion["edad"], 
                genero=informacion["genero"], mail=informacion["mail"], tipo=informacion["tipo"],
                    castracion=informacion["castracion"], nombre_del_Tutelar=informacion["nombre_del_Tutelar"], 
                    telefono=informacion["telefono"])
                Adop.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = AdopcionFormulario()
 
    return render(request, "AppCoder/Adopcion.html", {"miFormulario": miFormulario})


#CRUD-ADOPCIONES-------------------------
def leer_adopcion(request):
    adopcion_all= Adopcion.objects.all()
    return HttpResponse (serializers.serialize('json',adopcion_all))

def crear_adopcion(request):
    adopcion1= Adopcion(nombre_de_Mascota="Max",edad="5", 
                genero="macho", mail="mad_max@mail.com", tipo="canino",
                    castracion="si", nombre_del_Tutelar="Juan Perez", 
                    telefono="3517851654")
    adopcion1.save()
    return HttpResponse(f'Adopcion de {adopcion1} ha sido creada')

def editar_adopcion(request):
    nombre_consulta="Max"
    Adopcion.objects.filter(nombre_de_Mascota=nombre_consulta).update(nombre_de_Mascota="PepeNuevo")
    return HttpResponse(f'La adopcion de {nombre_consulta} ha sido actualizada')

def eliminar_adopcion(request):
    nombre_nuevo = "PepeNuevo"
    adopcion1= Adopcion.objects.get(nombre_de_Mascota=nombre_nuevo)
    adopcion1.delete()
    return HttpResponse(f'Adopcion {nombre_nuevo} ha sido eliminado')

#------LISTA----(clase 23)

class AdopcionesList(ListView):
    model = Adopcion
    template = "AppCoder/adopcion_list.html"

class AdopcionesCreate(CreateView):
    model = Adopcion
    fields = '__all__'
    success_url = '/AppCoder/adopciones/list/'

#-----Clase 24------------
class AdopcionesEdit(UpdateView):
    model = Adopcion
    fields = '__all__'
    success_url = '/AppCoder/adopciones/list/'

class AdopcionesDetail(DetailView):
    model = Adopcion
    template_name='AppCoder/adopcion_detail.html'

class AdopcionesDelete(DeleteView):
    model = Adopcion
    success_url = '/AppCoder/adopciones/list/'


#Provisorio------------------------

def Provisoriooos(request):
    if request.method == "POST":
            miFormularioProvi = ProvisoriosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormularioProvi)
 
            if miFormularioProvi.is_valid:
                informacionP = miFormularioProvi.cleaned_data
                  #informacion = {"curso":"12313", "camada": 1223, "numero_dia":1}
                Provi = Provisorios(nombreProvisorio=informacionP["nombreProvisorio"], tipo=informacionP["tipo"], 
                    genero=informacionP["genero"], animalesenCasa=informacionP["animalesenCasa"],
                    telefono=informacionP["telefono"],mail=informacionP["mail"])
                Provi.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormularioProvi = ProvisoriosFormulario()
 
    return render(request, "AppCoder/Provisorios.html", {"miFormularioProvi": miFormularioProvi})

def provisoriosApi(request):
    Provisorios_todos= Provisorios.objects.all()
    return HttpResponse(serializers.serialize('json', Provisorios_todos))

def buscarprovisorio(request):
    return render( request, 'AppCoder/busqueda_provisorio.html')

def buscarP(request):
    codigoP = request.GET['nombreProvisorio']
    tutelar_todos = Provisorios.objects.filter(nombreProvisorio=codigoP)
    #return HttpResponse (f'Esta es la linea {codigo} que tiene estos destinos:')
    return render(request, 'AppCoder/resultado_provisorio.html', {"PROVISORIO":codigoP, "nombreProvisorio":tutelar_todos})

#--------------------------#CRUD-Provisorios-------------------------

def leer_provisorio(request):
    provisorio_all= Provisorios.objects.all()
    return HttpResponse (serializers.serialize('json',provisorio_all))

def crear_provisorio(request):
    provisorio1= Provisorios (nombreProvisorio="Maxi Asta", 
                genero="macho", mail="mad_max@mail.com", tipo="canino",
               telefono="3517851654",animalesenCasa="perro macho")
    provisorio1.save()
    return HttpResponse(f'Provisorio {provisorio1} ha sido creada')

def editar_provisorio(request):
    nombreP_consulta="Maxi Asta"
    Provisorios.objects.filter(nombreProvisorio=nombreP_consulta).update(nombreProvisorio="Laura Nuevo")
    return HttpResponse(f'La adopcion de {nombreP_consulta} ha sido actualizada')

def eliminar_provirosio(request):
    nombreP_nuevo = "Laura Nuevo"
    provisorio1= Provisorios.objects.get(nombreProvisorio=nombreP_nuevo)
    provisorio1.delete()
    return HttpResponse(f'Provisorio {nombreP_nuevo} ha sido eliminado')

#------LISTA----(clase 23)
class ProvisoriosList(ListView):
    model = Provisorios
    template_name = 'AppCoder/provisorios_list.html'

class ProvisoriosCreate(CreateView):
    model = Provisorios
    fields = '__all__'
    success_url = '/AppCoder/provisorios/list/'
#-----Clase 24------------
class ProvisoriosEdit(UpdateView):
    model = Provisorios
    fields = '__all__'
    success_url = '/AppCoder/provisorios/list'

class ProvisoriosDetail(DetailView):
    model = Provisorios
    template_name='AppCoder/provisorios_detail.html'

class ProvisoriosDelete(DeleteView):
    model = Provisorios
    success_url = '/AppCoder/provisorios/list'




#ENCONTRADOS---------------------------------------------
def Encontradooos(request):
    if request.method == "POST":
            miFormularioE = EncontradosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormularioE)
 
            if miFormularioE.is_valid:
                informacionE = miFormularioE.cleaned_data
                  #informacion = {"curso":"12313", "camada": 1223, "numero_dia":1}
                Enc = Encontrados(nombreRetiene=informacionE["nombreRetiene"],
                    telefono=informacionE["telefono"],mail=informacionE["mail"])
                Enc.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormularioE = EncontradosFormulario()
 
    return render(request, "AppCoder/Encontrados.html", {"miFormularioE": miFormularioE})

def encontradosApi(request):
    Encontrados_todos= Encontrados.objects.all()
    return HttpResponse(serializers.serialize('json', Encontrados_todos))

def buscarencontrados(request):
    return render( request, 'AppCoder/busqueda_encontrados.html')

def buscarE(request):
    codigoE = request.GET['nombreRetiene']
    retiene_todos = Encontrados.objects.filter(nombreRetiene=codigoE)
    #return HttpResponse (f'Esta es la linea {codigo} que tiene estos destinos:')
    return render(request, 'AppCoder/resultados_encontrados.html', {"ENCONTRADOS":codigoE, "nombreRetiene":retiene_todos})

#CRUD-Encontrados-------------------------
def leer_encontrado(request):
    encontrado_all= Encontrados.objects.all()
    return HttpResponse (serializers.serialize('json',encontrado_all))

def crear_encontrado(request):
    encontrado1= Encontrados( nombreRetiene="Lisa", mail="lisa_123@gmail.com", 
                    telefono="351786454")
    encontrado1.save()
    return HttpResponse(f'Encontrado por {encontrado1} ha sido creado')

def editar_encontrado(request):
    nombre_consultaE="Lisa"
    Encontrados.objects.filter(nombreRetiene=nombre_consultaE).update(nombreRetiene="Juan")
    return HttpResponse(f'El nombre de quien retiene {nombre_consultaE} ha sido actualizado')

def eliminar_encontrado(request):
    nombre_nuevoE = "Juan"
    encontrado1= Encontrados.objects.get(nombreRetiene=nombre_nuevoE)
    encontrado1.delete()
    return HttpResponse(f'Retención de animal por {nombre_nuevoE} ha sido eliminado')


class EncontradoList(ListView):
    model = Encontrados
    template_name="AppCoder/encontrados_list.html"


class EncontradoCreacion(CreateView):
    model = Encontrados
    fields= '__all__'
    success_url= '/AppCoder/encontrado/list'


# Editar
class EncontradoEdit(UpdateView):
    model = Encontrados
    fields= '__all__'
    success_url= '/AppCoder/encontrado/list'  


# Detalle
class EncontradoDetail(DetailView):
    model = Encontrados
    template_name="AppCoder/encontrados_detail.html"

# Borrar
class EncontradoDelete(DeleteView):
    model=Encontrados
    success_url = 'AppCoder/encontrado/list'


#experimentando...(?)
def historia(request):
    return render(request,'AppCoder/historia.html')

def contacto(request):
    return render(request,'AppCoder/contacto.html')

def Quien(request):
    return render(request,'AppCoder/quien.html')

def Privacidad(request):
    return render(request,'AppCoder/privacidad.html')