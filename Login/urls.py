
from django.contrib import admin
from django.urls import path
from TodoList.views import(DisplayTodos,DeleteTodo,SetMark,UnMark,add_todo,update_todo)
from registeruser.views import(registerUserView, loginView, logOutView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DisplayTodos,name='home'),
    path('delete/<pk>/',DeleteTodo ),
    path('mark/<pk>/',SetMark ),
    path('unmark/<pk>/',UnMark ),
    path('add-todo/',add_todo ),
    path('update/<pk>/',update_todo ),


    path('register', registerUserView ,name='register'),
    path('login/', loginView,name='login'),
    path('logout/', logOutView,name='logout'),
]
