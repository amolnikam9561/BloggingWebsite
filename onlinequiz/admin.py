from django.contrib import admin

from bloggingapp.models import *
from onlinequiz.models import *
# Register your models here.

admin.site.register(Questions)
admin.site.register(UserDatabase)
