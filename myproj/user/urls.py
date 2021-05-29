from django.urls import path
from .views import Signup,Login,Home,logout
from .middlewares import LoginCheckMiddleware,LogoutCheckMiddleware
from.import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('signup',LogoutCheckMiddleware(Signup.as_view()), name='signup'),
    path('login',LogoutCheckMiddleware(Login.as_view()), name='login'),
    path('logout',LoginCheckMiddleware(logout), name='logout'),
    path('All_tasks',views.Show_task, name='tasks'),
    ]