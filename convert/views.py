from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from .lectura import leer,precioMetales, respuestas, libros


def contact(request):
  form=InputForm()
  resultado=[] 
  if request.method=='POST':
    form= InputForm(request.POST)
    if form.is_valid():

      Datos=form.cleaned_data['Datos']
      #email=form.cleaned_data['email']
      #body= body.append('123')
      Datos2=Datos.split('\r\n')
      #body2.append('extra')
      frasesMetal,preguntas=leer(Datos2)
      precioMetales(libros.valor,frasesMetal)
      resultado=respuestas(preguntas,libros.valor,libros.metales)
      for lineas in resultado:
        print(lineas)
      
      libros.valor={}
      libros.metales={}
     
  
      
  args = {'form':form, 'resultado':resultado}
     
  form=InputForm() 
  
  return render(request,'form.html',args)

