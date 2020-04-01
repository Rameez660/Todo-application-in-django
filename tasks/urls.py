from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
	path('print/<str:pk>/', views.printTask, name="print"),
	path('login/',views.login,name="login"),
    path('logout/',views.handlelogout,name='handlelogout')




]