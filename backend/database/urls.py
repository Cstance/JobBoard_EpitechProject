from django.urls import path
from database import views

urlpatterns = [
    path('users/', views.UserRequests().all),
    path('users/<int:pk>/', views.UserRequests().single),
    path('users/<int:pk>/', views.UserRequests().single),
    path('users/type/', views.isAdvertiser),
    path('users/info/', views.getInformation),
    path('companies/', views.CompanyRequests().all),
    path('companies/<int:pk>/', views.CompanyRequests().single),
    path('advertisements/', views.AdvertisementRequests().all),
    path('advertisements/<int:pk>/', views.AdvertisementRequests().single),
    path('applications/', views.ApplicationRequests().all),
    path('application/<int:pk>/', views.AdvertisementRequests().single)

]