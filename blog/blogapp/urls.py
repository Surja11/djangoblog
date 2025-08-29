from django.urls import path
from . import views

urlpatterns = [
  path('',views.home, name = "home"),
  path('login/', views.loginView, name = "login"),
  path('logout/', views.logoutUser, name = "logout"),
  path('register/', views.register, name = "register"),
  path('createPost/', views.CRUDPost.as_view(), name= "createPost"),
  path('yourblogs/', views.yourblogs, name = "yourblogs"),
  path('readblog/<id>',views.readBlog,name="readblog"),
  path('editblog/<id>/',views.editBlog,name="editblog"),
  path('deleteblog/<id>/',views.deleteBlog, name="deleteblog")
]