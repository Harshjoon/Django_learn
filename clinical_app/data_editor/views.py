from django.shortcuts import render
from django.contrib.auth.decorators     import user_passes_test , login_required
from django.contrib             import messages
from django.http                import HttpResponseRedirect
from django.shortcuts           import redirect
#from .models                    import edit_hospitals
from .forms                     import EditHospitalsForm
from form.models                import Hospitals
#from form.models                import Hospitals
from .functions                 import edit_hospitals

def check_admin(user):   
   return user.is_superuser

#@user_passes_test(check_admin)
# @login_required
# def home_page(request):
#     print("-----------------------------")
#     if request.user.is_superuser:
#         return render(request, "data_editor/home.html")
#     else:
#         messages.warning(request, "Only admins can access dashboard")
#         return redirect('login', name="dataeditor-home")
    
@login_required
def home_page(request):

    if request.user.is_superuser:
        if request.method    == 'POST':
            print("request post sent.")

            form_data       = EditHospitalsForm(request.POST)

            if form_data.is_valid():

                edit_hospitals(Hospitals, form_data, request)
                messages.success(request, f'Hospital data edited.')
                return redirect("form-home")

        form_context = {
            "hospital_form": EditHospitalsForm()
        }
        return render(request, "data_editor/edit_format.html", form_context)
        
    else:
        messages.warning(request, "Only admins can access dashboard")
        return redirect('login', name="dataeditor-home")