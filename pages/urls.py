from django.urls import path
from .views import HomePageView, ToDo_objCreateView, ToDo_objUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('todo/new', ToDo_objCreateView.as_view(), name='todo_new'),
    path('todo/update/<int:pk>/',
        ToDo_objUpdateView.as_view(), name='todo_update'),
]
