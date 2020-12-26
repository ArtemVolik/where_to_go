from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(admin.TabularInline, SortableInlineAdminMixin):
    model = Image
    readonly_fields = ('image_preview',)
    fields = ('image', 'image_preview', 'image_order')

    def image_preview(self, obj):
        return format_html('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height=200,
            )
        )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )



admin.site.register(Image)

