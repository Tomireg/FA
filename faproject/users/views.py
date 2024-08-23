from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #Added import here
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully, now you can login.')
            return redirect('login') 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    #Create instances of the forms.
    u_form = UserUpdateForm 
    p_form = ProfileUpdateForm

    #Create a context dictionary to pass into the template. The keys are the variables
    #we will access in our template
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context) #Context passed here