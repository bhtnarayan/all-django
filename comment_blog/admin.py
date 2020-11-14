from django.contrib import admin
from . models import *
# Register your models here.

admin.site.site_header = "Blog Project"


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)