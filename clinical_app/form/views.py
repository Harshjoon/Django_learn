from django.shortcuts   import render
from django.http        import HttpResponse

# Create your views here.

test_form_format = {
    "Hospital name",
    "Patient name",
    "Surgery type",
    "Issues observed"
}

def form_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/main.html')

def home_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/home.html')

def about_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/about.html')