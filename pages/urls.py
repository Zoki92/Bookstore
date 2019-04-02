from django.urls import path
from .views include HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
]
