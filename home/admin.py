from django.contrib import admin
from .models import Contact, Newsletter, Profile

# Change Django Administration default name
admin.site.site_header = "Coding Easy Administration"
admin.site.site_title = "Coding Easy Administration site"
admin.site.index_title = "Dashboard"
# Register the model
admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Profile)
