from django.shortcuts import render ,redirect , HttpResponse
import random , datetime , json
from django.http import JsonResponse
from database.models import *
from database.models import class_stu_tech as CST
from database.models import role_id as RI
from database.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate , logout as auth_logout
import datetime
import mysql.connector
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from mysite.core.forms import SignUpForm
from .forms import *
from django.forms import modelformset_factory
from os import access


# Create your views here.
# check for anonymous user - not logged in user

def temp_sign_up(request):
    courses_display= class_stu_tech.objects.all().filter(class_stu_tech=11)
    if request.method == 'POST':
        #form = SignUpForm(request.POST)
        form = MyUserCreationForm(request.POST)
        fm=class_stu_tech_form(request.POST)
        
        #if fm.is_valid():
            #role_id= RI.objects.get(role_id=2)  
            #email_id = User.objects.filter(email_id="suhani20@gmail.com")
            #class_stu=request.POST.get('class_stu_tech')
            #Class_stu_tech = CST(role_id=role_id , email_id_id=email_id , class_stu_tech=class_stu)
            #Class_stu_tech.save()
            #fm.save()
        if form.is_valid():
            user=form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = MyUserCreationForm()
        fm=class_stu_tech_form()
    return render (request , 'stu_sign_up.html' , {'form':form  , 'courses':courses_display ,})#, 'fm':fm}  )

