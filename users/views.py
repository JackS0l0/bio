from django.shortcuts import render,redirect
from .froms import UserLoginForm
from django.contrib import auth
from django.views.generic import View
from main.models import İnfo
from django.contrib.auth import logout
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