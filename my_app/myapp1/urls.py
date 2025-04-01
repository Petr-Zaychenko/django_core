from django.urls import path
from . import views

urlpatterns = [
    path('', views.page, name='page'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_file/', views.add_file, name='add_file'),
    path('good_job/', views.good_job, name='good_job'),
    path('register/', views.register, name='register'),

]
