from django.urls import path
from database import views
from django.contrib import admin

urlpatterns = [
    path('', views.home , name="home"),
    path('about/' , views.about , name='about'),
    path('change_setting/' , views.change_setting , name='change_setting'),
    path('chat_bot/' ,views.chat_bot , name='chat_bot'),
    path('login' , views.login , name='login' ),
    path('logout' , views.logout , name='logout' ),
    path('query_page/' , views.query_page ,name='query_page'),
    path('add_notes/' , views.add_notes ,name='add_notes'),
    path('sign_up/' , views.sign_up , name='sign_up'),
    path('student_exams_scheduled/' , views.stu_future , name='stu_future'),
    
    path('stu_home/' , views.stu_home , name='stu_home'),
    path('login/stu_home/' , views.stu_home , name='stu_home'),

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

    path('add_course/',views.add_course,name="add_course"),
    path('remove_course/',views.remove_course,name="remove_course"),
    path('add_class/',views.add_class,name="add_class"),
    path('remove_class/',views.remove_class,name="remove_class"),

    path('temp_sign_up' ,views.temp_sign_up , name="temp_sign_up"),
    path('course_select', views.course_select,name='course_select'),
    path('class_select/', views.class_select,name='class_select'),
    #path('delete/<int:primry_key>/' ,views.delete_data , name="deletedata"),
    #path('update/<int:primry_key>/' ,views.update_data , name="updatedata"),
    path('quiz/', views.quiz,name='quiz'),
    path('exam_detail' , views.exam_detail , name="exam_detail"),
    path('ques_setup' , views.ques_setup , name="ques_setup"),
    
    path('course_select/', views.course_select,name='course_select'),
    path('show',views.show),
    path('test/',views.test),
    path('returner/',views.returner),
    path('correct_ans/',views.correct_ans),

    path('index/' , views.index , name="index" ),
]
