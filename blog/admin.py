from django.contrib import admin
from . models import Category, Tag , Post 

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    list_display = ("title", "category", "status", "date", "get_tags")
    
    list_filter = ("category", "status", "date")
    
    search_fields = ("title", "content")
    
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tag.all()])
    
    get_tags.short_description = 'Etiquetas'
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "total_posts")
    
    prepopulated_fields = {"slug": ("name",)}
    
    ordering = ("name",)
    
    def total_posts(self, obj):
        return Post.objects.filter(category=obj).count()
    
    total_posts.short_description = "Total de posts"
    
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "total_posts")
    
    prepopulated_fields = {"slug": ("name",)}
    
    ordering = ("name",)
    
    def total_posts(self, obj):
        return obj.post_set.count()
    
    total_posts.short_description = "Total de posts"



admin.site.site_title = "Panel Administrativo del Blog"
admin.site.site_header = "Administracion del Blog"
admin.site.index_title = "Panel principal del Blog"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
