from django.shortcuts       import render
from django.views.generic   import ListView
from django.http            import HttpResponse
from .models                import Post
from .forms                 import clinical_form

# DUMMY DATA
# test_form_format = {
#     "Hospital name",
#     "Patient name",
#     "Surgery type",
#     "Issues observed"
# }

def main_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    #return render(request, 'form/main.html')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'form/main.html', context)

def forms_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    #return render(request, 'form/main.html')

    if request.method == 'POST':
        form_data = clinical_form(request.POST)
        
        if form_data.is_valid():
            hospital_name   = form_data.cleaned_data['hospital_name']
            patient_name    = form_data.cleaned_data['patient_name']

            post            = Post(
                hospital_name = hospital_name,
                patient_name  = patient_name
            )            
            post.author = request.user
            post.save()
            
            #return render(request, 'form/home.html')
            return HttpResponse(f"Recived patient name : {patient_name}")

    form_context = {
        'forms': clinical_form()
    }

    return render(request, 'form/form.html', form_context)

def home_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/home.html')

def about_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/about.html')


'''

'''