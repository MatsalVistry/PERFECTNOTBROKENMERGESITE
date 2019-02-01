from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$',views.signup_view, name ="signup"),
    url(r'^loginpage/$',views.loginpage_view,name="loginpage"),
]