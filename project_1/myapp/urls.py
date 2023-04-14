from django.urls import path
from . import views


## domain.com/myapp/
urlpatterns = [
    path('home',views.index,name='index_name')
]