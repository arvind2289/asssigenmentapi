from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

# Register your models here.
# class CustomUsersAdmin(ModelAdmin):
#
#     list_display = ['id', 'name', 'is_active',
#                  'email','user_type']
#     list_filter = ['is_active']
#
#
# admin.site.register(CustomUsers, CustomUsersAdmin)
class UsersAdmin(ModelAdmin):
    list_display = ['id', 'first_name','last_name','email','username', 'is_active',
                    'user_type']

admin.site.register(User,UsersAdmin)



class QuestionsAdmin(ModelAdmin):
    list_display = ['id', 'question','user_id','question_created',
                    ]

admin.site.register(Questions,QuestionsAdmin)


@admin.register(QuestionsAnswer)
class QuestionsAnswerAdmin(ModelAdmin):
    list_display = ['id','questions', 'answer','AnswerBy', 'question_created',
                    ]


    def AnswerBy(self, inst):
        return inst.mentor

    AnswerBy.allow_tags = True
    AnswerBy.short_description = "Answer By"

    # def questions_PublicUser(self, inst):
    #     return inst.questions.user_id
    #
    # questions_PublicUser.allow_tags = True
    # questions_PublicUser.short_description = "Question Ask By"




