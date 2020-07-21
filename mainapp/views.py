
from rest_framework import viewsets
from .models import Website
from .serializers import WebsiteSerializer
from django_filters import rest_framework as filters


class WebsiteFilter(filters.FilterSet):
    userId = filters.NumberFilter(field_name="user", lookup_expr='exact')
    class Meta:
        model = Website
        fields  = [ 'user' , 'site', 'username']

class WebsiteViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comments instances.
    """
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    filterset_class = WebsiteFilter

    def get_queryset(self):
        userId = self.request.query_params.get('userId')
        return Website.objects.filter( user = userId)

