from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'catalog/contacts.html')
def homepage(request):
    return render(request, 'catalog/home.html')
