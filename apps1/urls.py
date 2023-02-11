from django.urls import path
from .views import *

app_name = "demo1"

urlpatterns = [
    path('apps1/',LandingPage.as_view(),name='apps1'),
]

