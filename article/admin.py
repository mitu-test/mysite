from django.contrib import admin
from article.models import ArticleColumn,ArticlePost
# Register your models here.
class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('user','column','created')
    list_filter = ("column",)
admin.site.register(ArticleColumn,ArticleColumnAdmin)

class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ('author','title','slug','column','body','created','updated')
    list_filter = ("author",)
admin.site.register(ArticlePost,ArticlePostAdmin)


