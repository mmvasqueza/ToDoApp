from django.shortcuts import render

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