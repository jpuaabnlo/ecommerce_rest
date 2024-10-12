from django.db import models
from apps.base.models import BaseModel

'''from simple_history.models import HistoricalRecors'''

# Create your models here.
class MeasureUnit(BaseModel):
    description = models.CharField('Descripción', max_length = 50, blank = False, null = False, unique = True)


    '''
    historical=HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by
        
    @_history_user_setter
    def _history_user(self, value):
        self.changed_by = value'''
    
    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'
    
    def __str__(self):
        return self.description
    
    
class CategoryProduct(BaseModel):
    
    description = models.CharField('Descripción', max_length = 50, blank = False, null = False, unique = True)

    '''
    historical=HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by
        
    @_history_user_setter
    def _history_user(self, value):
        self.changed_by = value'''
    
    class Meta:
        verbose_name = 'Categoría del producto'
        verbose_name_plural = 'Categorías del producto'
    
    def __str__(self):
        return self.description
    
class Indicator(BaseModel):

    discount_value = models.PositiveSmallIntegerField(default = 0)
    category_product = models.ForeignKey(CategoryProduct, on_delete = models.CASCADE, verbose_name = 'Indicador')

    '''
    historical=HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by
        
    @_history_user_setter
    def _history_user(self, value):
        self.changed_by = value'''
    class Meta:
        verbose_name = 'Indicador de oferta'
        verbose_name_plural ='Indicadores de oferta'
    
    def __str__(self):
        return f'Oferta de la categoría{self.category_product} : {self.discount_value}%'
    
class Product(BaseModel):

    name = models.CharField('Nombre de producto',max_length = 155, null = False, blank = False, unique = True)
    description = models.TextField('Descripción del producto', blank = False, null = False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete = models.CASCADE, verbose_name = 'Unidad de medida', null = True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoría del producto', null = 'True')

    '''
    Imagen = models.ImageField('Imagen del producto, upload_to = 'products/', blank = True, null = True)
    historical=HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by
        
    @_history_user_setter
    def _history_user(self, value):
        self.changed_by = value'''
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.name
