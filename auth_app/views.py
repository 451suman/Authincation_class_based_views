from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'



class SignupView(View):
    template_name = 'registration/signup.html'

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to home after successful signup
        else:
            return render(request, self.template_name, {'form': form})  # Re-render form with errors if not valid

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})




