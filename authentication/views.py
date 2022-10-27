from django.shortcuts import redirect, render
from .forms import SignupForm
from django.views import View


class SignupPage(View):
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        return render(request, 'create_artist.html', {'form': form})

    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})