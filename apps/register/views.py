from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User

def index(request):
    return render(request, 'Projectpage1.html')


def main(request):
    return render(request, 'Projectpage3.html')

def contact(request):
    return render(request, 'Projectpage7.html')

def review(request):
    return render(request, 'Projectpage5.html')

def about(request):
    return render(request, 'Projectpage4.html')

def logout(request):
    return render(request, 'Projectpage8.html')

def moviedesc(request):
    return render(request, 'Projectpage6.html')

def moviesee(request):
    return render(request, 'Projectpage9.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf8'), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/Regconf')

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        hashed_password = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt())
        if (bcrypt.checkpw( user.password.encode('utf8'),hashed_password)):
            request.session['id'] = user.id
            return redirect('/Main')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'Projectpage1.html', context)

def regconf(request):
    return render(request, 'Projectpage2.html')
