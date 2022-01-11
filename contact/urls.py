from django.urls import path, include
from .views import ContactView

urlpatterns = [
    path('', ContactView.as_view())
]
