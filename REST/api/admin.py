from django.contrib import admin
from api.models import branches
from import_export.admin import ImportExportMixin

# Register your models here.

class BranchesAdmin(ImportExportMixin,admin.ModelAdmin):
    pass

admin.site.register(branches,BranchesAdmin)