from django.shortcuts       import render
from django.views.generic   import ListView
from django.http            import HttpResponse
from .models                import Post
from .forms                 import clinical_form
from .functions             import set_models
from django.contrib.auth.decorators     import login_required
from django.contrib             import messages

# DUMMY DATA
# test_form_format = {
#     "Hospital name",
#     "Patient name",
#     "Surgery type",
#     "Issues observed"
# }

@login_required
def main_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    #return render(request, 'form/main.html')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'form/main.html', context)

@login_required
def forms_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    #return render(request, 'form/main.html')

    if request.method == 'POST':
        form_data = clinical_form(request.POST)

        if form_data.is_valid():
            print("--------------------------")
            # hospital_name   = form_data.cleaned_data['hospital_name']
            # patient_name    = form_data.cleaned_data['patient_name']
            # post            = Post(
            #     hospital_name = hospital_name,
            #     patient_name  = patient_name
            # )                        
            # post.author = request.user
            # post.save()

            set_models(Post, form_data, request)

            messages.success(request, f'Data added to the database')
            return render(request, 'form/home.html')
            #return HttpResponse(f"Recived patient name : {form_data.cleaned_data['patient_name']}")

    form_context = {
        'forms': clinical_form()
    }

    return render(request, 'form/form.html', form_context)

@login_required
def home_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/home.html')

def about_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/about.html')


def edit_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/edit.html')


'''

'''