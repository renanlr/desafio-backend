from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

    owner = serializers.ReadOnlyField(source='owner.username')

    def update(self, instance, validated_data):
        instance.classification = validated_data.get('classification', instance.classification)
        instance.rating = validated_data.get('rating', instance.rating)
        return instance
