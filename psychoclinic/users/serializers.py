from rest_framework import serializers
from .models import Patient, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'avatar', 'is_active',
                  'is_staff', 'is_superuser', 'date_joined')


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Patient
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_data = data.pop('user')
        data.update(user_data)
        return data
