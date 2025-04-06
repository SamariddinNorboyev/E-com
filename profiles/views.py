from django.shortcuts import render, redirect
from django.views import View
from .models import Profile
from .forms import ProfileUpdateForm
# Create your views here.
class ProfileUpdateView(View):
    def get(self, request):
        user = request.user
        profile = Profile.objects.filter(user = user).first()
        form = ProfileUpdateForm(instance=profile)
        return render(request, 'profiles/profiles.html', {'form':form})
    def post(self, request):
        user = request.user
        profile = Profile.objects.filter(user = user).first()
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        form = ProfileUpdateForm(instance=profile)
        return render(request, 'profiles/profiles.html', {'form':form})