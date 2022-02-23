from django.shortcuts import render, redirect
# from .models import Register
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
from .forms import RegisterForm
# Create your views here.

def home(request):
    template = 'api/index.html'
    return render(request, template)

# def register(request, CreateView):
#     # if request.method == 'POST':
#     #     username = request.POST.get('username')
#     #     first_name = request.POST.get('first_name')
#     #     last_name = request.POST.get('last_name')
#     #     email = request.POST.get('email')
#     #     password = request.POST.get('password')
#     #     address = request.POST.get('address')
#     #     city = request.POST.get('city')
#     #     state = request.POST.get('state')
#     #     zip_code = request.POST.get('zip_code')
#     #     country = request.POST.get('country')
        
#     form_class = CustomUserCreationForm
#     # success_url = reverse_lazy('login')
    
#     template = 'api/register.html'
#     return render(request, template)

# class register(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'api/register.html'


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
        
    else:
        form = RegisterForm()
        
    return render(response, "api/register.html", {"form":form})