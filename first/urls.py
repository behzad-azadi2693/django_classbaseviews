from django.urls import path
from . import views


app_name='first'

urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
    path('index/', views.Index.as_view(), name = 'index'),
    path('todo-list/', views.TodoListView.as_view(), name = 'todo-list'),
    path('todo-detail/<slug:myslug>', views.TodoDetailView.as_view(), name='todo-detail'),
    path('todo-create/>', views.TodoCreate.as_view(), name='todo-create'),
    path('todo-delete/<int:pk>/', views.TodoDelete.as_view(), name='todo-delete'),
    path('todo-update/<int:pk>/', views.TodoUpdate.as_view(), name='todo-update'),
    path('<int:year>/<int:month>/', views.MonthTodo.as_view(), name = 'month')<
]