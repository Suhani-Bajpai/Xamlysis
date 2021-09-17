from django.urls import path
from database import views
from django.contrib import admin

urlpatterns = [
    path('', views.home , name="home"),
    path('about/' , views.about , name='about'),
    path('change_setting/' , views.change_setting , name='change_setting'),
    path('chat_bot/' ,views.chat_bot , name='chat_bot'),
    path('login/' , views.login , name='login' ),
    path('logout/' , views.logout , name='logout' ),
    path('query_page/' , views.query_page ,name='query_page'),
    path('sign_up/' , views.sign_up , name='sign_up'),
    path('student_exams_scheduled/' , views.stu_future , name='stu_future'),
    path('student_home_page/' , views.stu_home , name='stu_home'),
    path('student_login/' , views.stu_login , name='stu_login'),
    path('student_previous_exams/' , views.stu_prev , name='stu_prev'),
    path('student_sign_up/' , views.stu_sign_up , name='stu_sign_up'),
    path('teachers_future_exam_scheduled/' , views.teach_future, name='teach_future'),
    path('teachers_home/' , views.teach_home , name='teach_home'),
    path('teachers_login/' , views.teach_login , name='teach_login'),
    path('teachers_previous_exams_scheduled/' , views.teach_prev , name='teach_prev'),
    path('teachers_schedule/' , views.teach_schedule , name='teach_schedule'),
    path('teachers_sign_up/' , views.teach_sign_up , name='teach_sign_up'),
    #added for checking
    path('check/',views.base1,name="base1"),
    path('temp_sign_up' ,views.temp_sign_up , name="temp_sign_up"),
    #path('delete/<int:primry_key>/' ,views.delete_data , name="deletedata"),
    #path('update/<int:primry_key>/' ,views.update_data , name="updatedata"),
]
