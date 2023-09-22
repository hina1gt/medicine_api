from django.urls import *
from .views import *

urlpatterns = [
    path('client/', ClientAPI.as_view(), name='client'),
    path('client/<int:pk>/', ClientDetailAPI.as_view(), name='client_detail'),
    path('sponsor/', SponsorAPI.as_view(), name='sponsor'),
    path('sponsor/<int:pk>/', SponsorDetailAPI.as_view(), name='sponsor_detail'),
    path('blog/', BlogAPI.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailAPI.as_view(), name='blog_detail'),
]