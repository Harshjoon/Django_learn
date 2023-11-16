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