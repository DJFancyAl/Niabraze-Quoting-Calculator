from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['date'] = instance.date.strftime("%B, %d %Y")
        return data