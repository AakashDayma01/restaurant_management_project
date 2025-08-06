from django.contrib import admin
from .models import Item, Order, OrderItem


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']
    search_fields = ['item_name']
    list_filter = ['created_at']
    ordering = ['-created_at']

#inline for showing Orderitems inside the Order admin page
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['item','quantity']
    can_delete = False

#Custom Admin for Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer','total_amount','status','created_at']
    list_filter = ['status','created_at']
    search_fields = ['customer__username']
    readonly_fields = ['total_amount','created_at']
    inline = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','item','quantity']
    search_fields = ['order__id','item__item_name']

# Register your models here.
admin.site.register(Item,ItemAdmin)
