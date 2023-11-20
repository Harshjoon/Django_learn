from django.shortcuts       import render
from django.views.generic   import ListView
from django.http            import HttpResponse
from .models                import Post
from .forms                 import clinical_form
from .functions             import set_models, set_forms
from django.contrib.auth.decorators     import login_required
from django.contrib             import messages
from django.shortcuts           import redirect
from django.urls            import reverse
from urllib.parse           import urlencode

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
def forms_page(request):#, patien_id=None):

    patient_id      = request.GET.get('patient_id')

    if request.method == 'POST':
        form_data = clinical_form(request.POST)
        if form_data.is_valid():
            set_models(Post, form_data, request)
            messages.success(request, f'Data added to the database')
            #return render(request, 'form/home.html')
            return redirect("form-home")
            #return HttpResponse(f"Recived patient name : {form_data.cleaned_data['patient_name']}")

    if patient_id is not None:
        # change form data from models
        post            = Post.objects.all().filter( patient_id=patient_id )
        form_data       = clinical_form(instance=post.first())

        form_context = {
            'forms': clinical_form(instance=post.first())#form_data
        }

        print(post.first().instrument_test)

        return render(request, 'form/form.html', form_context)

    form_context = {
        'forms': clinical_form()
    }
    return render(request, 'form/form.html', form_context)

@login_required
def home_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    if request.method == "POST":
        patient_id = request.POST['patient_id']
        print(patient_id)
        from form.models import Post
        #post = Post.objects.get(patient_id=patient_id)
        post        = Post.objects.all().filter( patient_id=patient_id )
        if len(post) == 0:
            messages.warning(request, "Patient ID does not exits.")
        else:
            base_url            = reverse('form-form')
            query_string        = urlencode({'patient_id': patient_id})
            url                 = '{}?{}'.format(base_url, query_string)
            return redirect(url)        
    return render(request, 'form/home.html')

def about_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/about.html')

def edit_page(request):
    #return HttpResponse('<h1>Form page</h1>')
    return render(request, 'form/edit.html')

'''
            # hospital_name   = form_data.cleaned_data['hospital_name']
            # patient_name    = form_data.cleaned_data['patient_name']
            # post            = Post(
            #     hospital_name = hospital_name,
            #     patient_name  = patient_name
            # )                        
            # post.author = request.user
            # post.save()

            ########### TEST ONLY #############

            form_obj        = clinical_form(instance=post.first())

            #return render(request, 'form/form.html', {'forms': form_obj} )

            #return redirect('form-form', {'form_context':form_obj})
            #return redirect('form-form', form_context=[form_obj])
            #return redirect('form-form', form_context=None)
            #return reverse('form-form', args=(form_obj,))

            ##################################

            # form_data = set_forms( clinical_form ,post )
            # print(type(form_data))
            # print("redired to form page with form data.")
            # #return redirect("form-home")  
            

            #return redirect("form-form", query_string)#patien_id='1')#, kwargs={"form_context": form_obj} )
            # return render(request, 'form/form.html', {'forms': form_data} )
'''