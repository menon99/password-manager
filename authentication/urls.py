from .views import UserViewSet
from rest_framework import routers
from django.urls import path
from rest_framework.authtoken import views

router = routers.SimpleRouter()

router.register(r'user', UserViewSet)

urlpatterns = [
    path( 'auth/', views.obtain_auth_token ),
]
urlpatterns += router.urls

# http://localhost:8000/app/user/auth/