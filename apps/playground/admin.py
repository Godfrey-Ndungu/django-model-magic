from django.contrib import admin
from .models import SampleModelWithAllFields


class SampleModelWithAllFieldsAdmin(admin.ModelAdmin):
    pass


admin.site.register(SampleModelWithAllFields, SampleModelWithAllFieldsAdmin)
