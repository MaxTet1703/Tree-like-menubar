from django.urls import path

from .views import home, menu_topic

urlpatterns = [
    path('', home, name="home"),
    path('<slug:url>', menu_topic, name="menu")
]