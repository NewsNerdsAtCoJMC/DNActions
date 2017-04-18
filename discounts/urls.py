from django.conf.urls import url
from discounts import views

urlpatterns = [
    url(r'^$', views.deal_list),
]
