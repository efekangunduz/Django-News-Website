from django.contrib import admin

# Register your models here.
from new.models import Category, New, Images


class NewImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class NewAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'image_tag', 'status']
    list_filter = ['status', 'category']
    inlines = [NewImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['new', 'title', 'image_tag']
    list_filter = ['new']


admin.site.register(Category, CategoryAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Images, ImagesAdmin)
