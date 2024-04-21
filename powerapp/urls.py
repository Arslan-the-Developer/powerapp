from django.urls import path,include
from powerapp import views

urlpatterns = [
    path('',views.index,name="index")
]
