from django.urls import path
from .views import MemoryView

urlpatterns = [
    path('memory', MemoryView.as_view(), name='memory'),
]
