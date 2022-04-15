from django.urls import path
from .views import HomePageView, AboutUsView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('aboutus/', AboutUsView.as_view(), name = 'aboutUs'),
]