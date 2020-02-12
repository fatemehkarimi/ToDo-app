from django.urls import path
from .views import HomePageView, ToDo_objCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('todo/new', ToDo_objCreateView.as_view(), name='todo_new'),
]
