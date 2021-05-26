from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^Projectpage1.html$', views.index),
    url(r'^Regconf$', views.regconf),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^Main$', views.main),
    url(r'^Projectpage3.html$', views.main),
    url(r'^Projectpage7.html$', views.contact),
    url(r'^Projectpage5.html$', views.review),
    url(r'^Projectpage4.html$', views.about),
    url(r'^Projectpage8.html$', views.logout),
    url(r'^Projectpage6.html$', views.moviedesc),
    url(r'^Projectpage9.html$', views.moviesee),
]
