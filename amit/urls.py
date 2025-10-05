
from django.urls import path
from . import views

# localhost1:8000/amit
# localhost1:8000/amit/order
urlpatterns = [
    path('',views.amit,name='amit'),
    # path('order/',views.order,name='order')
]
