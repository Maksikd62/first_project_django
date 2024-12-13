from django.shortcuts import render
from django.http import HttpResponse

elements = [
    {"id": 1, "name": "Book", "description": "Harry Potter", "contact_number": "123-456-7890"},
    {"id": 2, "name": "Film", "description": "Bones", "contact_number": "098-765-4321"},
]

def list(request):
    html = "<h1>Elements</h1> <ul>"
    for element in elements:
        html += f"<li>{element['name']}</li>"
    html += "</ul>"

    return HttpResponse(html)

def detail(request, id):
    element = None
    for el in elements:
        if el["id"] == id:
            element = el
            break
    if element is not None:
        html = f"<h1>{element['name']}</h1>"
        html += f"<p>Description: {element['description']}</p>"
        html += f"<p>Contact Number: {element['contact_number']}</p>"
        return HttpResponse(html)
    else:
        return HttpResponse("Element not found", status=404)
