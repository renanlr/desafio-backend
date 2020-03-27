from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root),
    path('trips/', views.TripList.as_view(), name='trip-list'),
    path('trips/<int:pk>/', views.TripDetail.as_view(), name='trip-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
