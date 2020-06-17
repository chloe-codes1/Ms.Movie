from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
        path('profile/', views.UserAPI.as_view(), name='profile'),
        path('<user_pk>/', views.OtherUserAPI.as_view(), name='others_profile'),
]
