from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('category/<category_slug>/', views.HomePage.as_view(), name='category_filter'),
    path('detail/<product_slug>', views.ProductDetailView.as_view(), name='detail')
]
