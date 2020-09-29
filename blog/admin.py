from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
   
   list_display = ('author', 'title', 'text', 'publishe_date')

   search_fields = ['author']
    
admin.site.register(Post, PostAdmin)
