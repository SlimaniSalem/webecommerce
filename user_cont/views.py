from django.contrib.auth import get_user_model,login
from django.shortcuts import render, redirect

User = get_user_model()
def user_log(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            return render(request, 'inscription.html', {'username': username})
        else:
             user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index')

    return render(request,'inscription.html')