def login(request): 
    if request.user.is_authenticated:
        return redirect('home')

    if request.method =="POST" :
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username , password=password)
            if user is not None:
                auth_login(request , user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password.")
        else:
    	    messages.error(request,"Invalid username or password.")
	
    form = AuthenticationForm()
    return render(request , 'login.html' , {'form':form})

def logout(request):
    auth_logout(request)
	
    messages.info(request, "You have successfully logged out.") 
    return redirect( 'home')

def home (request):
    return render(request , 'landup_page.html')

def about(request):
    return render(request , 'about_page.html')

def change_setting(request):
    form=Change_Mobile_No_Form()
    current_user=request.user
    if request.method=="POST":
        form = Change_Mobile_No_Form(request.POST)
        if form.is_valid():
            mn=form.cleaned_data['mobile_no']
            obj=User.objects.get(email_id=current_user.email_id)
            obj.mobile_no=mn
            obj.save(update_fields=['mobile_no'])
            return redirect('stu_home')
    return render(request , 'change_mobile_no.html' , {'form':form})

def chat_bot(request):
    return render(request , 'database/chat_bot.html')

def query_page(request):
    return render(request , 'database/query_page.html')

def sign_up(request):
    return render(request , 'database/sign_up.html')

def stu_future(request):
    return render(request , 'database/stu_future.html')






















def stu_home(request):
    current_user=request.user
    stud_data = CST.objects.filter(email_id=current_user.email_id,)
    all=[]  
    [all.append(str(x.class_stu_tech)) for x in stud_data]
    exam_data = exam_details.objects.all()
    availed_courses = courses_availed.objects.filter(email_id=current_user.email_id,)
    ac=[]
    [ac.append(str(x.course_id)) for x in availed_courses]
    acc=[]
    for s in ac:
        strt=s.find('(')+1
        end=s.find(')',strt)
        acc.append(s[strt:end])
    exams=[]
    for s in exam_data:
        if (s.course_id_id in acc):
            exams.append(s)
    given_exams = score_table.objects.filter(email_id_id=current_user.email_id,)
    next_exams=[]
    donttake=[]
    [donttake.append(str(x.exam_code_id)) for x in given_exams]
    for i in exams:
        if (i.date >= datetime.datetime.now().date()):
            if(i.exam_code not in donttake):
                next_exams.append(i)

    context={
        'class': all,
        'mobile':current_user.mobile_no,
        'next_exams':next_exams,
        'pre_exams':given_exams
    }
    return render(request , 'stu_home.html',context)

def login_stu_home(request):
      
    current_user=request.user
    stud_data = CST.objects.filter(email_id=current_user.email_id,)
    all=[]  
    [all.append(str(x.class_stu_tech)) for x in stud_data]
    context={
        'class': all,
        'mobile':current_user.mobile_no,
    } 
    return render(request,'stu_home.html',context)















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
    current_user=request.user
    edobj=exam_details.objects.filter(email_id_id=current_user.email_id).values('exam_title' , 'exam_code', 'date' , 'max_marks' , 'duration' , 'start_time')
    edobj=list(edobj)
    #print(edobj)
    #edobj=edobj[:]["exam_title"]
    #no_q=exam_details.objects.filter(exam_code=ec).values('no_of_ques')[0]["no_of_ques"]
    #print(edobj)
    if request.GET.get('course'):
        if request.method=="POST":
            return HttpResponse("STAY BLESSED AND WARM")
        print("yes Hello World")
        ques = ques_table.objects.filter(exam_code__exam_code__icontains=request.GET.get('course'))
        data=[]
        ques=list(ques)
        random.shuffle(ques)
        for quest in ques:
            data.append({
                "ques_id" : quest.ques_id,
                "marks" : quest.marks,
                "ques" : quest.ques,
                "opt1" : quest.option1,
                "opt2" : quest.option2,
                "opt3" : quest.option3,
                "opt4" : quest.option4,
                "correct" : quest.correct,
                "exam_code" : request.GET.get('course'),
        })
        if data==[]:
            data.append({"exam_code" : request.GET.get('course'),})
        print(data)
        payload ={ 'data':data}
        return render(request , 'teach_schedule.html' , {'data' :data,})
    
    elif request.GET.get('code'):
        print(request.GET.get('code'))
        obj = exam_details.objects.get(exam_code=request.GET.get('code'))
        print(obj)
        obj.delete()
        return redirect('teach_home')   

    elif request.GET.get('del_ques'):
        print(request.GET.get('del_ques'))
        obj = ques_table.objects.get(ques_id=request.GET.get('del_ques'))
        course_id= obj.exam_code_id
        print(obj)
        print( course_id)
        obj_ed=exam_details.objects.get(exam_code=course_id)
        obj_ed.no_of_ques-=1
        obj_ed.max_marks-=obj.marks
        print(obj_ed.no_of_ques , obj_ed.max_marks)
        obj_ed.save(update_fields=['no_of_ques' , 'max_marks'])
        obj.delete()
        return redirect(f'/teachers_home/?course={course_id}')   

    elif request.method=="POST":
        print("be happy always")
        form = Ques_Setup_Form(request.POST)
        form1 = Change_Date_Form(request.POST)
        form2 = Change_Duration_Form(request.POST)
        form3 = Change_Start_Time_Form(request.POST)
        if form.is_valid():
            qu=form.cleaned_data['ques']
            op1=form.cleaned_data['option1']
            op2=form.cleaned_data['option2']
            op3=form.cleaned_data['option3']
            op4=form.cleaned_data['option4']
            cor=form.cleaned_data['correct']
            mk=form.cleaned_data['marks']
            obj=exam_details.objects.get(exam_code=request.GET.get('add_ques'))
            print(obj)
            c=datetime.datetime.now()
            qi=str(request.GET.get('add_ques'))+str("-")+c.isoformat()
            qt=ques_table(ques_id=qi ,ques=qu , option1=op1 , option2=op2 , option3=op3 , option4=op4 , correct=cor , marks=mk , exam_code_id=request.GET.get('add_ques') )
            qt.save()
            obj.no_of_ques+=1
            obj.max_marks+=mk
            obj.save(update_fields=['no_of_ques' , 'max_marks'])
            return redirect(f'/teachers_home/?course={request.GET.get("add_ques")}') 
        
        elif form1.is_valid():
            dat=form1.cleaned_data['date']
            obj=exam_details.objects.get(exam_code=request.GET.get('edit'))
            obj.date=dat
            obj.save(update_fields=['date'])
            return redirect('teach_home')

        elif form2.is_valid():
            dur=form2.cleaned_data['duration']
            obj=exam_details.objects.get(exam_code=request.GET.get('edit'))
            obj.duration=dur
            obj.save(update_fields=['duration'])
            return redirect('teach_home')

        elif form3.is_valid():
            st=form3.cleaned_data['start_time']
            obj=exam_details.objects.get(exam_code=request.GET.get('edit'))
            obj.start_time=st
            obj.save(update_fields=['start_time'])
            return redirect('teach_home')

    
    elif request.GET.get('add_ques'):
        print("positive attitude")
        form = Ques_Setup_Form()
        # return redirect(f'/teachers_home/?add_ques={request.GET.get("add_ques")}')
        return render(request , 'stu_sign_up.html' , {'form' : form ,})

    elif request.GET.get('edit'):
        form1 = Change_Date_Form()
        form2 = Change_Duration_Form()
        form3 = Change_Start_Time_Form()
        return render(request , "change_setting.html" , {'form1':form1 , 'form2':form2 , 'form3':form3,})
        return HttpResponse("Stay Healthy")

    elif request.GET.get('upcoming'):
        obj=exam_details.objects.filter(email_id=current_user.email_id).values('exam_title' , 'exam_code', 'date' , 'max_marks' , 'duration' , 'start_time')
        d=datetime.datetime.now()
        list_obj=[]
        for x in obj:
            print(x)
            print(x['date'])
            if x['date'] >=d.date() :
                list_obj.append(x)
        return render(request , 'teach_home.html' , {'edobj':list_obj , })

    elif request.GET.get('previous'):
        obj=exam_details.objects.filter(email_id=current_user.email_id).values('exam_title' , 'exam_code', 'date' , 'max_marks' , 'duration' , 'start_time')
        d=datetime.datetime.now()
        list_obj=[]
        for x in obj:
            if x['date'] <d.date() :
                list_obj.append(x)
        return render(request , 'teach_home.html' , {'edobj':list_obj , })

    return render(request , 'teach_home.html' , {'edobj':edobj , })


























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


def class_select(request):
    current_user=request.user
    classes=['1' , '2' , '3' , '4' , '5' , '6' ,'7' ,'8' , '9' , '10' ,'11','12']
    class_joined = CST.objects.filter(email_id=current_user.email_id)
    class_joined_list =[]
    [class_joined_list.append(str(x.class_stu_tech)) for x in class_joined]
    class_notjoined_list = [x for x in classes if x not in class_joined_list]
    
    return render(request , 'class_select.html' , {'cnj':class_notjoined_list , 'cj':class_joined_list ,})


def add_class(request):
    current_user=request.user
    class_id1 = request.POST.get("class")
    s=str(class_id1)
    print(class_id1)
    email_id1=current_user.email_id
    print("" ,"\n")
    print(current_user.role_id)
    obj=class_stu_tech.objects.filter(email_id=current_user.email_id,role_id=2)
    if obj :
        return redirect('/class_select/')
    o_ref=class_stu_tech(current_user.role_id.role_id,email_id1 , class_id1)
    o_ref.save()
    return redirect('/class_select/')

def remove_class(request):
    current_user=request.user
    class_id1 = request.POST.get("class")
    print(current_user.role_id)
    class_stu_tech.objects.filter(email_id=current_user.email_id,role_id=current_user.role_id.role_id,class_stu_tech=class_id1).delete()
    return redirect('/class_select/') 

    






def course_select(request):
    current_user=request.user
    all_courses = course_id.objects.all()
    availed_courses = courses_availed.objects.filter(email_id=current_user.email_id,)
    all=[]  
    [all.append(str(x.course_id)) for x in all_courses]
    ac=[]
    [ac.append(str(x.course_id)) for x in availed_courses]
    acc=[]
    for s in ac:
        strt=s.find('(')+1
        end=s.find(')',strt)
        acc.append(s[strt:end])
    #print(current_user.email_id)
    #not_ac = all.exclude(course_id__in=ac)
    not_ac = [i for i in all if i not in acc]
    #acc is the availed courses
    #not_ac is the not availed course

    '''
    for s in all:
        print(s,'11')
    for s in acc:
        print(s,'33')
    for s in not_ac:
        print(s,'44')
     '''
    CourseFormSet = modelformset_factory(courses_availed, fields=('course_id','email_id','role_id'))
    if request.method == "POST":
        formset = CourseFormSet(
            request.POST, request.FILES,
            queryset=courses_availed.objects.exclude(email_id=current_user.email_id,),
        )
        if formset.is_valid():
            formset.save()
            # Do something.
    else:
        formset = CourseFormSet(queryset=courses_availed.objects.filter(email_id=current_user.email_id,))
    
    return render(request, 'course_select.html', {'form': formset,'nac' : not_ac,'ac':acc})


def add_course(request):
    current_user=request.user
    course_id1 = request.POST.get("course")
    s=str(course_id1)
    print(course_id1)
    email_id1=current_user.email_id
    print("" ,"\n")
    print(current_user.role_id.role_id)
    o_ref=courses_availed(course_id1,current_user.role_id.role_id,email_id1)
    o_ref.save()
    return redirect('/course_select/')

def remove_course(request):
    current_user=request.user
    course_id1 = request.POST.get("course")
    #id=courses_availed.objects.filter(email_id=current_user.email_id,role_id=2,course_id=course_id1)
    courses_availed.objects.filter(email_id=current_user.email_id,role_id=current_user.role_id.role_id,course_id=course_id1).delete()
    return redirect('/course_select/') 

def show(request):
    xx = course_id.objects.all()
    return render(request,"show.html",{'xx':xx})













def test(request):
    current_user=request.user
    if request.method == 'POST':
        print(request.POST)
        questions=ques_table.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=q.marks
            print(request.POST.get(q.ques))
            ans='option'+str(q.correct)
            print(ans)
            if ans ==  request.POST.get(q.ques):
                score+=q.marks
                correct+=1
            else:
                wrong+=1
        percent = score/(total) *100
        exid=request.POST.get("exid")
        #print(score_table.objects.all().order_by('-id')[0].id,'-------')
        id1=score_table.objects.all().order_by('-id')[0].id+1
        o_ref=score_table(id=id1,exam_code_id=exid,email_id_id=current_user.email_id,role_id_id=2,scored_marks=score,percentage=percent)
        o_ref.save()
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'test_result.html',context)
    else:
        questions=ques_table.objects.all()
        examid=request.GET.get("exid")
        instr=exam_details.objects.get(exam_code=examid)
        context = {
            'questions':questions,
            'inst':instr,
            'examid':examid
        }
        return render(request,'test.html',context)

