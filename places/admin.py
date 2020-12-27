from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


def image_preview(obj):
    """Return preview Image object."""
    return format_html('<img src="{url}" height={height} />'.format(
        url=obj.image.url,
        height=200
        )
    )


class ImageTabularInline(SortableInlineAdminMixin, admin.TabularInline):
    """Related images for the Place object page."""

    model = Image
    readonly_fields = ('image_preview',)
    fields = ('image_order', 'image', 'image_preview', )
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    """Show and edit related images on Place object page."""

    inlines = (ImageTabularInline,)
    search_fields = ['title']


admin.site.register(Image)
