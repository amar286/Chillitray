from django.shortcuts import render,redirect, HttpResponseRedirect
from.models import *
from django.views import View
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator

class Signup(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        userData = request.POST
        # validate
        error = self.validateData(userData)
        if error:
            return render(request, 'signup.html', {"error": error, "userData": userData})
        else:
            if User.userExits(userData['username']):
                error["userExits_error"] = "User Already Exits"
                return render(request, 'signup.html', {"error": error, "userData": userData})
            else:
                usr = User(
                    username=userData['username'],
                    password=make_password(userData['password']),
                )
                usr.save()
                return redirect('home')
    # Validate form method
    def validateData(self, userData):
        error = {}
        if not userData['username'] or not userData['password'] or not \
        userData['confirm_password']:
            error["field_error"] = "All field must be required"
        elif len(userData['password']) < 8 and len(userData['confirm_password']) < 8:
            error['minPass_error'] = "Password must be 8 char"
        elif len(userData['username']) > 25 or len(userData['username']) < 3:
            error["name_error"] = "Name must be 3-25 charecter"

        elif userData['password'] != userData['confirm_password']:
            error["notMatch_error"] = "Password doesn't match"

        return error


class Login(View):
    return_url = None

    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request,'login.html')

    def post(self,request):
        userData = request.POST
        username = User.emailExits(userData["username"])

        if username:
            if check_password(userData["password"],username.password):
                request.session["username"] = username.u_id
                print(username.u_id)

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                return render(request,'login.html',{"userData":userData,"error":"username or password doesn't match"})
        else:
            return render(request,'login.html',{"userData":userData,"error":"Email or password doesn't match"})

def Home(request):
    usr = request.session.get('username')
    return render(request, 'home.html',{'usr':usr})


def logout(request):
	request.session.clear()
	return redirect('home')


def Show_task(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 5)
    page = request.GET.get('page')
    alltask = paginator.get_page(page)
    return render(request, 'All_tasks.html',{'task':alltask})