def correct_ans(request):
    exam_id1 = request.POST.get("course")
    all=ques_table.objects.all()
    ans=ques_table.objects.filter(exam_code_id=exam_id1)
    for i in ans:
        print(i.exam_code_id)
    return render(request,'test_ans.html',{'questions':ans})

def returner(request):
    return redirect('stu_home')




#temporary log in
"""
def temp_sign_up(request):
    if request.method == 'POST':
        #form = SignUpForm(request.POST)
        form = MyUserCreationForm(request.POST)
        fm=class_stu_tech_form(request.POST)
        if fm.is_valid():
            fm.save()
        if form.is_valid():
            user=form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = MyUserCreationForm()
        fm=class_stu_tech_form()

    enteries = User.objects.all()
    return render (request , 'stu_sign_up.html' , {'form':form , 'fm':fm , 'entries':entries}  )

def delete_data(request , primary_key):
    if request.method=='POST'
        pi = User.objects.get(primary_key='value')
        pi.delete()
        return HttpResponseRedirect('/') 

def update_data(request , primary_key):
    if request.method=='POST':
        pi = User.objects.get(primary_key="value")
        fm = MyUserCreationForm(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi = User.objects.get(primary_key="value")
            fm = MyUserCreationForm( instance=pi)

    return render(request , '' , {'form':form})

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

def exam_detail(request):
    if request.method == 'POST':
        #User.objects.get() 
        form = Exam_Detail_Form(request.POST)
        if form.is_valid():
            ec=form.cleaned_data['exam_code']
            et=form.cleaned_data['exam_title']
            d=form.cleaned_data['date']
            st=form.cleaned_data['start_time']
            du=form.cleaned_data['duration']
            nq=form.cleaned_data['no_of_ques']
            mm=form.cleaned_data['max_marks']
            ci=form.cleaned_data['course_id']
            request.session['exam_code']=ec
            count=1
            request.session['cnt']=count
            global cnt
            current_user=request.user
            #user=User.object.filter(email_id=current_user.email_id)
            #print(user)
            ei=current_user.email_id
            print(ei)
            fm=exam_details(exam_code=ec , exam_title=et , date=d,start_time=st,duration=du, no_of_ques=nq , max_marks=mm, course_id=ci , email_id_id=ei)
            fm.save()
            #form.save()
            global exam_code
            def exam_code():
                return ec
            return redirect('ques_setup')
    else:
        form = Exam_Detail_Form()
    return render (request , 'stu_sign_up.html' ,{'form':form ,} )


def ques_setup(request):
    count=request.session['cnt']
    ec=request.session['exam_code']
    ec1=exam_code()
    nq=exam_details.objects.filter(exam_code=ec).values('no_of_ques')
    no_q=exam_details.objects.filter(exam_code=ec).values('no_of_ques')[0]["no_of_ques"]
    print(no_q)
    print(nq)
    if request.method=='POST':
        form = Ques_Setup_Form(request.POST)
        if form.is_valid():
            qu=form.cleaned_data['ques']
            op1=form.cleaned_data['option1']
            op2=form.cleaned_data['option2']
            op3=form.cleaned_data['option3']
            op4=form.cleaned_data['option4']
            cor=form.cleaned_data['correct']
            mk=form.cleaned_data['marks']
            qi=str(ec)+str("-")+str(count)
            qt=ques_table(ques_id=qi ,ques=qu , option1=op1 , option2=op2 , option3=op3 , option4=op4 , correct=cor , marks=mk , exam_code_id=ec )
            qt.save()
            if count<no_q:
                count+=1
                request.session['cnt']=count
                return redirect('ques_setup')
            else :
                return redirect('home')
    else:
        form = Ques_Setup_Form()
    return render(request , 'ques_setup.html' , {'form' : form ,'nq':nq})

def quiz(request):
    ques=ques_table.objects.all()
    
    if request.GET.get('id'):
        ques = ques.filter(ques_id__icontains=request.GET.get('id'))

    ques=list(ques)
    data=[]
    random.shuffle(ques)
    for quest in ques:
        data.append({
            "marks" : quest.marks,
            "ques" : quest.ques,
            "opt1" : quest.option1,
            "opt2" : quest.option2,
            "opt3" : quest.option3,
            "opt4" : quest.option4,
            "correct" : quest.correct,
        })

    payload ={ 'status' : True , 'data':data}
    return JsonResponse(payload)

    #if request.GET.get('category'): return redirect(f"/quiz/?category={request.GET.get('category')}")