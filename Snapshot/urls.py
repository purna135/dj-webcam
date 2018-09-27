from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^success$', views.save_screenshot, name='save_screenshot'),
]