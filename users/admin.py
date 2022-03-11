from django.contrib import admin
from .models import Profile

# Change Django Administration default name
admin.site.site_header = "Coding Easy Administration"
admin.site.site_title = "Coding Easy Administration site"
admin.site.index_title = "Dashboard"
# Register the model
admin.site.register(Profile)
