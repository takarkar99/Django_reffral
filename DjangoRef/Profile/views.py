from django.shortcuts import render
from .models import Profile


def my_recommended_view(request):
    temp = 'profile.html'
    print(request.user)
    profile = Profile.objects.get(user=request.user)
    li = profile.get_recommended_profiles()
    context = {'li':li}
    return render(request, temp, context)