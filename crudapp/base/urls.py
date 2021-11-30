from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('insert',views.insertData, name="insertData"),
    path('edit/<id>',views.editData, name="editData"),
    path('delete/<id>',views.deleteData, name="deleteData"),
]
