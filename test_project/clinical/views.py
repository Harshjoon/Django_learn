from django.shortcuts import render
from django.http        import HttpResponse

# Create your views here.
def fill_data(request):
    #return HttpResponse('<hi>home page</h1>')   
    return render(request, 'clinical/fill_data.html')