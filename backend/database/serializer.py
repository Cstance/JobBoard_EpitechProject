from rest_framework import serializers
from .models import Users, Advertisements, Companies, Application


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__' 

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisements
        fields = '__all__' 
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__' 

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
