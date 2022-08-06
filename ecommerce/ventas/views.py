from django.shortcuts import HttpResponse
from django.shortcuts import render
html_base = """
 <h1>Shopping Car</h1>
 <ul>
   <li><a href="/">Inicio</a></li>
   <li><a href="/articulo/">Articulos</a></li>
   <li><a href="/cliente/">Clientes</a></li>
   <li><a href="/venta/">Ventas</a></li>
   <li><a href="/consulta/">Consultas</a></li>
 </li>
"""
def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)


def articulo(request):
  return HttpResponse(html_base+
    """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")

def cliente(request):
  data = {
      'titulo':'GESTION DE CLIENTESssss',
      'crear_url': '/crearcliente',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/listCliente.html",data)

def crearCliente(request):
  data = {
      'titulo':'MANTENIMIENTO DE CLIENTES',
      'crear_url':'/crearcliente',
      'action':'add',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/formCliente.html",data)

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)

def contabilidad(request):
  data = {
        'titulo': "OPCIONES MODULO CONTABLE"
  }
  return render(request, "modcontabilidad/contabilidad.html",data)








def opc1(request):
  data = {
        'titulo': "PLAN DE CUENTAS",
        'crearC_url': '/crearcontabilidad',
        'listarC_url': '/contabilidad1',
  }
  return render(request, "modcontabilidad/opcion1.html", data)

def crearContabilidad(request):
  data = {
      'titulo':'MANTENIMIENTO DE CONTABILIDAD',
      'crearC_url':'/crearcontabilidad',
      'action':'add',
      'listarC_url': '/contabilidad1',
  }
  return render(request, "modcontabilidad/formContabilidad.html",data)












def opc2(request):
  data = {
        'titulo': "ENERO 2022"
  }
  return render(request, "modcontabilidad/opcion2.html", data)

def opc3(request):
  data = {
        'titulo': "LIBRO DIARIO"
  }
  return render(request, "modcontabilidad/opcion3.html", data)




