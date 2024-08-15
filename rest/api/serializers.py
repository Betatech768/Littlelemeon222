from rest.models import Take 
from rest_framework.serializers import ModelSerializer

class TakeSerializer(ModelSerializer):
    class Meta:
        model= Take 
        fields = '__all__'