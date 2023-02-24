from django.contrib import admin
from user_management import models


@admin.register(models.MainUser)
class MainUserAdmin(admin.ModelAdmin):
    pass
