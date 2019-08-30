
from django.contrib import admin
from django.urls import path
from crud import views
from crud.controllers import ProductController
urlpatterns = [
    path('',views.home,name='home'),
    path('product',ProductController.home,name='ProductHome'),
    path('product/add',ProductController.add,name='ProductAdd'),
    path('admin/', admin.site.urls),
]
