from django.contrib import admin
from .models import Post


admin.site.site_header = "OBG Adminstration"
admin.site.site_title = "OBG Administration"

admin.site.register(Post)


