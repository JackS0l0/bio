from django.shortcuts import render,redirect
from .froms import UserLoginForm,CreateUser
from django.contrib import auth
from django.views.generic import View
from main.models import İnfo
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def index(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('home/')
    else:
        form = UserLoginForm()
    data={
        'title': 'Biologiya - Quliyeva Suqra',
        'form': form,
        'info':İnfo.objects.all()[0:1],
    }
    return render(request,'index.html',data)
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
@login_required
def signup(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, 'İstifadəçi yaradıldı')  # Add success message
            form = CreateUser()  # Reset the form for further entries
    else:
        form = CreateUser()

    data = {
        'title': 'Biologiya - Quliyeva Suqra - Signup',
        'form': form,
    }
    return render(request, 'create.html', data)