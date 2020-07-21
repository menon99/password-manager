from .models import  Website
from rest_framework import serializers

class WebsiteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Website
        fields = "__all__"