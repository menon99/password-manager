
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Website
from .serializers import WebsiteSerializer
from django_filters import rest_framework as filters
from . import utils

from django.db.models import F, Value , CharField
from django.contrib.auth.models import User



class WebsiteFilter(filters.FilterSet):
    userId = filters.NumberFilter(field_name="user", lookup_expr='exact')
    class Meta:
        model = Website
        fields  = [ 'user' , 'site', 'username']

# class Temp:
#     function = utils.decrypt( Value('password' , output_field= CharField() ) ) 


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing site instances.
    """
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    filterset_class = WebsiteFilter

    
    def get_queryset(self):
        qs = Website.objects.filter( user = self.request.query_params.get('userId'))
        return qs

    

