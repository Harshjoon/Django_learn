from django.shortcuts   import render
from django.http        import HttpResponse
from .forms             import surgery_data_form
# Create your views here.

test_form_format = {
    "Hospital name",
    "Patient name",
    "Surgery type",
    "Issues observed"
}

def surgery_form_page(request):
    form = surgery_data_form()
    return render(request, 'form/surgery_data_from.html', {'forms' : form})

def form_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/main.html')

def home_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/home.html')

def about_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/about.html')