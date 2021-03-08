
from user.models import *
from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from user.models import QuestionsAnswer , Questions
User = get_user_model()
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','username', 'email','password','user_type']



class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['question','user_id']


class QuestionsAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsAnswer
        fields = ['questions','answer','mentor','question_created']