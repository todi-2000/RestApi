from django.urls import path,include
from . import views


urlpatterns = [
    path('cal/',views.Calc.as_view())
]