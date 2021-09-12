from django.shortcuts import render ,redirect , HttpResponse
#from database.models import sign_up as SU 
from database.models import class_stu_tech as CST
from database.models import role_id as RI
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate , logout
import datetime
import mysql.connector
from django.contrib.auth.forms import UserCreationForm
#from mysite.core.forms import SignUpForm
from .forms import MyUserCreationForm


# Create your views here.
# check for anonymous user - not logged in user

def temp_sign_up(request):
    if request.method == 'POST':
        #form = SignUpForm(request.POST)
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('home')
    else:
        form = MyUserCreationForm()
    return render (request , 'stu_sign_up.html' , {'form':form})

def home (request):
    return render(request , 'landup_page.html')

def about(request):
    return render(request , 'about.html')

def change_setting(request):
    return render(request , 'database/change_setting.html')

def chat_bot(request):
    return render(request , 'database/chat_bot.html')

def login(request): 
    return render(request , 'database/login.html')

def query_page(request):
    return render(request , 'database/query_page.html')

def sign_up(request):
    return render(request , 'database/sign_up.html')

def stu_future(request):
    return render(request , 'database/stu_future.html')

def stu_home(request):
    return render(request , 'database/stu_home.html')

def stu_login(request):
    if request.method=="POST":
        email=request.POST.get('Email-Id')
        username = request.POST.get('Username')
        password=request.POST.get('Password')

        user1 = sign_up.authenticate(email=email , password=password ) 
        user2 = sign_up.authenticate(username=username , password=password)
        
        if user1 is not None :
            #login(request , user1)
            return redirect("stu_home.html")
        elif user2 is not None:
            #login(request , user2)
            return redirect("stu_home.html")
    return render(request , 'stu_login.html')

def stu_prev(request):
    return render(request , 'database/stu_prev.html')

def stu_sign_up(request):
    if request.method=="POST":
        name=request.POST.get('name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        stu_class=request.POST.get('stu_class')
        email_id=request.POST.get('email_id')
        mob_no=request.POST.get('mob_no')
        institute_name=request.POST.get('institute_name')
        subjects=request.POST.get('subjects')

        x = str(datetime.datetime.now())
        id="STU "+x[:19]
        role_id= RI.objects.get(role_id=2)  
        Sign_up=SU(role_id=role_id , id=id ,name=name , username=username , password=password , email_id=email_id ,mobile_no=mob_no , institute_name=institute_name)
        Sign_up.save()

        email= SU.objects.get(email_id=email_id) 
        Class_stu_tech = CST(role_id=role_id , email_id=email , class_stu_tech=stu_class)
        Class_stu_tech.save()

        return redirect('home')

    return render(request , 'stu_sign_up.html')


def teach_future(request):
    return render(request , 'database/teach_future.html')

def teach_home(request):
    return render(request , 'database/teach_home.html')

def teach_login(request):
    if request.method=="POST":
        email=request.POST.get('Email-Id')
        username = request.POST.get('Username')
        password=request.POST.get('Password')

        user1 = sign_up.authenticate(email=email , password=password ) 
        user2 = sign_up.authenticate(username=username , password=password)
        
        if user1 is not None :
            #login(request , user1)
            return redirect("teach_home.html")
        elif user2 is not None:
            #login(request , user2)
            return redirect("teach_home.html")

    return render(request , 'teach_login.html')


def teach_prev(request):
    return render(request , 'database/teach_prev.html')

def teach_schedule(request):
    return render(request , 'database/teach_schedule.html')

def teach_sign_up(request):
    if request.method=="POST":
        name=request.POST.get('Name')
        username=request.POST.get('Username')
        password=request.POST.get('Password')
        teach_class=request.POST.get('Class')
        email_id=request.POST.get('Email-ID')
        mob_no=request.POST.get('Mobile Number')
        institute_name=request.POST.get('Institute Name')
        subjects=request.POST.get('Courses')

        x = str(datetime.datetime.now())
        id="TEA "+x[:19]

        Sign_up=sign_up(role_id=1 ,id=id , name=name , username=username , password=password , email_id=email_id ,mobile_no=mob_no , institute_name=institute_name)
        Sign_up.save()

        Class_stu_tech = class_stu_tech(role_id=1 , email_id=email_id , class_stu_tech=teach_class)
        Class_stu_tech.save()

        return redirect(request , 'teach_home.html' )

    return render(request , 'teach_sign_up.html')

#added for checking
def base1(request):
    return render(request , 'base1.html')


#temporary log in
"""
def temp_login (request):
    con1 = mysql.connector.connect(host="localhost" , user="root" , password="priyanshi13" , database="xamlysis")
    cursor = con1.cursor()
    con2 = mysql.connector.connect(host="localhost" , user="root" , password="priyanshi13" , database="xamlysis")
    cursor = con2.cursor()


def home(request):
    #return HttpResponse("A trial");
    #context is set of variables
    context={
        'variable':"this is sent",
        'variable1' : 'thanks to yt'
    }

    return render(request , 'loading_page.html' , context)

def about(request):
    if request.user.is_anonymous:
        return redirect("base.html")

    if request.method=="POST":
        email=request.POST.get('email')
        phone=request.POST.get('no')
        Sample=sample(email=email , phone=phone)
        Sample.save()
        #displays all the data saved in the db
        sample.objects.all()
        sample.objects.all()[0].email
        sample.objects.filter(email='s@gmail.com')
        sample.objects.filter(email="s@gmail.com" , phone="s@gmail.com")
        var = sample.objects.filter(email="s@gmail.com" , phone="s@gmail.com")
        var.email="s@g.com"
        var.save()
        sample.objects.all().first
        sample.objects.all().last

    if request.method=="POST":
        email=request.POST.get('email')
        phone=request.POST.get('no')

        #for login  -bootstrap login
        user = User.authenticate(email=email , phone=phone)
        # for html write - welcome {{request.user 
        if user is not None:
            login(request , user)
            return redirect("base.html")

        messages.success(request, 'Profile details updated.')

    return render(request , 'loading_page.html')

    def logout_of_the_user(request):
        logout(request)
    return redirect(request , "loading_page.html")

"""