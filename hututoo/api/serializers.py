from datetime import datetime
from rest_framework import serializers
from .models import *

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizs
        fields = '__all__'

    # def checkdate():
    #     date = datetime.now()
    #     return date

    # def validate(self, data):
    #     if data['created'] < self.checkdate():
    #         raise serializers.ValidationError({'error': 'Date must me valid..'})

    #     return data