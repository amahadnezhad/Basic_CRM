from django.urls import path

from .views import AboutUsPageView

urlpatterns = [
    path('aboutus/', AboutUsPageView.as_view(), name='aboutus')
]
