from django.urls import path
from .views import HomePageView, AboutPageView, ListPageView
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("list/", ListPageView.as_view(), name="list"),
]
