"""
URL configuration for BloggingWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bloggingapp.views import *
from onlinequiz.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home),
    path('givemelogin/',givemelogin),
    path('givemeregister/',givemeregister),
    path('register/',register),
    path('login/',login),
    path('errorpage',errorpage),
    path('blogpage',blogpage),
    # path('givemeadminaccess/',give_me_admin_access),
    path('question_management/',question_management),
    path('addQuestion/',addQuestion),
    path('viewQuestion/',viewQuestion),
    path('deleteQuestion/',deleteQuestion),
    path('updateQuestion/',updateQuestion),
    path('givemeuserregister/',givemeuserregister),
    path('userregistration/',userregister),
    path('givemeuserlogin/',givemeuserlogin),
    path('userlogin/',userlogin),
    path('givemeadminregister/',givemeadminregister),
    path('adminregister/',adminregister),
    path('givemeadminlogin/',givemeadminlogin),
    path('adminlogin/',adminlogin),
    path('student_dashboard/',student_dashboard),
    path('question_navigation/',question_navigation),
    path('nextQuestion/',nextQuestion),
    path('previousQuestion/',previousQuestion),
    path('endexam/',endexam),
    path('starttest/',startTest),
    path('admin_dashboard/',admin_dashboard),
    path('student_results/',student_results),
    path('question_management/',question_management),

]
