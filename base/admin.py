from django.contrib import admin

# Register your models here.
from base.models import Contact
from base.models import Post

admin.site.register(Contact)
admin.site.register(Post)