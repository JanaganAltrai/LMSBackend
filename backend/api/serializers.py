from rest_framework import serializers
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .models import User


class DateField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return value.strftime('%Y-%m-%d')

class TimeField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return value.strftime('%H:%M:%S')
    


class UserSerializer(serializers.ModelSerializer):

    join_date = DateField()
    join_time = TimeField()

    class Meta:
        model=User
        fields = ['id', 'name', 'email','password', 'role', 'join_date', 'join_time']
        extra_kwargs={
            'password':{'write_only':True}
        }


    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 