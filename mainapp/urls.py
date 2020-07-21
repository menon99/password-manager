
from .views import WebsiteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'sites', WebsiteViewSet)
