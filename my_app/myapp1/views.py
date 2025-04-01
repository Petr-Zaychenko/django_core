from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .services import AuthService, FileService


def page(request):
    context = {
        "all_files": FileService.get_all_files()
    }
    return render(request, "index.html", context)


def delete_file(request, file_id):
    if FileService.delete_file(file_id):
        return HttpResponseRedirect("/")
    return HttpResponseNotFound("Файл не найден")


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if AuthService.login_user(request, username, password):
            return redirect('good_job')
    return render(request, "login.html")


def user_logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('page')


def add_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        FileService.add_file(request.FILES['file'], request)
        return redirect('page')
    return render(request, "add_file.html")


def good_job(request):
    return render(request, "good_job.html")


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        user = AuthService.register_user(request, email, password, password2)
        if user:
            return redirect('page')

    return render(request, "register.html")