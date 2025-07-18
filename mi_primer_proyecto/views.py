from django.http import HttpResponse

def index(request): 
    return HttpResponse("<h1> ¡Hola, mundo! Esta es mi primera vista en Django.</h1>")    
