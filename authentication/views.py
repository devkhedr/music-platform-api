from django.shortcuts import redirect, render
from .forms import sign_up_form
from django.views import View


class signup_page(View):
    def post(self, request):
        form = sign_up_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        return render(request, 'create_artist.html', {'form': form})

    def get(self, request):
        form = sign_up_form()
        return render(request, 'signup.html', {'form': form})