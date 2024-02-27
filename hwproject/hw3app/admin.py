from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Товар закончился")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(product_quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['name', 'price', 'product_quantity', 'product_added']
    ordering = ['price']
    list_filter = ['product_added']
    search_fields = ['name']
    search_help_text = ['Поиск по полю - имя продукта (name)']
    actions = [reset_quantity]

    """Отдельный продукт"""
    # fields = ['name', 'price', 'product_quantity', 'product_added', 'description']
    readonly_fields = ['product_added']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                        'fields':['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'product_quantity'],
            }
        ),
        (
            'Прочее',
            {
                'description': 'Картинку можно поменять',
                'fields': ['image', 'product_added'],
            }
        ),
    ]


class ClientAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'phone_number', 'registration_date', 'email']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)

# Register your models here.
