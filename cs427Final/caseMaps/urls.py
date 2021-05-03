from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('chloropleth/', views.chloropleth, name='chloropleth'),
    path('histograms/', views.histograms, name='histograms'),
    path('histograms/ajax/get_demographic/<str:demographic>', views.ajax_histograms, name='ajax_histograms'),
    path('regression/', views.regression, name='regression'),
]