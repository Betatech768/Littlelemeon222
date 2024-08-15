from django.urls import path
from . import views

urlpatterns = [
    path('adminlogin/', views.loginPage, name = "login_page"),
    path('logout/', views.logoutUser, name = "logout_page"),
    path('', views.home, name = "home"),
    path('menu/', views.menu, name = "menu"),
    path('about/', views.about, name= "about"),
    path('adminportal/', views.adminportal, name = "admin"),
    path('createMenu/', views.createMenu, name = "create_menu"),
    path('updateMenu/<str:pk>/', views.updateMenu, name = "update_menu"),
    path('deleteMenu/<str:pk>/', views.deleteMenu, name = "delete_menu"),
    path('createCategory/', views.createCategory, name = "create_cat"),
    path('createBooking/', views.createBooking, name = "create_book"),
    path('Thanks/', views.Thanks, name = "thanks"),
    path('updateCat/<int:pk>/', views.updateCat, name = "update_cat"),
    path('deleteCategory/<str:pk>/', views.deleteCategory, name = "delete_cat"),
    path('deleteBooking/<str:pk>/', views.deleteBooking, name = "delete_book"),
    path('Booklist/', views.Booklist, name = "book_list"),
    path('createUser/', views.createUser, name = "create_user"),
    path('menuDescription/<str:pk>/', views.menuDescription, name = "menu_description"),
    path('createOrder/', views.createOrder, name = "order"),
    path('deleteUser/<str:pk>/', views.deleteUser, name = "delete_user"),
    path('OrderList/<str:pk>/', views.OrderList, name = "order_list"),
    
    
    
]

