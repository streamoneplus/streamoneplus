from django.contrib import admin
from .models import Video, IpAddress, Category, Comments

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):   
     list_display = ['title', 'slug', 'video', 'author', 'publish', 'status', ]
     list_filter = ['status', 'created', 'publish', 'author', 'category' ]  
     search_fields = ['title', 'category'] 
     prepopulated_fields = {'slug': ('title',)}  
     raw_id_fields = ['author']  
     date_hierarchy = 'publish' 
     ordering = ['status', 'publish']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):   
     list_display = ['title', ]
     list_filter = ['title',  ]  
     search_fields = ['title'] 
    
@admin.register(IpAddress)
class IpAddressAdmin(admin.ModelAdmin):   
     list_display = ['ip' ]
     
@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name',  'video', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name',  'body')     
     
