from django.conf.urls import url
from .views import RegisterView

urlpatterns = [
    url(r'^$', RegisterView.as_view()),
]
