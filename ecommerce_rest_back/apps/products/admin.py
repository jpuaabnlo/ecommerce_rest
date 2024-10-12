from django.contrib import admin
from apps.products.models import *

# Register your models here.

''' Esto sirve para mostrar en la pagina de admin
el id del producto y su descripcion.
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')'''

''' Esto sirve igual que lo anterior
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')'''

admin.site.register(MeasureUnit) 
''', MeasureUnitAdmin)'''
admin.site.register(CategoryProduct) 
''', CategoryProductAdmin)'''
admin.site.register(Indicator)
admin.site.register(Product)