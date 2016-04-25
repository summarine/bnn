from django.conf.urls import url, include
from . import views

app_name='forecasting'
urlpatterns = [
    url(r'^$',views.HomePageView.as_view(), name='index')
]