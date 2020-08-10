from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'tms'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('register/', views.register, name='register'),

    path('product_list/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('contact.html', views.contact, name='contact'),
]