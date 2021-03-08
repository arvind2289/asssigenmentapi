from user.api import viewset as users_api_viewset
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


urlpatterns =[


    path('login/', users_api_viewset.UserLogin.as_view(), name="login"),# login with email and password for genrate token
    path('api/login/', obtain_auth_token, name='api_token_auth'), # this url use for genrate token with username and password
    path('api/createuser/', users_api_viewset.user_list, name='create_user'),# create user and list user
    path("api/question/",users_api_viewset.QuestionCreate,name='question'), # post question and list posted question
    path("api/question/answer/",users_api_viewset.QuestionAswerView,name='QuestionsAnswer'), # question answer
    path("api/userype/filter/",users_api_viewset.UserTypeFilter,name="UserTypeFilter"), # user_type filter

]