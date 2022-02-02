from django.contrib import admin

# Register your models here.
from base.models import Contact, Event, Post

admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Event)