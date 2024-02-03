from accounts import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup_view, name = 'signup_auth'),
    path('login/', views.login_view, name = 'login_auth'),
    path('logout/', views.logout_view, name = 'logout_auth'),
]


