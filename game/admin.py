from django.contrib import admin

from .models import *

# Register your models here.


class SceneAdmin(admin.ModelAdmin):
    list_display=('Name','pub_date','id')
    #filter_horizontal = ('NextScenes',)
    search_fields=['pub_date','id']

admin.site.register(Scene,SceneAdmin)
admin.site.register(Scene_picture)
admin.site.register(Scene_text)
admin.site.register(Turning_point)
