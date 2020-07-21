
from rest_framework import viewsets
from .models import Website
from .serializers import WebsiteSerializer
from django_filters import rest_framework as filters
from . import utils

from django.db.models import F, Value , CharField



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
        userId = self.request.query_params.get('user')
        print('id is ', userId)
        sites = Website.objects.filter( user__pk = userId)#.annotate( password = Temp )  
        print('sites is ',sites)
        for site in sites:
            site.password = utils.decrypt(site.password)
            print(site.password)
        return sites
    

