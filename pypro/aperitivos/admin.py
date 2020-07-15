from django.contrib.admin import ModelAdmin
from django.contrib.admin import register

from pypro.aperitivos.models import Video


@register(Video)
class AperitivosAdmin(ModelAdmin):
    list_display = ['titulo', 'slug', 'creation', 'vimeo_id']
    ordering = ['creation']
    prepopulated_fields = {'slug': ('titulo',)}
