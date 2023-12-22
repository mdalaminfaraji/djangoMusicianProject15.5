# musicians/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('musicians_table/', views.musicians_table, name='musicians_table'),
    path('edit_musician/<int:musician_id>/', views.edit_musician, name='edit_musician'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
   
]
