from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="homepage"),
    path('about-us/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
]