from django.shortcuts import render ,redirect
from .forms import UserRegistrationForm ,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request , f'Added successfully {username}!')
            return redirect('Login')
    else:
        form=UserRegistrationForm()
    return render(request , "users/registers.html" , {"form":form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form=UserUpdateForm(request.POST ,instance=request.user)
        p_form=ProfileUpdateForm(request.POST , request.FILES ,
                                 instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , "You updated your profile")
            return redirect('Profile')
    else:
        u_form = UserUpdateForm( instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request , "users/profile.html",context)