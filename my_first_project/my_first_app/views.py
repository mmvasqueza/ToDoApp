from django.shortcuts import render

# Es sumamente importante la identación en Python
# esta definición de función debe ir sin espacios al inicio
# La vista se comunica con la plantilla (template)
# y le pasa datos a través del contexto (context)
# La vista recibe una petición (request) y devuelve una respuesta (response)
# Create your views here.
def CarView(request):
    car_list = [
        {"title": "BMW"},
        {"title": "Audi"},
        {"title": "Toyota"},
        {"title": "Honda"},
        {"title": "Ford"}
        ]    
    context = {
        "car_list" : car_list
        }
    return render(request, "my_first_app/car_list.html", context)