from django.shortcuts           import render, redirect
from django.contrib.auth.decorators     import login_required
#from django.contrib.auth.forms  import UserCreationForm
from django.contrib             import messages
from .forms                     import UserRegisterForm

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email  = form.cleaned_data.get('email')
            organisation = email.split("@")[1]

            if organisation != "ssinnovations.org":
                messages.warning(request, "Only ssinovations email is allowd.")
                return redirect('register')
            
            from django.contrib.auth.models import User
            if len( User.objects.all().filter(email=email) ) != 0:
                messages.warning(request, "Email already exists use different email.")
                return redirect('register')

            print("email--------",email)
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
            #return redirect('form-home')            
    else:
        #form    = UserCreationForm()
        form    = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form} ) 

@login_required
def profile(request):
    return render(request, 'users/profile.html')

