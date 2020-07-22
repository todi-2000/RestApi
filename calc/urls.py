from django.urls import path,include
from . import views


urlpatterns = [
    path('calc/',views.Calc.as_view())
]