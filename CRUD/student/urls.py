from django.urls import path
from .views import index, action_handler
urlpatterns = [
    path('', index, name='home'),
    path('<str:action>/<int:id>/',action_handler)
]
