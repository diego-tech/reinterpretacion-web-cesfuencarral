from django.urls import path
from .views import CampusPageView, SamplePageView

urlpatterns = [
    path('', CampusPageView.as_view(), name='campus'),
    path('sample/', SamplePageView.as_view(), name='sample'),
]
