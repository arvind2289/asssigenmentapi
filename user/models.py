from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.
from django.utils import timezone
from django_currentuser.middleware import get_current_authenticated_user
class User(AbstractUser):
    USER_TYPE = (
        ('0', 'user'),
        ('1', 'mentor'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE, default='1')



class CustomUsers(models.Model):
    USER_TYPE = (
        ('user', 'user'),
        ('mentor', 'mentor'),
    )
    id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=100,choices=USER_TYPE, default='mentor')
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=255, null=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True,unique=True,max_length=200)

    def __str__(self):
        return self.name or ''

    def __unicode__(self):
        return self.name or ''


class Questions(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    question = models.CharField(max_length=500,db_column='question')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False,db_column="user_id")
    question_created = models.DateTimeField(default=timezone.now,db_column="question_created")
    def __str__(self):
        return self.question or ''


    class Meta:
        db_table = 'questions'
        managed = True
        verbose_name = "Create Questions"
        verbose_name_plural = 'Create Questions'



class QuestionsAnswer(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    questions = models.ForeignKey(Questions,on_delete=models.CASCADE,null=True,blank=True,db_column="questions")
    answer = models.TextField(max_length=2000,db_column='answer')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,db_column="mentor")
    question_created = models.DateTimeField(default=timezone.now,db_column="question_created")

    def __str__(self):
        return self.questions or ''

    class Meta:
        db_table = 'questionsanswer'
        managed = True
        verbose_name = "Questions Answer List"
        verbose_name_plural = 'Questions Answer List'

