from django.contrib import admin
from .models import Problem, myUser, Solution
from django.contrib.auth.admin import UserAdmin

admin.site.register(Solution)
admin.site.register(Problem)
admin.site.register(myUser, UserAdmin)