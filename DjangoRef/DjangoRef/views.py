from django.shortcuts import render, redirect
from Profile.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse


def SignUp(request):
    profile_id = request.session.get('ref_profile')
    temp = 'signUp.html'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if profile_id:
                recommended_by = Profile.objects.get(id=profile_id)
                instance = form.save()
                registered_user = User.objects.get(id=instance.id)
                registered_profile =  Profile.objects.get(user=registered_user)
                registered_profile.recommended_by = recommended_by.user
                registered_profile.save()
                return redirect('main_urls')
            else:
                form.save()
    context = {'forms': form}
    return render(request, temp, context)


def login_view(request):
    temp = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('main_urls')
    return render(request,temp,{})


def logout_view(request):
    logout(request)
    return redirect('main_urls')





def main_view(request):
    temp = 'main.html'
    code = request.GET.get('ref_code')
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
    except:
        pass
    context = {}
    return render(request, temp, context)