from django.conf.urls import url
from django.views.generic import RedirectView

from url import views as views


urlpatterns = [
    url(r'^(?P<short_name>.*)/$', views.Redirect.as_view()),
    url(r'^$', views.Home.as_view(), name='home'),
]