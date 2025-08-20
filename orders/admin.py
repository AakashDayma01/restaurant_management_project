from django.contrib import admin
from .models import Menu , Order, OrderItem

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin,ModelAdmin):
    list_display = ("name","price","category")
    search_fields = ("name","category")
    list_filter = ('category',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('Id','customer','total','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ("customer__username",)
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','menu_item','quantity','subtotal')
    search_fields = ('menu_item__name','order__id')
    
