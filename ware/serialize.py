from rest_framework import serializers
from ware.models import Ware


class WareSerializer(serializers.ModelSerializer):
    class Meta:  # 데이터에 대한 데이터 (데이터 설명)
        model = Ware
        fields = ['name', 'description', 'price']
