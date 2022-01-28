from pyexpat import model
from django.contrib import admin
from .models import Author
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class AuthorAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin) 