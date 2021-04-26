from django.contrib import admin
from core import models
from core import forms


admin.site.register(models.OrganizationMetod)
admin.site.register(models.Staff)
admin.site.register(models.StaffCategory)
admin.site.register(models.Regulations)
admin.site.register(models.District)
admin.site.register(models.Udo)
admin.site.register(models.UnionInteres)
admin.site.register(models.UnionInteresProfile)
# admin.site.register(models.User)


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'first_name', 'last_name', 'patronymic', 'position',
              'is_staff', 'is_superuser']
    form = forms.UserAdminForm
