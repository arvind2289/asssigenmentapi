from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuestionsAnswerSerializer, QuestionsSerializer
from ..models import QuestionsAnswer, Questions
from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
import json
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import api_view

import traceback
@authentication_classes([])
@permission_classes([])
class UserLogin(APIView):
    def post(self, request, format=None):
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            User = get_user_model()
            if User.objects.filter(email= email).exists():
                user_instance = User.objects.get(email=email)
                user = authenticate(username=user_instance.username,
                                    password=password)
                if user:
                    login(request, user)
                    if Token.objects.filter(user=user).exists():
                        Token.objects.get(user=user).delete()
                    token = Token.objects.create(user=user)
                    resp = {
                        "Token": str(token),
                        "name": user_instance.email,
                        "code": 200,
                        "user_id": user_instance.id,
                    }
                    return HttpResponse(json.dumps(resp, sort_keys=True, default=str), content_type="application/json")
                    # return Response(resp)
                else:
                    resp = {"error": "Invalid password", "code": 212}
                    return Response(resp)
            else:
                resp = {"error": "Invalid mobile number", "code": 210}
                return Response(resp)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + " " + str(trace_back)
            print(message)
            resp = {"error": "Something went wrong, please try again or contact administrator", "code": 500}
            return Response(resp)

### create user view

@api_view(['GET', 'POST'])
@permission_classes([])
def user_list(request):
    User= get_user_model()
    """
    List all code user, or create a new users.
    """
    if request.method == 'GET':
        #User = get_user_model()
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            instance_obj = serializer.save()
            instance_obj.username = instance_obj.email
            instance_obj.user_tpe = '0'
            instance_obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([])
def QuestionCreate(request):
    """
    List all code question, or create a new question.
    """
    if request.method == 'GET':
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



### filter user type
@api_view(['GET', 'POST'])
def UserTypeFilter(request):
    User = get_user_model()
    if request.method == 'POST':
        user_type =request.data['user_type']
        user = User.objects.filter(user_type=user_type)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def QuestionAswerView(request):
    """
    List all code question, or create a new question.
    """
    if request.method == 'GET':
        questions = QuestionsAnswer.objects.values('id','questions__question','answer','questions__user_id',
                                                   'mentor__first_name')

        import  json
        return HttpResponse(json.dumps(list(questions), sort_keys=True, default=str),
                            content_type="application/json")

## filter on according to Question

