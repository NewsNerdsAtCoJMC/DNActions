from django.conf.urls import url
from flashbriefing import views

urlpatterns = [
    url(r'^$', views.flash_briefing),
]
