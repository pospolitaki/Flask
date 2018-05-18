from django.contrib import admin

from pizza_app.models import Address, PizzaOrder

# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'full', )

class PizzaOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'kind', 'size','user')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.author = request.user
        obj.save()



# PizzaIngredient
# PizzaMenuItem
# PizzaSize
# PizzaOrder

# list_display
# search
#

admin.site.register(Address, AddressAdmin)
admin.site.register(PizzaOrder, PizzaOrderAdmin)
