from django.urls import path
from .views import SignupPageView

url_patterns = [
    path('signup/', SignupPageView.as_view(), name="signup"),
]
