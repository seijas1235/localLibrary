from django.urls import path
from .views import SingUpView, ProfileUpdate , SingUpAdminView

urlpatterns = [
    path('signup/',SingUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('signupadmin/',SingUpAdminView.as_view(), name='signupadmin'),
]