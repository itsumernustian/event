from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index1, name="index"),
    path("sign_in", views.sign_in, name="sign_in"),
    path("register", views.registration, name="register"),
    path("createEvent", views.createEvent, name="createEvent"),
    path("eventdetails", views.eventdetails, name="eventdetails")
]
