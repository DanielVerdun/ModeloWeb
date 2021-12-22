from django.shortcuts import render , redirect
from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    
    formulario = FormularioContacto()
    
    if request.method == "POST":
        
        formulario = FormularioContacto(data=request.POST)

        if formulario.is_valid():

            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido") 
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            return redirect("/contacto/contacto/?valido")

    return render(request, "contacto/contacto.html",{"formulario":formulario})