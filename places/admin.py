from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageTabularInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ('image_preview',)
    fields = ('image_order', 'image', 'image_preview', )
    extra = 0

    def image_preview(self, obj):
        return format_html('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height=200
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImageTabularInline,)


admin.site.register(Image)

