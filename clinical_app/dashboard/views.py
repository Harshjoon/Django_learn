from django.shortcuts import render
from django.contrib.auth.decorators     import user_passes_test , login_required
from django.contrib             import messages
from django.http                import HttpResponseRedirect
from django.shortcuts           import redirect

def check_admin(user):   
   return user.is_superuser


#@user_passes_test(check_admin)
@login_required
def home_page(request):
    print("-----------------------------")
    if request.user.is_superuser:
        return render(request, "dashboard/home.html")
    else:
        messages.warning(request, "Only admins can access dashboard")
        return redirect('login', name="dashboard-home")