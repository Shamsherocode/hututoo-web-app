
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class QuizOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        # fields = '__all__'
        fields = ['option1', 'option2']




class QuizCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCategory
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizs
        fields = '__all__'


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['options'] = QuizOptionSerializer(instance.options).data
        return rep

    # def checkdate():
    #     date = datetime.now()
    #     return date

    # def validate(self, data):
    #     if data['created'] < self.checkdate():
    #         raise serializers.ValidationError({'error': 'Date must me valid..'})

    #     return data