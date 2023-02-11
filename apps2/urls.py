from django.urls import path
from .views import *

app_name = "demo2"

urlpatterns = [
    path('apps2/',LandingPage.as_view(),name="apps2"),

]