from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageTabularInline(SortableInlineAdminMixin, admin.TabularInline):
    """Related images for the Place object page."""

    model = Image
    readonly_fields = ('image_preview',)
    fields = ('image_order', 'image', 'image_preview', )
    extra = 0

    def image_preview(self, obj):
        try:
            image_preview = format_html('<img src="{}" height={} />',
                               mark_safe(obj.image.url),
                               200)
            return image_preview
        except ValueError:
            return 'Картинка еще не загружена'



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    """Show and edit related images on Place object page."""

    inlines = (ImageTabularInline,)
    search_fields = ['title']


admin.site.register(Image)
