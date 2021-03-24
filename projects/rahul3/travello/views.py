from django.shortcuts import render,redirect
from . models import Destination
from django.contrib.auth.models import User,auth




def index(request):
      
    dests =  Destination.objects.all()
    

    return render( request, "index.html", {'dests': dests})
    
'''
def registers(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('Username taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User created')
                return redirect('login')
        else:
            print('password is not mateching')
        return redirect('/')
    else:
        return render(request, "registers.html")    


'''



    




         