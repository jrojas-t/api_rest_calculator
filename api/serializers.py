from rest_framework import serializers
from base.models import ConnectionElementView

class ConnectionElementViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionElementView
        fields = '__all__'