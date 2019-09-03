from django.contrib import admin
from image.models import Image
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('user','title','url','slug','description','created','image' )
    list_filter = ("user",)
admin.site.register(Image,ImageAdmin)

