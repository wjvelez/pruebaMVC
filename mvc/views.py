from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from mvc.models import Orders
from mvc.models import OrderDetails

import requests


def hola(request):
    return render(request, 'mvc/prueba.html')

def index(request, customerid = ""):
    if (customerid != None and customerid != ""):
        orders = Orders.objects.filter(customerid__istartswith = customerid)
    else:
        orders = Orders.objects.all()

    return render(request, 'mvc/index.html', {
        'orders': orders,
    })

def order_detail(request, orderid):
    try:
        # Retorna una lista de objetos 'OrderDetails' filtrada por el atributo orderid
        detail_list = OrderDetails.objects.filter(orderid=orderid)
    except OrderDetails.DoesNotExist:
        raise Http404('No existe este objecto')
    return render(request, 'mvc/order_detail.html', {
        'detail_list': detail_list,
        'orderid': orderid,
    })

# Create your tests here.

# enviar solicitud a espol

#user=input('usuario: ')
#clave=input('clave: ')

"""
POST /saac/wsandroid.asmx/autenticacion HTTP/1.1
Host: ws.espol.edu.ec
Content-Type: application/x-www-form-urlencoded
Content-Length: length

authUser=string&authContrasenia=string

HTTP/1.1 200 OK
Content-Type: text/xml; charset=utf-8
Content-Length: length

<?xml version="1.0" encoding="utf-8"?>
<boolean xmlns="http://tempuri.org/">boolean</boolean>
"""

#direc = "http://ws.espol.edu.ec//saac/wsandroid.asmx//autenticacion?"


us=input('usuario: ')
cl=input('clave: ')
#r = requests.get('http://ws.espol.edu.ec//saac/wsandroid.asmx//autenticacion', auth=(usuario, clave))
r = requests.get('https://api.github.com/user', auth=(us, cl))

#direc = direc + "authUser=\"" + user + "\"&" + "authContrasenia=\"" + clave + "\""


# direc = direc + "authUser=\"" + user + "\"&" + "authContrasenia=\"" + real + "\""
#print(direc)

#authUser="wjvelez"
#authContrasenia="string"
#r = requests.get('http://ws.espol.edu.ec//saac/wsandroid.asmx//autenticacion?authUser="string"&authContrasenia="string"')

#
#authUser=input('usuario: ')
#authContrasenia=input('clave: ')
#direc = "http://ws.espol.edu.ec//saac/wsandroid.asmx//autenticacion?"
#direc = direc + authUser + "&" + authContrasenia
#r = requests.get('http://ws.espol.edu.ec//saac/wsandroid.asmx//autenticacion?authUser&authContrasenia')
#r = requests.get('http://ws.espol.edu.ec//saac/wsandroid.asmx//autenticacion?authUser="string"&authContrasenia="string"')
#r = requests.get(direc)
#r.status_code
#r.headers['content-type']
#r.encoding
print(r.text)





























