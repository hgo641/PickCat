from django.contrib import admin
from .models import *

# Register your models here.


class InlineImage(admin.TabularInline):
    model = CatPhoto


class CatPostAdmin(admin.ModelAdmin):
    inlines = [InlineImage, ]
    list_display = (
        'title',
        'createdAt',
        'updatedAt'
    )

class InlineCat(admin.TabularInline):
    model = Cat


class KitchenAdmin(admin.ModelAdmin):
    inlines = [InlineCat, ]
    list_display = (
        'name',
        'address',
        'registeredAt',
    )


class CatAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'registeredAt',
    )
    list_display_links = (
        'name',
    )

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'nickname',
        'email',
        'date_joined'
    )
    list_display_links = (
        'nickname',
        'email'
    )


admin.site.register(CatPost, CatPostAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Cat, CatAdmin)
admin.site.register(Kitchen, KitchenAdmin)
admin.site.register(ImageTest)
