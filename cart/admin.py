from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('total_price',)

# показывает все сессии 
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'total_items', 'subtotal', 'created_at',
                    'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('session_key',) # вот чисто чтобы не забыть
                                     # если кортеж с одним элементом - обязательно запятая в конце, иначе ошибка
    inlines = [CartItemInline]
    readonly_fields = ('total_items', 'subtotal')

# Какие товары находятся в корзине 
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'product_size', 'quantity',
                    'total_price', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('product__name', 'cart__session_key')
    readonly_fields = ('total_price',)
