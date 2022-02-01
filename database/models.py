
from os import P_OVERLAY
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, IntegerField
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    email_id = models.EmailField(max_length=200  , primary_key=True ,unique=True)
    mobile_no = models.CharField(max_length=200 , default="0")
    role_id = models.ForeignKey("role_id" , on_delete=models.CASCADE , default=2)
    USERNAME_FIELD = 'email_id'
    
    REQUIRED_FIELDS = [] 
    # A list of the field names that will be prompted for when creating a user via the createsuperuser management command. 
    # The user will be prompted to supply a value for each of these fields. 
    # REQUIRED_FIELDS has no effect in other parts of Django, like creating a user in the admin.

class UserManager(BaseUserManager):

    def create_user(self , email_id,password=None):
        if not email_id:
            raise ValueError('User must have an email address')

        user = self.model( email_id=self.normalize_email(email_id) ,)
        # Normalizes email addresses by lowercasing the domain portion of the email address.

        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, username, password, **kwargs):
        user = self.model(email=username, is_staff=True, is_superuser=True,**kwargs)
        user.set_password(password)
        user.save()
        return user


class role_id(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name= models.CharField(max_length=100)

class course_id(models.Model):
    course_id = models.CharField(primary_key=True , max_length=100)
    course_name= models.TextField(max_length=100)
    class_stu_tech=models.IntegerField(default=11)
"""
class sign_up(models.Model):
    role_id=models.ForeignKey("role_id" , on_delete=models.CASCADE)
    id=models.CharField( max_length=50)
    name=models.TextField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    email_id=models.EmailField(primary_key=True)
    mobile_no=models.CharField(max_length=200)
    institute_name=models.TextField()
"""


class class_stu_tech(models.Model):
    role_id=models.ForeignKey("role_id" , on_delete=models.CASCADE)
    #email_id=models.ForeignKey("sign_up" , on_delete=models.CASCADE)
    email_id = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )
    class_stu_tech=models.IntegerField()
    serial_no=models.AutoField(primary_key=True)


class courses_availed(models.Model):
    course_id=models.ForeignKey("course_id" , on_delete=models.CASCADE )
    role_id=models.ForeignKey("role_id" , on_delete=models.CASCADE)
    #email_id=models.ForeignKey("sign_up" , on_delete=models.CASCADE)
    email_id = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )
    serial_no=models.AutoField(primary_key=True)

class exam_details(models.Model):
    exam_code=models.CharField(max_length=50 , primary_key=True)
    exam_title=models.TextField()
    date=models.DateField(help_text = "(YYYY-MM-DD)")
    start_time=models.TimeField()
    duration=models.DurationField( help_text="(HH:MM:SS)")
    no_of_ques=models.IntegerField()
    max_marks=models.IntegerField()
    course_id=models.ForeignKey("course_id" , on_delete=models.CASCADE )
    #email_id=models.ForeignKey("sign_up" , on_delete=models.CASCADE)
    email_id = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )
    class_stu = models.IntegerField(default=11)

class ques_table(models.Model):
    ques_id=models.CharField(max_length=50 , primary_key=True)
    ques=models.TextField(max_length=500)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    correct=models.IntegerField()
    marks=models.IntegerField()
    exam_code=models.ForeignKey("exam_details" , on_delete=models.CASCADE )

class answer_table(models.Model):
    exam_code=models.ForeignKey("exam_details" , on_delete=models.CASCADE )
    ques_id=models.ForeignKey("ques_table",on_delete=models.CASCADE , related_name="ques_idd")
    #email_id=models.ForeignKey("sign_up",on_delete=models.CASCADE)
    email_id = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )
    role_id=models.ForeignKey("role_id",on_delete=models.CASCADE )
    option_marked=models.IntegerField()
    check_correct=models.BooleanField()

class score_table(models.Model):
    exam_code=models.ForeignKey("exam_details" , on_delete=models.CASCADE )
    #email_id=models.ForeignKey("sign_up" , on_delete=models.CASCADE)
    email_id = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )
    role_id=models.ForeignKey("role_id" , on_delete=models.CASCADE )
    scored_marks=models.IntegerField()
    percentage=models.DecimalField(max_digits=5,decimal_places=2)

class registration_table(models.Model):
    exam_code=models.ForeignKey("exam_details" , on_delete=models.CASCADE )
    #email_id=models.ForeignKey("sign_up" , on_delete=models.CASCADE)
    email_id = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )
    role_id=models.ForeignKey("role_id" , on_delete=models.CASCADE )   

class notes_table(models.Model):
    #email_id=models.ForeignKey("sign_up" , on_delete=models.CASCADE)
    email_id = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )
    exam_code=models.ForeignKey("exam_details" , on_delete=models.CASCADE )
    notes=models.TextField(max_length=500)

class query_table(models.Model):
    #email_id=models.ForeignKey("sign_up" , on_delete=models.CASCADE)
    email_id = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )
    exam_code=models.ForeignKey("exam_details" , on_delete=models.CASCADE )
    role_id=models.ForeignKey("role_id" , on_delete=models.CASCADE)
    query=models.TextField(max_length=500)


"""
class sample(models.Model):
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    def __str__(self): #this is used so that the fields that are stored are displayed with thier respective emails instead of being numbered as table_name1,table_name2
        return self.email
"""

# You should also define a custom manager for your user model.
# If your user model defines username, email, is_staff, is_active, is_superuser, last_login, and date_joined fields the same as Django’s default user, you can install Django’s UserManager;
#  however, if your user model defines different fields, you’ll need to define a custom manager that extends BaseUserManager
