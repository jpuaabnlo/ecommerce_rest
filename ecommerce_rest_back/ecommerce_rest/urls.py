from django.contrib import admin
from django.urls import path, include
from apps.users.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('usuario/', include('apps.users.api.urls')),
    path('products/', include('apps.products.api.routers'))
    
]
