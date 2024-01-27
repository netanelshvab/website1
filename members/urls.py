from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('members/', views.memberss, name='members'),
    path('home/', views.WEBSITEhome, name='home'),
    path('home/about-me', views.about_me, name='about-me'),
    path('', RedirectView.as_view(url='/home/')),  # Redirects the root URL to '/home/'
    path('members/details/<int:id>', views.details, name='details'),
    path('product/<int:id>', views.details, name='details'),

]