from .models import  Website
from rest_framework import serializers
from . import utils

class WebsiteSerializer(serializers.ModelSerializer):
    decrypted_password = serializers.SerializerMethodField('password')
    def password(self, p):
        return utils.decrypt(p.password)

    class Meta:
        model = Website
        fields = '__all__'