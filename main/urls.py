from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('item/', views.item, name="item"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('create-item', views.create_item, name="create-item"),
    path('edit-item/<int:pk>', views.edit_item, name="edit-item"),
    path('delete-item/<int:pk>', views.delete_item, name="delete-item"),
    path('profilepage/', views.profilepage, name="profilepage"),

]
