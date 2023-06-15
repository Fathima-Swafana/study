
from django.urls import path
from . import views
app_name='collegestoreapp'
urlpatterns = [

    path('',views.index,name="index"),



]